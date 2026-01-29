# if_elif_else.py

#1: x >10, >5 or <=5
x = 7
if x > 10:
    print(">10")
elif x > 5:
    print(">5")
else:
    print("<=5")

#2: y >10, >5 or <=5
y = 3
if y > 10:
    print(">10")
elif y > 5:
    print(">5")
else:
    print("<=5")

#3: z <5, ==10, else
z = 10
if z < 5:
    print("<5")
elif z == 10:
    print("==10")
else:
    print("other")

#4: positive, negative, zero
a = 0
if a > 0:
    print("positive")
elif a < 0:
    print("negative")
else:
    print("zero")

#5: <10, <20, else
b = 15
if b < 10:
    print("<10")
elif b < 20:
    print("<20")
else:
    print(">=20")
