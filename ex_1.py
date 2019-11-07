n = int(input())
if n in range(1000, 9999):
    n = str(n)
    print(n[0]+n[3]+n[2]+n[1])
if n in range(10000, 99999):
    n = str(n)
    print(n[0]+n[1]+n[4]+n[3]+n[2])