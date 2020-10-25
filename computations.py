""" 
	Name: computations
	Date: 24/09/2020
	Day : Thursday
  Author: Md. Aminul Islam
 Subject: Computations
 			1. Simple Interest
 			2. Compound Interest
 			3. Grades Calculation
 			4. Gravitational Force
 			5. Triangle Area
"""

###1. Simple Interest
# P = Principal, R = Interest Rate, N = Number of Years, I = Interest
# p = float(input("Enter the Principal: "))
# r = float(input("Enter the Interest Rate: "))
# n = float(input("Enter the Number of Years(Duration): "))

# i = p * (r/100) * n
# a = p + i

# print('The Interest is:', round(i,2),'BDT')
# print('You have to pay total:', round(a,2),'BDT')


###2. Compound Interest
# def compound_interest(p,r,n):
# 	a = round(p * (1+r/100)**n)
# 	return a

# p = float(input("Enter the Principal: "))
# r = float(input("Enter the Interest Rate: "))
# n = float(input("Enter the Number of Years(Duration): "))
# print('You have to pay total:', compound_interest(p,r,n),'BDT')


###3. Grades Calculation
# def cal_grade(avg):
# 	if avg >= 80:
# 		Grade = "A+"
# 	elif avg >= 70:
# 		Grade = "A"
# 	elif avg >= 60:
# 		Grade = "A-"
# 	elif avg >= 50:
# 		Grade = "B"
# 	elif avg >= 40:
# 		Grade = "C"
# 	elif avg <= 33:
# 		Grade = "F"

# 	return Grade



# # user inputs
# n = int(input("How many subjects: "))
# subjects = []

# for i in range(n):
# 	s = int(input("Enter subject-{0}'s marks: ".format(i+1)))
# 	subjects.append(s)

# avg = sum(subjects)/n

# print('Your average marks is:',avg)
# print('You got:', cal_grade(avg))


###4. Gravitational Force
# G = 6.673 * pow(10, -11)
# m1 = float(input("Enter the mass of the first object: "))
# m2 = float(input("Enter the mass of the second object: "))
# r = float(input("Distence between the objects: "))

# F = ((G * m1 * m2) / pow(r, 2))

# print('Gravitational Force between the objects is:', F, "N")

###5. Triangle Area
import math
def triangle_area(a,b,c):
	s = (a+b+c)/2
	area = math.sqrt(s*(s-a)*(s-b)*(s-c))
	return round(area,3)


a = int(input("Enter first side: "))
b = int(input("Enter first side: "))
c = int(input("Enter first side: "))

print('Area of the triangle is: ', triangle_area(a,b,c))