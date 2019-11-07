s = input()
first = 0
last = 0
k = 0
g = len(s) - 1
for i in range(len(s)):
    if s[i] == 'h':
        first = i + 1
        break
while g != 0:
    if s[g] == 'h':
        last = g
        break
    g -= 1
while k < last:
    print(s[k], end='')
    k += 1
while first < len(s):
    print(s[first], end='')
    first += 1





