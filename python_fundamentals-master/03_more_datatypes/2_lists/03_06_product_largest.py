'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''

cnt = 0
ls = []



while cnt < 10:
    num = int(input("enter a number: "))
    ls.append(num)
    cnt += 1

m = ls[0]
s = 1
for i in ls:
    s *= i
    if i > m:
        m = i


print(m)
print(s)