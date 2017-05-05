"""
remove raw doc that is not starts with `{"created_at"`
needed for the raw tweets collected by twitter4J during 2013-2015
"""

from os import listdir
from os.path import isfile, join

paths = ['2015-09', '2015-10']
for mypath in paths:
    print(mypath)
    files = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]

    outpath = mypath+'.txt'
    for file in files:
        with open(file, 'r', encoding='utf-8', errors='ignore') as infile, open(outpath, 'a', encoding='utf-8', errors='ignore') as outfile:
            for line in infile:
                if line.startswith('{"created_at"'):
                    outfile.write(line)
    print('done')           