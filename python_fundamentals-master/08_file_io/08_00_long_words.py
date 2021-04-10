'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''
word = []
with open('words.txt', 'r') as fin:
    for line in fin.readlines():
        line = line.rstrip()
        if len(line) > 20:
            word.append(line)
print(word)