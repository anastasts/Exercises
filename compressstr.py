n = input().split()
num = 0
for i in range(len(n)):
    if n[i] != '0':
        print(n[i], end=' ')
    else:
        num += 1
for k in range(num):
    print('0', end=' ')

