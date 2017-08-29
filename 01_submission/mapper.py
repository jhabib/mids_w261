#!/usr/bin/python
import sys
import re

count = 0
WORD_RE = re.compile(r"[\w']+")
filename = sys.argv[2]
findword = sys.argv[1].lower()

with open (filename, "r") as myfile:
    for line in myfile:
        for match in WORD_RE.findall(line):
            if match.lower() == findword:
                print findword, 1