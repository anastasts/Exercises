k = int(input()) #вместимость
m = int(input())
n = int(input()) #сколько нужно пожарить
if k >= n:
    print(2*m)
elif n*2 % k == 0:
  r = m*(n*2 // k)
  print(r)
else:
  r = m*(1+(n*2 // k))
  print(r)
