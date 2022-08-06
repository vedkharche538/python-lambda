# basic lambda
from functools import reduce
print((lambda x, y: x+y)(2, 3))
# %%
num = [45, 10, 6, 24, 5, 4, 90, 16]
filter_result = filter(lambda x: x % 2 == 0, num)
print(list(filter_result))
# %%
name = ["harsh", "shyam", "akash"]

print(filter(lambda x: x.startswith("a"), name))
# %%
# write a python program to count the student above 18
stu_data = {1: ["sam", 15], 2: ["ram", 16], 3: ["shyam", 18], 4: ["harsh", 30]}
len(list(filter(lambda x: x[1] > 18, stu_data.values())))

# %%
# %%
# %%
# write a python program to count the student above 18
stu_data = {1: ["sam", 15], 2: ["ram", 16], 3: ["shyam", 18], 4: ["harsh", 30]}
print(list(filter(lambda x: x[1] > 18, stu_data.values())))
# %%
# MAP function
num = [45, 10, 6, 24, 5, 4, 90, 16]
filter_result = map(lambda x: x*x, num)
print(list(filter_result))

# %%
l1 = [2, 3, 5]


def square(x):
    return x*x


print(list(map(square, l1)))
# %%
seq = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x*y, seq)
print(product)

# %%
# no of names starts with S word using map
name = ["suraj", "sagar", "shyam", "siddharth", "amar"]
print(sum(map(lambda x: x.startswith("S"), name)))

# %%
# create  alist of name consisting of first and last name and combime them
data = [["Ankur", "Avik", "Kiran"], ["Nagar", "Sarkar", "Kumar"]]
list(map(' '.join, zip(*data)))
# %%
# another way to do the same
data = [["Ankur", "Avik", "Kiran"], ["Nagar", "Sarkar", "Kumar"]]
first_name = data[0]
second_name = data[1]

name = list(map(lambda x, y: x+" "+y, first_name, second_name))
print(name)

# %%
# Extract the multiples of 5

input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
              15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
list(filter(lambda x: x % 5 == 0, input_list))

# %%
"""You are given a list of strings such as input_list = ['hdjk', 'salsap', 'sherpa']
.Extract a list of names that start with an ‘s’ and end with a ‘p’
(both 's' and 'p' are lowercase) in input_list."""
input_list = ['hdjk', 'salsap', 'sherpa']
list(filter(lambda x: x.startswith("s") and x.endswith("p"), input_list))

# %%
"""Reduce Function
Description Using the Reduce function, concatenate a list of words in input_list, and print the output as a string.
If input_list = ['I','Love','Python'], the output should be the string 'I Love Python'.
    """
from functools import reduce
input_list = ['All','you','have','to','fear','is','fear','itself']
str(reduce(lambda x, y: x+" "+y, input_list))



# %%
'''You are given a list of numbers such as input_list = [31, 63, 76, 89]. Find and print the largest number in input_list using the reduce()
function.
'''
input_list = [99, 63, 76, 89]
int(reduce(lambda x,y:x if x>y else y, input_list))

# %%
#sum of the squares of 2 given numbers

(lambda x,y:x**2+y**2)(3,4)

# %%
#Write a lambda function to check a number is even or odd
li = [2,3,4,5,6,7,8,9,10]

list(map(lambda x:"even" if x%2==0 else "odd", li))


# %%
