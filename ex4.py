n = int(input())
sum = 0
for k in range(1,n//2 + 1):
    if n % k == 0:
        sum += k
if sum == n:
    print("YES")
else:
    print("NO")