n = int(input())
if n <= 100:
    A = []
    for i in range(n):
        A.append([0]*n)
    for i in range(n):
        A[i][n-i-1] = 1
        for j in range(n-i, n): #для j проверяем условие, что j<n+i
            A[i][j] = 2
    for row in A:
        for elem in row:
            print(elem, end=' ')
        print()



