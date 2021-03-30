'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''

m = input("Enter a string")
list_ = m.split(sep=' ')
result_list = []

for i in list_:
    l_ = []
    for j in i:
        l_.append(j)
    t = tuple(l_)
    result_list.append(t)

print(result_list)
