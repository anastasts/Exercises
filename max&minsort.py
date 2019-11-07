n = [int(k) for k in input().split()]
for i in range(len(n)):
    max = i
    min = i
    for j in range(i,len(n) - i):
        if n[j] > n[max]:
            max = j
        if n[j] < n[min]:
            min = j
    n[i], n[max] = n[max], n[i]
    n[-1 - i], n[min] = n[min], n[-1 -i]

print(n)




