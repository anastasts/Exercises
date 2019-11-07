def add_1(list, el): #добавляет по одному элементу
    for elem in el:
        list.append(elem)

def add_2 (list, el): #склеивает
    list.extend(el)

def add_3 (list, *el): #из аргементов делает и массив и добавляет, не могу менять
    for elem in el:
        list.append(elem)

def add_4 (list, **el): #kt
    for el1, el2 in el.items():
        list.append(el2)

def add_5 (list, el):
    for el1, el2 in el.items():
        list.append(el2)

first = [1,2,3,4,5]
print(first)
add_1(first,[6,7])
print(first)
add_2(first,[8,9])
print(first)
add_3(first,10,11)
print(first)
add_4(first,a=12,b=13)
print(first)
add_5(first,{'a' : 14,'b' : 15})
print(first)