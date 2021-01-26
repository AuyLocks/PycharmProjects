people = [25, 25 ,50]
cash = 0
for index, item in enumerate(people):
    if item == 25:
        cash += item
    else:
        print(cash)
        print('Can not sell you a ticket')

