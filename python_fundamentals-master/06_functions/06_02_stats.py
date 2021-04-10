'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [1, 2, 3, 4, 5, 6, 7]



def stats(ls):
    max_n = max(ls)
    min_n = min(ls)
    avg_n = sum(ls)/len(ls)
    sum_n = sum(ls)
    return max_n, min_n, avg_n, sum_n


# call the function below here
print(stats(example_list))
