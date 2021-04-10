'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

words = []

with open('words.txt', "r") as fin:
    for line in fin.readlines():
        words.append(line.rstrip())


words_reverse = []

for i in range(len(words)-1, -1, -1):
    words_reverse.append(words[i])

with open('words_reverse.txt', 'w') as fout:
    fout.write('\n'.join(words_reverse))


