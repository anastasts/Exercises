n = [int(k) for k in input().split()]
count = 1
for i in range(len(n)-1):
    if n[i] != n[i + 1]:
        count += 1
print(count)
