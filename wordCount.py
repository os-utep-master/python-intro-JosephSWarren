import sys
import re
import os
import subprocess

if len(sys.argv) is not 2:
    print("Correct usage: wordCount.py <input text file>")
    exit()

textFname = sys.argv[1]

if not os.path.exists(textFname):
    print("text file input %s doesn't exist! Exiting" %textFname)
    exit()

outputWriter = open("output.txt", "w+")

wordDictionary = {}

with open(textFname, 'r') as textFile:
    for line in textFile:
        for word in re.split("\s", line):
            re.sub("\W", '', word)
            if word in wordDictionary:
                wordDictionary[word]+=1
            else:
                wordDictionary[word]=1
sorted(wordDictionary)

for word in wordDictionary:
    outputWriter.write("%s %d\n" % (word, wordDictionary[word]))