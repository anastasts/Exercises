l = [1, 42, None, False, 'Alice']

i = iter(l)
first = next(i) #передвигает по списку на след эл
second = next(i)
third = next(i)
fourth = next(i)
fifth = next(i)
print(first, second, third, fourth, fifth)

for x in l:
    print(x, end=' ')
i = iter(l)
while True:
    try:
        print(next(i))
    except StopIteration:
        break