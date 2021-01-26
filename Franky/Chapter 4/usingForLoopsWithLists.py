# supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
# for i in range (len(supplies)):
#     print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

#######################################

# # The In and Not In operators
# spam = ['hello', 'hi', 'howdy', 'heyas']
#
# 'cat' in spam   # False
# 'howdy' not in spam   # False
# 'howdy' in spam       # True
# 'cat' not in spam     # True

#######################################

# # myPets
#
# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# print('Enter a pet name:')
# name = input()
# if name not in myPets:
#     print('I do not have a pet named ' + name)
# else:
#     print(name + ' is my pet.')

###########################################

# # The Multiple Assigment Trick is a shortcut that lets you assign multiple variables with the values in a list in one line of code
#     # The long way of doing it
#
# cat = ['fat', 'orange', 'loud']
# size = cat[0]
# color = cat[1]
# disposition = cat[2]
# print(size + color + disposition)

        ###################

# # The faster way of doing multiple assignment
# cat = ['fat', 'orange', 'loud']
# size, color, disposition = cat
# print(size + color + disposition)

        ###################

# # This trick can only be used to assign variables for the exact length of the list
# cat = ['fat', 'orange', 'loud']
# size, color, disposition, name = cat  # This will produce an error since the is no forth item in the list
#                                       # ValueError: not enough values to unpack

        ###################

# # This trick can also be used to swap variables
#
# a, b = 'Alice', 'Bob'
# a, b = b, a
# print(a)
# print(b)

#############################################

# # Augmented Assignment Operators
#
# spam = 42
# spam = spam + 1   # 43
#
# # A shortcut is useing +=
#
# spam = 42
# spam += 1
#
# # It can also be used with different operators such as +, -, *, /, and %
#
# spam = 'Hello'
# spam += ' world!'
# print(spam)
#
# bacon = ['Zophie']
# bacon *= 3
# print(bacon)

################################################

# supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
# for index, item in enumerate(supplies):
#     print('Index ' + str(index) + ' in supplies is: ' + item)
## enumerate() function returns to values the index in the list and the actual item in the list.

# ###################################################
#
# # Using the random.choice() and random.shuffle() functions with Lists
#           #############
# import random
# pets = ['Dog', 'Cat', 'Moose']
# print(random.choice(pets))
#
# # random.choice() gets one item from the list at random
#             #############

import random
people = ['Colette', 'Franky', 'Oscar']
random.shuffle(people)

#
# ## only works in terminal, what i currently have in code returns None

            ##################







