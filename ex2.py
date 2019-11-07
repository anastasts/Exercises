def print_time(s, n2):
    hour = 0
    for i in range(4):
        hour += s[-i+3] * (2**i)
    min = 0
    for i in range(6):
        min += s[-i+9] * (2**i)
    if hour <= 11 and min <= 59:
        string = [hour, min]
        n2.append(string)

def func(s, l, n, r, n2):
    print('here we go', s, r)
    for i in range(l):
        s[l-1-i] = 1
        if (n==r+1):
            print(s, r)
            print_time(s,n2)
        else:
            print('go deeper',s, r)
            func (s, l-i-1, n, r+1, n2)
        s[l - 1 - i] = 0

n = int(input()) #количество единиц
n1 = [0 for k in range(10)]
n2=[]
func(n1, 10, n, 0, n2)
n2.sort()
if n==0:
    print('0:00')
#print('LEEEEEEEEEEEEEEEEN', len(n2))
for i in range(len(n2)):
    if n2[i][1]<10:
        print( n2[i][0], ':0', n2[i][1], sep='')
    else:
        print(n2[i][0], ':', n2[i][1], sep='')
