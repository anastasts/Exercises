s = input()
flag = 0
for i in range(len(s)):
    if (s[i] not in s[i+1:]) and (s[i] not in s[:i]):
        print(i)
        flag = 1
        break
if flag == 0:
    print("NOTFOUND")