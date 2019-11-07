s = map(int, input().split())
s1 = []
for k in s:
    if k % 2 != 0:
        s1.append(k)
if not s1:
    print('0')
else:
    print(min(s1))









