'''
Print out every prime number between 1 and 100.

'''

n = 100

for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)