s = str(input())
flag = 1 #flag=0 значит не полиндром
l = len(s)
for i in range(l//2): #доходим до половины строки
    if s[i] == s[l-i-1]:
        continue
    else:
        flag = 0
        break
if flag > 0:
    print('YES')
    exit(0)
flag = 1
for i in range(l):
    if l % 2 != 0 and i == l//2: #строка нечетная и элемент посередине
        continue
    if i < l/2:
        h = 0 #flag one more
        j = 0
        while j < (l+h)//2:
            if j == i:
                j += 1
                h = 1
            if s[j] == s[l-j+h-1]:
                flag += 1
            else:
                flag = 0
                break
            j+=1
    else:
        j = l - 1
        h = 0
        while j >= (l-h)//2:
            if j == i:
                j -= 1
                h = -1
            if s[j] == s[l-j+h-1]:
                flag += 1
            else:
                flag = 0
                break
            j -= 1
    if flag > 0:
        print('YES')
        exit(0)
if flag > 0:
    print('YES')
else:
    print('NO')




