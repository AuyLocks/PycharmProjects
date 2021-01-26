import copy
spam = ['A', 'B', 'C', 'D']
print(id(spam))   # 140483415480008
cheese = copy.copy(spam)
cheese[1] = 42
print(cheese)       # ['A', 42, 'C', 'D']
print(id(cheese))    # 140483415080200