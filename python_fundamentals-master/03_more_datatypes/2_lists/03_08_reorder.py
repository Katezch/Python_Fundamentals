'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

cnt = 0
ls = []

while cnt < 10:
    num = int(input("enter a number: "))
    ls.append(num)
    cnt += 1

new_ls = []
for i in range(1, 10, 2):
    new_ls.append(ls[i])

for i in range(8, -1, -2):
    new_ls.append(ls[i])

print(ls)

print(new_ls)