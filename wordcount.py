#!/usr/bin/env python


f = open('/Users/antonsolovyev/Documents/usdeclar.txt')
contents = f.read()

word_counts = {}
for s in contents.split():
    word_counts[s] = int(word_counts.get(s, '0')) + 1

for w in sorted(word_counts.keys()):
    print('word: "%s" occurs: %d times' % (w, word_counts[w]))