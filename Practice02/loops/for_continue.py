#1: skip 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#2: skip even
for j in range(1, 5):
    if j % 2 == 0:
        continue
    print(j)

#3: skip 4
for k in range(1, 6):
    if k == 4:
        continue
    print(k)

#4: skip 2 and 5
for n in range(1, 7):
    if n == 2 or n == 5:
        continue
    print(n)

#5: skip not 3
for x in range(1, 6):
    if x != 3:
        print(x)
