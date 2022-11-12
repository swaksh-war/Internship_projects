import argparse
import os
import spacy
from nltk.stem.lancaster import LancasterStemmer
import scripts.align_text as align_text
import scripts.cat_rules as cat_rules
import scripts.toolbox as toolbox

def main(args):
	# Get base working directory.
	basename = os.path.dirname(os.path.realpath(__file__))
	print("Loading resources...")
	# Load Tokenizer and other resources
	nlp = spacy.load("en")
	# Lancaster Stemmer
	stemmer = LancasterStemmer()
	# GB English word list (inc -ise and -ize)
	gb_spell = toolbox.loadDictionary(basename+"/resources/en_GB-large.txt")
	# Part of speech map file
	tag_map = toolbox.loadTagMap(basename+"/resources/en-ptb_map")	
	# Setup output m2 file
	out_m2 = open(args.out, "w")

	print("Processing files...")
	# Load the lang8 test file
	with open(args.lang8) as lang8_file:
		for line in lang8_file:
			line = line.strip()
			# Ignore empty lines
			if not line: continue
			line = line.split("\t")
			orig_sent = line[4].strip()
			cor_sents = line[5:]
			# Write the original output
			out_m2.write("S "+orig_sent+"\n")
			# If no cor_sents, write a noop edit and continue
			if not cor_sents:
				out_m2.write("A -1 -1|||noop|||-NONE-|||REQUIRED|||-NONE-|||0\n\n")
				continue
			# Markup the original sentence with spacy (assume tokenized)
			proc_orig = toolbox.applySpacy(orig_sent.split(), nlp)
			# Loop through alternative corrected sentences
			for cor_id, cor_sent in enumerate(cor_sents):
				# Markup each corrected sentence with spacy (assume tokenized)
				proc_cor = toolbox.applySpacy(cor_sent.strip().split(), nlp)
				# Auto align the parallel sentences and extract the edits.
				auto_edits = align_text.getAutoAlignedEdits(proc_orig, proc_cor, nlp, args)
				# If there are no edits, orig and cor are the same so write a noop.
				if not auto_edits:
					out_m2.write("A -1 -1|||noop|||-NONE-|||REQUIRED|||-NONE-|||"+str(cor_id)+"\n")
				# Loop through the edits.
				for auto_edit in auto_edits:
					# Give each edit an automatic error type.
					cat = cat_rules.autoTypeEdit(auto_edit, proc_orig, proc_cor, gb_spell, tag_map, nlp, stemmer)
					auto_edit[2] = cat
					# Write the edit to the output m2 file.
					out_m2.write(toolbox.formatEdit(auto_edit, cor_id)+"\n")
			# Write a newline when there are no more edits.
			out_m2.write("\n")		
			
if __name__ == "__main__":
	# Define and parse program input
	parser = argparse.ArgumentParser(description="Convert an English Lang8 (v1.0) file into m2 format.",
									formatter_class=argparse.RawTextHelpFormatter,
									usage="%(prog)s [-h] [options] lang8 -out OUT")
	parser.add_argument("lang8", help="A path to the Lang8 (v1.0) data.")
	parser.add_argument("-out", help="The output filepath.", required=True)
	parser.add_argument("-lev", help="Use standard Levenshtein to align sentences.", action="store_true")
	parser.add_argument("-merge", choices=["rules", "all-split", "all-merge", "all-equal"], default="rules",
						help="Choose a merging strategy for automatic alignment.\n"
							"rules: Use a rule-based merging strategy (default)\n"
							"all-split: Merge nothing; e.g. MSSDI -> M, S, S, D, I\n"
							"all-merge: Merge adjacent non-matches; e.g. MSSDI -> M, SSDI\n"
							"all-equal: Merge adjacent same-type non-matches; e.g. MSSDI -> M, SS, D, I")
	args = parser.parse_args()
	# Run the program.
	main(args)