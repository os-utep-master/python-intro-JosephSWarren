import sys
import re
import os
import subprocess

if len(sys.argv) is not 3:
    print("Correct usage: wordCount.py <input text file> <output text file>")
    exit()

textFname = sys.argv[1]

if not os.path.exists(textFname):
    print("text file input %s doesn't exist! Exiting" %textFname)
    exit()

allWords = []
with open(textFname, 'r') as textFile:
    for line in textFile:
        allWords.extend(re.findall(r"\w+", line))
        
wordDictionary = {}
for word in allWords:
    word=word.lower()
    if word in wordDictionary:
        wordDictionary[word]+=1
    else:
        wordDictionary[word]=1

outputWriter = open("%s" % sys.argv[2], "w+")

for key in sorted(wordDictionary.keys()):
    outputWriter.write("%s %d\n" % (key, wordDictionary[key]))
