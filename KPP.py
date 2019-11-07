n = int(input())
count = 0
summ = 0
s = 0
while n > 0:
    n -= 1
    print("What is your name?How old are you?", end='')
    name = input()
    old = int(input())
    if old < 18:
        print('NO')
    else:
        print('YES')
        if count == 0:
            min_age = old
            max_age = old
        else:
            if old < min_age:
                min_age = old
            if old > max_age:
                max_age = old
        count += 1
        s += len(name)
        summ += old
print("Passed:", count)
if count > 0:
    print("Minimal age:", min_age)
    print("Maximal age:", max_age)
    print("Average age:", summ // count)
    print("Average name length:", s / count)


