
AL = set()#Создали пустое множество
BB = set()
inp = open('input.txt','r')#Открыли файл на чтение
for line in inp:#Перебираем строчки в файле по очереди по одной
    friends = set([str(k) for k in line.split()])#Делаем множество
    if 'Алиса' in friends :
        AL = AL.union(friends)
    if 'Боб' in friends:
        BB = BB.union(friends)
if 'Алиса' in AL:
    AL.remove('Алиса')
if 'Боб' in BB:
    BB.remove('Боб')
if len(AL.intersection(BB)) > 0:
    print('YES')
else:
    print('NO')
inp.close()


