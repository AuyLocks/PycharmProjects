# #allMyCats1
# # This first example isn't a good way to program because it isn't dynamic, if the number of cats ever changes it can't adjust
#
# print('Enter the name of cat 1:')
# catName1 = input()
# print('Enter the name of cat 2:')
# catName2 = input()
# print('Enter the name of cat 3:')
# catName3 = input()
# print('Enter the name of cat 4:')
# catName4 = input()
# print('Enter the name of cat 5:')
# catName5 = input()
# print('Enter the name of cat 6:')
# catName6 = input()
# print('The cat names are:')
# print(catName1 + ' ' + catName2 + ' ' + catName3 + ' ' + catName4 + ' ' + catName5 + ' ' + catName6)

#######################################

#allMyCats2

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name]  # list concatenation
print('The cat names are: ')
for name in catNames:
    print(' ' + name)