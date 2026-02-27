# 1
def squares_up_to_n(n):
    for i in range(n + 1):
        yield i * i
# 2
def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i
# 3
def divisible_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i
# 4
def squares_range(a, b):
    for i in range(a, b + 1):
        yield i * i
# 5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter n: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))

print("\n1) Squares up to n:")
for x in squares_up_to_n(n):
    print(x)

print("\n2) Even numbers (comma separated):")
print(",".join(str(x) for x in even_numbers(n)))

print("\n3) Divisible by 3 and 4:")
for x in divisible_by_3_and_4(n):
    print(x)

print("\n4) Squares from a to b:")
for x in squares_range(a, b):
    print(x)

print("\n5) Countdown from n to 0:")
for x in countdown(n):
    print(x)