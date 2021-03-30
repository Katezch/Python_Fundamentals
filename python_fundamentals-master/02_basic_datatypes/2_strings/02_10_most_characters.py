'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''

s1 = input("enter string1:")
s2 = input("enter string2:")
s3 = input("enter string3:")

print(len(s1), ", ", s1, "\n", len(s2), ", ", s2, "\n", len(s3), ", ", s3)
