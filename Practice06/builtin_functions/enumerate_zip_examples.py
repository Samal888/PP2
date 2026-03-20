names = ["A", "B"]
scores = [90, 80]

for i, name in enumerate(names):
    print(i, name)

for n, s in zip(names, scores):
    print(n, s)