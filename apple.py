print('Enter the number of people:')
n = int(input())
print('Enter the amount of apple:')
k = int(input())
if (n <= 0 or k <= 0) or (n > 1000 or k > 1000):
    print('Error')
    exit(0)
else:
    if n == k: #если кол-во яблок совпадает с кол-во студентами
        print('Everyone has ' + str(n // k) + ' apple')
    elif n > k:
        print('You cant give apple')
    elif n < k:
        print('Everyone has ' + str(k // n) + ' apple')
    else:
        print('Error')