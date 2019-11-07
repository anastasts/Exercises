'''n = [int(k) for k in input().split()]
n = sorted(n)
n1 = []
c = []
for i in range(len(n)-1):
    if n[i] != n[i+1]:
        if n[i] == n[i-1]:
            n1.append(n[i])
    else:
        n1.append(n[i])
print(n1)
count = 1
for i in range(len(n1)-1):
    if n1[i] == n1[i+1]:
        i += 1
        count += 1
    else:
        print(n[i], 'Count = ', count)
        c.append(count)
        count = 1
print(c)'''
import statistics
n = [int(k) for k in input().split()]
try:
    m = statistics.mode(n)
    print(m)
except:
    print('UNKNOWN')








