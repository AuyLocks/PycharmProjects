#Error Handling

##########################

# #zeroDivide, will give out error "division by zero"
# def spam(divideBy):
#     return 42 / divideBy
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

############################

# #Using 'except' and 'try' to handle error codes
# def spam(divideBy):
#     try:
#         return 42 / divideBy
#     except ZeroDivisionError:
#         print('Error: Invalid argument.')
#
# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

##############################

# #the print(spam(1)) will not execute because once the code jumps to except it will not go back to try
# def spam(divideBy):
#     return 42 / divideBy
# try:
#     print(spam(2))
#     print(spam(12))
#     print(spam(0))
#     print(spam(1))
# except ZeroDivisionError:
#     print('Error: Invalid argument.')

###############################
