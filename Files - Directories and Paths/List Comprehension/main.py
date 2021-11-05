# This new list should contain every number in the list 'numbers' but each number should be squared.
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [sq**2 for sq in numbers]
print(squared_numbers)

# This new list should only contain the even numbers from the list numbers.
even_result = [even for even in numbers if even % 2 == 0]
print(even_result)

# create two files - file1.txt and file2.txt . Create a list called result which contains the numbers that are common
# in both files.

with open("file1.txt") as file_1:
    list_in_file1 = file_1.readlines()

with open("file2.txt") as file_2:
    list_in_file2 = file_2.readlines()

result = [int(element) for element in list_in_file1 if element in list_in_file2]
print(result)
