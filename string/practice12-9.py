""" 
	Name: Practice12-9
	Date: 12/09/2020
	Day : Saturday
  Author: Md. Aminul Islam
 Subject: Object Oriented Programming

"""

################## 01
## creating a class
# Superclass Monster
# class Monster:
# 	identity = "negative character"

# 	def __init__(self, color, heads):
# 		self.color = color
# 		self.heads = heads


# 	def attack(self):
# 		print("I am attacking...")


# # The class Fougthing: a subclass of Monster
# class Fogthing(Monster):
# 	def make_sound(self):
# 		print("Grrrrrrrrrr\n")

# # The class Mournsnake: a subclass of Monster
# class Mournsnake(Monster):
# 	def make_sound(self):
# 		print("Hisssshhhhh\n")

		
		


# # create some real monsters
# # fogthing = Monster("Black", 5)
# # mournsnake = Monster("Yellow", 4)
# # tangleface = Monster("Red", 3)


# # # check wheather those monsters got different existence in memory or not
# # print('I have ' + str(foghthing.heads) + ' heads and I\'m ' + foghthing.color)
# # print('I also have ' + str(mournsnake.heads) + ' heads and I\'m ' + mournsnake.color)
# # print('I gort ' + str(tangleface.heads) + ' heads and I\'m ' + tangleface.color)


# # create an instance/object/monster-character
# # mournsnake = Monster("Yeloow", 4)
# # # check if its created or not
# # print('I am a ' + str(mournsnake.heads) + ' headed monster.')
# # # make an attack by the new monster
# # mournsnake.attack() 

# # print('I am a ' + str(mournsnake.heads) + ' headed ' + mournsnake.identity)


# fogthing = Fogthing("Red", 5)
# print('i am ' + str(fogthing.heads) + ' headed ' + str(fogthing.color) + ' MONSTER!')
# fogthing.attack()
# fogthing.make_sound()



################## 02
## Multiple Inheritance
# Superclass A
class A:
	def where(self):
		print("I am from class A.")


# Superclass B
class B:
	def where(self):
		print("I am from class B.")


# Subclass C
class C(A, B):
	pass


an_instance_of_c = 	C()
an_instance_of_c.where()


## can call from superclass method
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()

B().spam()