# # Examples of Simple List
# [1,2,3]
# ['cat','bat','rat','elephant']
# ['Hello',3.1415,True,42]
# spam = ['cat','bat','rat','elephant']  #spam is only assigned one value and it is the list value

########################################

# #Getting Individual Values in a List with Indexes
#
# spam = ['cat','bat','rat','elephant']
# print(spam[1])
# print('The ' + spam[1] + ' ate the ' + spam[0] + '.')

##########################################

# # Accessing a list within a list
#
# spam = [['cat' , 'bat'],[10 , 20, 30, 40, 50]]
# print(spam[0])   # out put is ['cat' , 'bat']
# print(spam[1][3])  #output 40

###########################################

# #Negative Indexes
# spam = ['cat','bat','rat','elephant']
# spam[-1]  # 'elephant'
# spam[-3]  # 'bat'

#############################################

# # Getting Sublists with Slices
#    # spam[2] is a list with an index
#    # spam[1:4] is a list with a slice
#         #The first number indicates where it starts the second index number is where it ends but does not include that item.
#
# spam = ['cat','bat','rat','elephant']
# spam[0:4]    # ['cat','bat','rat','elephant']
# spam[1:3]    # ['bat', 'rat']
# spam[0:-1]   # ['cat','bat','rat']
#
#     # Leaving one index out
#         # Leaving the index number to the left of the colon is the same as starting at 0
# spam[:2]    # ['cat','bat']
#
#         # Leaving out the index number to the right of the colon is the same as telling it to use the length of the list
# spam[1:]    # ['bat','rat','elephant']
# spam[:]     # ['cat','bat','rat','elephant']

#############################################

# # Getting a List's Length with len()
#
# spam = ['cat','bat','rat','elephant']
# len(spam)      # 4

#############################################

# # Changing Values in a List with Indexes
#
# spam = ['cat','bat','rat','elephant']
# spam[1] = 'aardvark'
# print(spam)    # spam = ['cat','aardvark','rat','elephant']
#
# spam[2] = spam[1]
# print(spam)    # spam = ['cat','aardvark','aardvark','elephant']
#
# spam[-1] = 12345
# print(spam)    # spam = ['cat','aardvark','aardvark', 12345]

##############################################

# # List Concatenation and List Replication
#
# spam = [1, 2, 3 ]
# eggs = [A, B, C]
#
# spam*3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]
# spam + eggs   # [1, 2, 3, A, B, C]
# spam + [X, Y, Z]   # [1, 2, 3, X, Y, Z]

#################################################

# # Removing Values from Lists wirh DEL Statements
# spam = ['cat','bat','rat','elephant']
# del spam[2]
#
# print(spam)  # ['cat', 'bat', 'elephant']
#
# del spam[2]
# print(spam)  # ['cat', 'bat'}

####################################################

