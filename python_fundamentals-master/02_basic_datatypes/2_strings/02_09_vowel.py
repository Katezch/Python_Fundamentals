'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

s = input("enter a string here: ")
v = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
s_lower = s.lower()

cnt_a = 0
cnt_e = 0
cnt_i = 0
cnt_o = 0
cnt_u = 0

for i in s_lower:
    for k in v.keys():
        if i == k:
            v[k] += 1

for k, v in v.items():
    print(k,v)



