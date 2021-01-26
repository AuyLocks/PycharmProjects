r = -20
g = 253
b = 252

rgb = [r,g,b]
abc = ('A','B','C','D','E','F')
hex = ''

for index,item in enumerate(rgb):
    x = divmod(item, 16)
    if item > 255:
        hex += 'FF'
    else:
        for i in range(len(x)):
            if x[i] >= 15:
                hex += 'F'
            elif x[i] <= 9:
                hex += str(x[i])
            elif x[i] >= 10:
                hex += abc[x[i]%10]

print(hex)