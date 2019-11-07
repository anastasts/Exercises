s1 = input()
s2 = input()
flag = 0
if len(s1) == len(s2) and len(s1) > 0:
    for i in range(len(s1)):
        if s1 == s2:
            print(i)
            flag = 1
            break
        s1 = s1[-1] + s1[:-1]
if flag == 0:
    print(-1)

