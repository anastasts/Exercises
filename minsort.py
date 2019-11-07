n = [int(k) for k in input().split()]
for i in range(len(n)):
    ind = i
    for j in range(i, len(n)):
        if n[j] < n[ind]:
            ind = j
        n[i], n[ind] = n[ind], n[i]
print(n)