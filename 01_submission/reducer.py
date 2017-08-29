#!/usr/bin/python
import sys

total = 0
current_word = None

for line in sys.stdin:
    word, count = line.replace('\n', '').strip().split(' ')
    if current_word:
        if word == current_word: 
            total += int(count)
        else:
            print current_word, total
            total = int(count)
            current_word = word

    current_word = word

print current_word, total