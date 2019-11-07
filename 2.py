import math

N = int(input())
for i in range(1, math.floor(N**0.5)+1): #floor-округление вниз,  ceil;
    print(i*i, end=' ')



