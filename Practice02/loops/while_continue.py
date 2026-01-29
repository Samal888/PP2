#1: skip 3
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

#2: skip even
j = 0
while j < 4:
    j += 1
    if j % 2 == 0:
        continue
    print(j)

#3: skip 4
k = 1
while k <= 5:
    k += 1
    if k == 4:
        continue
    print(k)

#4: skip 2 and 5
n = 0
while n < 6:
    n += 1
    if n == 2 or n == 5:
        continue
    print(n)

#5: skip not 3
x = 0
while x < 5:
    x += 1
    if x != 3:
        print(x)
