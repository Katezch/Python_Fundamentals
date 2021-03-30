'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

m = input("enter a string:")
list_ = m.split(sep=' ')
d = {}

for i in list_:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

for k, v in d.items():
    print(k, v)

