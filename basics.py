"""
Write a function to reverse a string.
Create a dictionary from two lists using a dictionary comprehension.
Write a function that takes a list and returns the second largest number.
Explain the difference between is and ==.
Create a lambda function to filter even numbers from a list.
Use a try-except block to handle division by zero.
Open a file, write some data, and close it properly.
Implement a generator that yields the Fibonacci sequence.
Explain how Python’s defaultdict works with an example.
Write a program to check if a given string is a palindrome.
"""

# Write a function to reverse a string.

example_str = "123456789"
reversed = ""
len_str = len(example_str)

for ind in range(len_str):
    reversed+= example_str[len_str-1-ind]
print(reversed)

# Create a dictionary from two lists using a dictionary comprehension.

list_1 = [1,2,3,4,5]
list_2 = ['a', 'b', 'c', 'd', 'e']
assert len(list_1) == len(list_2)
combined_lists_dict = {a:b for a,b in zip(list_1, list_2)}
print(combined_lists_dict)

# Write a function that takes a list and returns the second largest number.

list_1 = [13,15,22,9, 4, 9]
max_index = list_1.index(max(list_1))
list_1[0], list_1[max_index] = list_1[max_index], list_1[0]
print("Second max", max(list_1[1:]))

# Explain the difference between is and ==.

"""
equal operator equates the value of the variables, while 'is' is checking if they are actually 
pointing towards the same value in memory
"""


# Create a lambda function to filter even numbers from a list.
list_nums = [1,2,3,4,5,6,11,12,13,14]

filt_even = lambda x: [a for a in x if a % 2 ==0]
print(filt_even(list_nums))

# Use a try-except block to handle division by zero.

try: 
    3/0
except ArithmeticError as e:
    print(e)

# Open a file, write some data, and close it properly.

with open("file.txt", "w") as f:
    f.write("Hello file!")

# Implement a generator that yields the Fibonacci sequence.

fibonacci_legnth = 10
def fibonacci_series(length):
    before_last_element, last_element = 0, 1
    for i in range(length):
        yield before_last_element
        before_last_element, last_element = last_element, before_last_element + last_element
print(list(fibonacci_series(fibonacci_legnth)))

# Explain how Python’s defaultdict works with an example.

