from functools import reduce
l1 = [2,5,7,9,17,19,1.2]

c= list(map(lambda x: str(x)[0] == "1", l1))
print(c) 