#
# def get_sum(a, b):
#     # good luck!
#     totalList = []
#     if a < b:
#         i = a
#         while i < b:
#             totalList.append(i)
#             i += 1
#         totalSum = sum(totalList)
#
#     elif b < a:
#         i = b
#         while i < a:
#             totalList.append(i)
#             i += 1
#         totalSum = sum(totalList)
#     elif a == b:
#         totalSum = a
#
#     return totalSum

# def accum(s):
#     # your code
#     i = 0
#     weird = ''
#     while i < len(s):
#         weird += str(s[i].upper)
#         for i in range (1 , len(s)):
#             weird += str(i*s[i].lower())
#         for i in range (1 , len(s)-1):
#             weird += '-'
#     return weird
# accum('later')

a = [1,2,2,2,2]
b =[2]
i = 0
newArray = []
while i < len(a):
    if a[i] != b:
        newArray.append(a[i])
    i += 1

print(newArray)
