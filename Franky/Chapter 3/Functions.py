# #helloFunc
# def hello():
#     print('Howdy!')
#     print('Howdy!!!')
#     print('Hello there.')
# hello()
# hello()
# hello()
################################
# #DEF Statements with Parameters
# #helloFunc2
# def hello(name):
#     print('Hello ' + name)
#
# hello('Alice')
# hello('Franky')
###############################
# #Return Values and Return Statements
# #magic8Ball
# import random
# def getAnswer(answerNumber):
#     if answerNumber == 1:
#         return 'It is certain'
#     elif answerNumber == 2:
#         return 'It is decidedly so'
#     elif answerNumber == 3:
#         return 'Yes'
#     elif answerNumber == 4:
#         return 'Reply hazy, try again'
#     elif answerNumber == 5:
#         return 'Ask again later'
#     elif answerNumber == 6:
#         return 'Concentrate and ask again'
#     elif answerNumber == 7:
#         return 'My reply is no'
#     elif answerNumber == 8:
#         return 'Outlook not so good'
#     elif answerNumber == 9:
#         return 'Very doubtful'
#
# r = random.randint(1, 9)
# fortune = getAnswer(r)
# print(fortune)
# #Another way to combine the lines 41 - 43 is print(getAnswer(random.randint(1,9)))
#############################
# #Local and Global Scope
# #
# # #sameName
# # def spam():
# #     eggs = 'spam local'
# #     print(eggs)  #prints 'spam local'
# #
# # def bacon():
# #     eggs = 'bacon local'
# #     print(eggs) #prints 'bacon local'
# #     spam()
# #     print(eggs) #prints 'bacom local'
# #
# # eggs = 'global'
# # bacon()
# # print(eggs)
######################
# #How to modify a global statement within a function
# #sameName2
#
# def spam():
#     global eggs
#     eggs = 'spam'
#
# eggs = 'global'
# spam()
# print(eggs)
#####################
# #sameName3
#
# def spam():
#     global eggs
#     eggs = 'spam'  # this is the global
#
# def bacon():
#     eggs = 'bacon' # this is a local
#
# def ham():
#     print(eggs)  # this is global
#
# eggs = 42 # this is the global
# spam()
# print(eggs)

#######################

# #sameName4
# def spam():
#     print(eggs) # Error, because you are asking for a variable that doesn't exist yet
#     eggs = 'spam local'
#
# eggs = 'global'
# spam()