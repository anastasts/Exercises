a = []
inp = open('input.txt','r')#Открыли файл на чтение
for line in inp:
    friends = set([str(k) for k in line.split()])#Делаем множество
    #print(friends)
    if len(a) == 0:
        a.append(friends)
    else:
        flag = 0
        for i in range(len(a)):
            for person in friends:
                if person in a[i]:
                    a[i] = a[i].union(friends)
                    flag = 1
                    break
        if flag == 0:
            a.append(friends)
flag = 0
for i in range(len(a)):
    if 'Алиса' in a[i]:
        for j in range(len(a)):
            for person in a[i]:
                if person != 'Алиса' and person in a[j] and 'Боб' in a[j]:
                    print('YES')
                    flag = 1
                    break
    if flag == 1:
        break
#print(a)
if flag == 0:
    print('NO')

