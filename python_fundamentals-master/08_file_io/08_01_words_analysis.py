'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
words = []
word_dict = {}

with open('words.txt', 'r') as fin:
    for line in fin.readlines():
        line = line.rstrip()
        words.append(line)
        word_dict[line] = len(line)

v_min = min(word_dict.values())
v_max = max(word_dict.values())
shortest_word = []
longest_word = []

for word in words:
    if len(word) == v_min:
        shortest_word.append(word)
    if len(word) == v_max:
        longest_word.append(word)

print(f"Those are the shortest words with length {v_min}: {shortest_word}")
print(f"Those are the longest words with length {v_max}: {longest_word}")
print(f'The file has total {len(words)} words')
