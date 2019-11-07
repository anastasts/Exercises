'''data = [1.0/x for x in [3, 2, 1, 0]]
print(data)'''

data = (1.0/x for x in [3, 2, 1, 0])
for x in data:
    print(x)

