arr = [1]
lvl = 10
for k in range(lvl): #глубина
    print(' '*(lvl-k), end='')
    for i in range(len(arr)):
        s=3
        t=arr[i]
        while t>0:
            s-=1
            t//=10
            #print('lol',t)
        print(' '*s,arr[i], end=' ')
    print()
    arr1 = [arr[0]]
    for i in range(len(arr) - 1):
        arr1.append(arr[i] + arr[i + 1])
    arr1.append(arr[-1])
    arr = arr1
