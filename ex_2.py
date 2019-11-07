inp = open('input.txt','r')#Открыли файл на чтение
l = [line.strip() for line in inp]
l = sorted(l, key=len)
inp.close()
out = open('output.txt','w')
for line in l:
    out.write(line+'\n')
out.close()

