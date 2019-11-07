n = int(input())
if n <= 1000:
    if n % 2 == 0:
        n += 2
        print(n)
    else:
        n += 1
        print(n)
else:
    print('Error')
