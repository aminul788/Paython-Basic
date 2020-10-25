	########## FUNCTION ###########
# ##################### 01
# # defining the function named hi
# def hi():
# 	print("hi Everyone!")

# # calling the function to use it.
""" 
	Name: Practice8-9
	Date: 08/09/2020
	Day : Tuesday
  Author: Md. Aminul Islam

"""

# hi()

# #again calling the fuction named hi
# hi()



################### 02
# def sum(x,y):
# 	z = x + y
# 	print(z)

# a = int(input("a: "))
# b = int(input("b: "))

# sum(a,b)


################# 03
# def sum(*args):
# 	sum = 0
# 	for num in args: 	#here, args is like a touple which is (12,10,20,25)
# 		sum += num
# 	return sum

# print(sum(12,10,20,15))


# ################# 04
# def print_dic(**args):
# 	print(args)


# print_dic(a=1, b=2, c=2)

# # or,we can write as below
# def print_dic2(**args):
# 	for a in args:
# 		print("{0} : {1}".format(a, args[a]))

# print_dic2(a=1,b=2,c=3)


# ################ 05
# def print_all(a,*args,**kwargs):
# 	print(a)
# 	print(args)
# 	print(kwargs)

# print_all(10,20,30,50,c=60,b=100)



################## 06
# def get_larger(x,y):
# 	if x>y:
# 		return x
# 	else:
# 		return y

# a = int(input("A : ")) 
# b = int(input("B : "))
# c = get_larger(a,b)

# print("{0} is larger.".format(c))



################### 07
# def greet(word):
#     """
#     Print a word with an
#     exclamation mark following it.
#     """
#     print(word + "!")

# # What the fucntion does?
# print(greet.__doc__)

# # Make sense, now lets use it    
# greet("Hello World")


## doc string.....
# def square_root(n):
#     """Calculate the square root of a number.

#     Args:
#         n: the number to get the square root of.
#     Returns:
#         the square root of n.
#     Raises:
#         TypeError: if n is not a number.
#         ValueError: if n is negative.

#     """
#     pass

# print(square_root.__doc__)



################## 08
# def beautify(text):
#     return text + '!!!'


# def make_line(func, words):
#     return "Hello " + func(words)


# print(make_line(beautify, "world"))



##################### 09
# import random

# value = random.randint(1, 100)
# print(value)


# # import pi,sqrt from module math
# from math import pi, sqrt

# print(pi)
# print(sqrt(25))


# # or can import as below
# from math import sqrt as square_root

# print(square_root(100))


############# exception handling
#################### 10
# try:
# 	a = 1000
# 	b = int(input("Enter a divisior to devide 1000: "))
# 	print(a/b)
# except ZeroDivisionError:
# 	print("You entered 0 which is not permited!")


# another one 
# try:
#     word = "spam"
#     print(word / 0)
# except:
#     print("An error occurred")


# usees of finally
# try:
# 	print("hello")
# 	print(1/0)
# except ZeroDivisionError:
# 	print("Devided by zero!")
# finally:
# 	print("This code will run no matter what")

