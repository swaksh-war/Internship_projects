# import necessary packages
import re
from collections import Counter
import numpy as np
import pandas as pd

# pre processing data
def process_text(path):
    words = []
    with open(path) as f:
        file_name_data = f.read()
    file_name_data = file_name_data.lower()
    words = re.findall(r'\w+',file_name_data)

    return words

book_words = process_text(r'alice_in_wonderland.txt')
vocab = set(book_words)

# create a counter dictionary finding 
# how many times each word appears in the text
def get_count(words):
    word_count_dict = {}
    word_count_dict = Counter(words)
    return word_count_dict

word_count_dict = get_count(book_words) # dictionary with the count

# calculate probability of the occurrence
def occurr_prob(word_count_dict):
    probs = {}
    m = sum(word_count_dict.values())
    for key in word_count_dict:
        probs[key] = word_count_dict[key]/m #calculate prob for each word
    return probs

# contains the word w and the probability P(w)
prob_of_occurr = occurr_prob(word_count_dict) # variable with the probs

# Delete, Switch, Replace and Insert and return the respective list of words from each task
def del_letter(word):
    del_letter = []
    split_letter = []

    for i in range(len(word)):
        split_letter.append([word[:i],word[i:]])
    for a,b in split_letter:
        del_letter.append(a+b[1:])

    return del_letter

def switch_letter(word):
    sw_letter = []
    split_letter = []

    for c in range(len(word)):
        split_letter.append([word[:c],word[c:]])
    sw_letter = [a+b[0]+b[2:] for a,b in sw_letter if len(b>=2)]

    return sw_letter

def replace_letter(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    repl_let = []
    split_let = []

    for c in range(len(word)):
        split_let.append([word[:c],word[c:]])
    repl_let = [a+l+(b[1:] if len(b)>1 else '') for a,b in split_let if b for l in letters]
    repl_set = set(repl_let)
    repl_set.remove(word)
    #turn the set back into a list and sort it, for easier viewing
    repl_let = sorted(list(repl_set))

    return repl_let

def insert_letter(word):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    ins_let = []
    split_let = []
    for c in range(len(word)):
        split_let.append([word[:c],word[c:]])
    ins_let = [ a + l + b for a,b in split_let for l in letters]

    return ins_let

# All functions above must be used in each word in the list of words from the file by using the n-edit distance algorithm where we will use n = 1,2 only    

# so, to change one letter at a time then we choose n = 1 and implement the func bellow
def edit_one_letter(word,allow_switches=True):
    edit_one_set = set()

    edit_one_set.update(del_letter(word))
    if allow_switches:
        edit_one_set.update(switch_letter(word))
    edit_one_set.update(replace_letter(word))
    edit_one_set.update(insert_letter(word))

    return edit_one_set

# similarly, choosing to change two letters at a time:
def edit_two_letter(word,allow_switches=True):
    edit_two_set = set()

    edit_one = edit_one_letter(word,allow_switches=allow_switches)
    for w in edit_one:
        if w:
            edit_two = edit_one_letter(w,allow_switches=allow_switches)
            edit_two_set.update(edit_two)
    return edit_two_set

# get list of suggested words based in correlation between given words
def get_correlations(word,probs,vocab, n=2):
    suggestions = []
    n_best = []

    suggestions = list((word in vocab and word) or edit_one_letter(word).intersection(vocab) or edit_two_letter(word).intersection(vocab))
    try:
        n_best = [[s, probs[s]*10**2] for s in list(reversed(suggestions))]
    except KeyError:
        print("e")

    return n_best # suggested word with the probability of being right

print(10*'-')
print('Type a word to check: ',end='')
my_word = input().capitalize()
print(10*'-')
tmp_corrections = get_correlations(my_word,prob_of_occurr,vocab,2)
for i, word_prob in enumerate(tmp_corrections):
    print(f"word {i}: {word_prob[0]}, probability {word_prob[1]:.4f}")



