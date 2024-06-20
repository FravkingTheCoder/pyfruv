import math
import random

# getting good at python


# below is some intro stuff that im just re checking
'''
# print("hello")
# integer = 4  # all numbers without decimals
# floats = 4.2122
# bools = True or False
# message = "wop wop wop wop wop dot fuck em up \n\t lmao"
# print(message)
#
# url = "https://github.com/FravkingTheCoder/linuxtings"
# print(url.removeprefix("https://"))
# print(url.removesuffix("linuxtings"))
#
# famous_person = "Biraja Swain"
# quote = f'{
# 	famous_person} once said, "When life throws punches at you, you throw punches back"'
# print(quote)

# name = "\tFrvsh\nB\tSwain\n	"
# print(name)
# print(name.lstrip())
# print(name.rstrip())
# print(name.strip())
#
'''

# shenanigans using lists
# gay = ['faggot','gay','lil nas x','america', 'joe biden']
# print(gay)
#
# # accessing individual elements of lists
# print(gay[1]) # accessing the 2nd element of the list since indexing in python starts with 0
#
# lmao = f"the most retarded united states president is {gay[4].title()}"
# print(lmao)

# using numbers lists with

# numbers = [1]
# for i in range(100):
# 	numbers.append(i)
# 	numbers.reverse()
# 	pront = f"nigga {numbers}"
# 	print(pront)
# 	print(len(numbers))
#
#
 
# for i in range(5): # starts from index 0 if no starting value is specified
# 	print(i)
#
# # make sure to adjust by 1 when trying to use range function
# for i in range(1,5):
# 	print(i)

# the end number in range() is not included when counting

#for i in range(1, 20):
#   lissts = []
#   lissts.append(i)
#   print(lissts)

'''when using for loops, make the list before the loop otherwise it will make a new list everytime'''  

# numbers = [i**2 for i in range(1, 30)] # this is list comprehension as the for loop is included in the list the temporary variable is used to fill the list
# # list comprehension already appends the values beforehand all in one line of code
#
# sqrts = (numbers[0:4]) # splicing the list, gives us the values from index 0 to 4
# sqrts_list = []
# for power in sqrts:
# 	root = math.sqrt(power)
# 	sqrts_list.append(root)
#
# print(sqrts_list)
#

'''List slicing'''
# # finding the items between given index values
# nums = [num * 2 for num in range(5)]
# print(nums[:3]) # prints items from the begininning till the third index
# print(nums[:-3])
# print(nums)
# '''
# output:
# [0, 2, 4]
# doesnt include the value of the third index
# '''
#
# # copying lists
# nums2 = [nums[:]]
# # the above line just copies every item from the beginning to the end, since we didnt specify
# # the end splice
#
#


'''
using tuples
'''

# tuples are lists that use () instead of []
# they are also immutable, and cannot be modified after creation

tuples = ("ucm", "muc", "mcu")
tups = (1,)

# if I wanted to change the above tuple "tuples", then I would have to make a new tuple with the same name and override the values


# toppings = ["chicken", "meth", "chilles"]
# for top in toppings:
# 	if top == "meth":
#     	print("we gotta cook jessie")
# 	else:
#     	print(f"adding {top} to ur shitty pizza")
#  

# usernames = ['bob', 'bps75', 'admin', 'krispyninja', 'ch', 'good2me']
# if usernames: # gives true if there is atleast one item in the list, false if not
# 	for user in usernames:
#     	if user == 'admin':
#       	print('welcome back admin, want to look at security settings?')
#     	else:
#         	print(f"Hello {user}, welcome back.")
# else:
# 	print('No users currently added')


''' Dictionaries '''
# a method of storing different types of data about someone/something as key:value pairs
# for example, in a phone book(dictionary), you can a person named alice{key} and her number{value}

phone_book = {"alice":983, "john":121, "dream":911} # uses curly brackets
# each key:value pair is separated by a comma

phone_book['pop'] = 9886380436 # this is how u add to the dictionary, inside the brackets is the key and then you specify the value it equals to

#  for key in phone_book:
#   if phone_book[key] == 911:
# 	print(f'oh shit its dream call the cops on his ass: {phone_book[key]}')
# 	print("Ring.\nRing..\nRing...\nDREAM ON THE GROUND U PREDATOR WE KNOW U LIKE KIDS")
# 	print("Calling Control, suspect tried to flee but we shot him and got him down.")
# 	break
#   else:
# 	print(f"{key}:{phone_book[key]}")
# 

for key,value in phone_book.items():
  print(f"\nKey: {key}")
  print(f"Value: {value}")

print(phone_book.items())
