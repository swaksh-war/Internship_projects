from filesplit.split import Split
import os
filename = r'/home/dingo/code/internship_projects/Internship_projects/Crypto/file splitting/surplusmed.txt'
filesize = os.path.getsize(filename)
chunkedsize = filesize//2
act_file_name = filename.split('/')[-1]
os.mkdir(f'store/{act_file_name}')
fs = Split(inputfile=filename, outputdir=f'store/{act_file_name}')
fs.bysize(chunkedsize)

