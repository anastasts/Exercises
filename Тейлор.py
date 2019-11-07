from math import sin

eps = float(input())
x = float(input())
sl = x
sum = x
i = 0
while sl < eps:
    i += 1
    sl *= ((-1)*x*x)/((i*2)*(i*2+1))
    sum += sl
print(sum)
print(sin(x))