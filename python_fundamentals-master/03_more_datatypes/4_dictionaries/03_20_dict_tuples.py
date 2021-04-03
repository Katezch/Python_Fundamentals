'''
CHALLENGE: Write a script that sorts a dictionary into a list of tuples based on values. For example:

input_dict = {"item1": 5, "item2": 6, "item3": 1}
result_list = [("item3", 1), ("item1", 5), ("item2", 6)]

NOTE: Check out the Python docs and see whether you can come up with a solution, even if you don't yet
      completely understand _why_ it works the way it does:
      https://docs.python.org/3/howto/sorting.html#key-functions
      Feel free to discuss any questions you have with your mentor and on the forum!


first try solution
input_dict = {"item1": 5, "item2": 6, "item3": 1}

v = []
result_list = []
for value in input_dict.values():
    v.append(value)

v = sorted(v)

for i in v:
    for key in input_dict.keys():
        if input_dict[key] == i:
            result_list.append((key,i))

'''


input_dict = {"item1": 5, "item2": 6, "item3": 1}

result_list = []

for k, v in input_dict.items():
    result_list.append((k, v))

result_list = sorted(result_list, key=lambda x: x[1])
print(result_list)

