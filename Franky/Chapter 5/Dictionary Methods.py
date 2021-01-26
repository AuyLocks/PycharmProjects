
# The keys(), values(), and items() Methods

spam = {'color': 'red', 'age': '42'}
for v in spam.values():
    print(v)
    # returns red, 42
print('\n')


for k in spam.keys():
    print(k)
    # returns color, age

print('\n')

for i in spam.items():
    print(i)
    # returns ('color', 'red'), ('age', '42')