""" 
	Name: Practice9-9
	Date: 09/09/2020
	Day : Wednessday
  Author: Md. Aminul Islam
 Subject: File Open, Read, & Write
 	
"""

############### 01
### File Open & Close ###

# open a file from same directory
# a = open("test.txt")

# # open a file from other directory
# b = open("/home/aminul/Desktop/test1.txt")

# # open a file in write mode
# a1 = open("test.txt", "w")

# # open a file in read mode
# a2 = open("test.txt", "r")

# # open a file in append mode
# a3 = open("test.txt", "a")

# # open a file that is not a text file in write mode (such a binary file) 
# a4 = open("my_file", "wb")


# # close a file after completing its work
# file_to_work = open("test.txt", "w")
# # do HERE whatever you like, with the file
# # such as write new lines in it

# # then close it
# file_to_work.close()



############### 02
### File Read ###

# a = open("test.txt", "r")
# content = a.read()

# print(content)
# a.close()


### play with read method
# file_to_work = open("test.txt", "r")

# just_one_character = file_to_work.read(1)
# print(just_one_character)

# remaining_four_characters = file_to_work.read(4)
# print(remaining_four_characters)

# rest_of_the_file = file_to_work.read()
# print(rest_of_the_file)

# file_to_work.close()


### making python list for each line by readliness() method
# file_to_work = open("test.txt", "r")

# lines = file_to_work.readlines()
# print(lines)

# file_to_work.close()


# ### line by line print by for loop
# file_to_work = open("test.txt", "r")

# for my_line in file_to_work:
#     print(my_line)

# file_to_work.close()



############### 03
### File Write ###

# write in a file
# file_to_work = open("test.txt", "w")
# file_to_work.write("I am writing!!!")
# file_to_work.close()

# file_to_work = open("test.txt", "r")
# print(file_to_work.read())
# file_to_work.close()


# show the size of the written file
# file_to_work = open("Test.txt", "w")
# is_writing_done = file_to_work.write("I am writing!!!")

# if is_writing_done:
#     print("Yes, {0} byte(s) has been written!".format(is_writing_done))
# file_to_work.close()


## append
# a = open("test.txt", "a")
# a.write("new line.")

# a = open("test.txt", "r")
# print(a.read)

### create a file
# f = open("newFile.txt","w")
# f.write("My Name is " + input("Enter your name: "))
# f.close()

# b = open("newFile.txt","r")
# content = b.read()
# print(content)
# b.close()


## file open with a temporary variable (best practice)
## by using this no need to close the file it will close automatically
with open("test.txt") as f:
    print(f.read())