s = [int(k) for k in input().split()]
for k in range(min(s), max(s)):
    if k not in s:
        print(k, end=' ')