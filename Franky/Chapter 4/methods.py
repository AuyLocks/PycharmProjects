# # Finding a Value in a List with the .index() Method
#
# spam = ['hello', 'hi', 'howdy', 'heyas']
# print(spam.index('hello'))   # results would be 0
# print(spam.index('heyas'))   # results would be 3
# print(spam.index('howdy howdy howdy'))  # ValueError: 'howdy howdy howdy' is not in list
#
# # when there are duplicates of values in the list it will always give the index value of the first instance
# eggs = ['Zophie', 'Pooka', 'Fat-tail', 'Pooka']
# print(eggs.index('Pooka'))   # index result would be 1

###########################################

# # Adding values to lists with the append() and insert() methods

# spam = ['cat', 'dog', 'bat']
# spam.append('moose')
# print(spam)    # spam = ['cat', 'dog', 'bat', 'moose]
#
# spam.insert(1, 'chicken')
# print(spam)    # spam = ['cat', 'chicken', 'dog', 'bat', 'moose']

#############################################

# Removing Values from lists with remove()

# spam = ['cat', 'bat', 'rat', 'elephant']
# spam.remove('rat')
# print(spam)    # spam = ['cat', 'bat', 'elephant']
#
#             ####################
#
# spam = ['cat', 'bat', 'rat', 'elephant']
# spam.remove('chicken')      # ValueError: list.remove(x): x not in list
#
#             ####################
#
# spam = ['cat', 'bat', 'rat', 'cat', 'hat', 'cat']
# spam.remove('cat')
# print(spam)   # spam = ['bat', 'rat', 'cat', 'hat', 'cat']
# #The del statement is good to use when you know the index of the value you want to remove from the list. The remove() method is good when you know the value you want to remove from the list.

########################################################

## Sortind the Values in a List with the sort() Method

# spam = [2, 5, 3.14, 1, -7]
# spam.sort()
# print(spam)   # returns [-7, 1, 2, 3.14, 5]
#
# spamOne = ['cats', 'ants', 'dogs', 'badgers', 'elephants']
# spamOne.sort()
# print(spamOne)   # returns ['ants', 'badgers', 'cats', 'dogs', 'elephants']
#
# spam.sort(reverse=True)
# print(spam)      # returns [5, 3.14, 2, 1, -7]
#
# ## you can not sort list with both string values and numerical values.
# ## sort() uses "ASCIIbetical order so capital leter will come before lower case ones.
#
# spamTwo =['Alice', 'ants', 'Bob', 'badgers', 'Carol', 'cats']
# spamTwo.sort()
# print(spamTwo)   # returns ['Alice', 'Bob', 'Carol', 'ants', 'badgers', 'cats']
#
# spamTwo.sort(key=str.lower)
# print(spamTwo)   # returns ['Alice', 'ants', 'badgers', 'Bob', 'Carol', 'cats']
# ## sort with the key=str.lower case will put the list into alphabetical order

            #############################

## Reversing the Values in a List with the reverse() Method

# spam = ['cat', 'dog', 'moose']
# spam.reverse()
# print(spam)   # returns ['moose', 'dog', 'cat']





