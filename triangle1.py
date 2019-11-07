k1 = [float(k) for k in input().split()]
k2 = [float(k) for k in input().split()]
k3 = [float(k) for k in input().split()]
if k1[0] == k2[0]:
    if k1[0] == k3[0]:
        print('No')
    else:
        print('Yes')
else:
    k = (k2[1] - k1[1]) / (k2[0] - k1[0])
    b = (k2[0]*k1[1] - k1[0]*k2[1]) / (k2[0] - k1[0])
    if k*k3[0] + b - k3[1] == 0:
        print("No")
    else:
        print("Yes")
