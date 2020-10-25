""" 
	Name: Practice9-9f
	Date: 9-10/09/2020
	Day : Wednessday & Thursday
  Author: Md. Aminul Islam
 Subject: Function

"""


################ 01

# my_list = []
# def my_function(arg):
# 	my_list.append(arg)

# my_function(10)

# print(my_list)



################# 02
# def oddOrEven(x):
# 	if x % 2 == 0:
# 		print("{0} is a EVEN Number.\n".format(x))
# 	else:
# 		print("{0} is an ODD Number.\n".format(x))
# i = 0
# while i<1:
# 	num = int(input("Enter your Number: "))
# 	if num == 0:
# 		break
# 	oddOrEven(num)


############### 03
## Using of anonymous function lambda

# a = int(input("x: ")) 
# b = int(input("y: ")) 
# print((lambda x,y: x + 2 * y)(a,b))


### map function
# def make_double(x):
# 	return x * 2

# my_marks = [10, 20, 12, 15]
# result = map(make_double, my_marks)
# print(list(result))


# ### filter function
# def is_even(x):
# 	return x % 2 == 0

# nums = range(1,10)
# result = filter(is_even, nums)
# print(list(result))


# ### filter and lambda function
# nums = range(1,10)
# result = list(filter(lambda x: x % 2 == 0, nums))
# print(result)


############### 04
###  generator by using yield
# def my_iterable():
# 	i = 5
# 	while i > 0:
# 		yield i
# 		i -= 1

# for i in my_iterable():
# 	print(i)


# ### another example
# def even_numbers(x):
# 	for i in range(x):
# 		if i % 2 == 0:
# 			yield i

# user_input = int(input("X: ")) 
# even_nums_list = list(even_numbers(user_input))
# print(even_nums_list)


### Decorator
# def my_decorator(func):
# 	def decorate():
# 		print("--------------")
# 		func()
# 		print("--------------")
# 	return decorate

# # def print_raw():
# # 	print("Clear Text")

# # print_raw = my_decorator(print_raw)
# # print_raw()


# @my_decorator
# def print_text():
#     print("Hello World!")

# print_text()


################# 04
### recursion (factorial)
# def factorial(x):
# 	if x == 1:
# 		return 1
# 	else:
# 		return x * factorial(x-1)

# print(factorial(5))


# first = {1, 2, 3, 4, 5, 6}
# second = {4, 5, 6, 7, 8, 9}

# print(first | second)
# print(first & second)
# print(first - second)
# print(second - first)
# print(first ^ second)



################## 05
### itertools
# from itertools import count

# for  i in count(50):
# 	print(i)
# 	if i >= 100:
# 		break

from itertools import accumulate

my_numbers = [1, 2, 3, 4, 5, 6]
accumulated_numbers = accumulate(my_numbers)
list_of_accu_nums = list(accumulated_numbers)
print(list_of_accu_nums)