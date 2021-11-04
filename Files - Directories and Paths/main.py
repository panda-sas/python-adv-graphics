# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# Reading a file
with open("/Users/Saswati Panda/OneDrive/Desktop/my_file.txt") as f:
    contents = f.read()
    print(contents)

# Writing a file
with open("/Users/Saswati Panda/OneDrive/Desktop/my_file.txt", mode="a") as file:
    file.write("\nThis is another new line of text - v2. ")

# Creating a file
# with open("another_file.text", mode="w") as file_2:
#     file_2.write("This is a second file. ")


