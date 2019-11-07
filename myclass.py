class MyList:
    def __init__(self, elements=[]): #Передаем элементы
        self.__list = elements.copy()
        if 'Chuck' in self.__list:
            self.__list.remove('Chuck')

    #Перегрузка операторов "+"
    def __add__(self, other):
        return MyList(self.__list + other.__list)

    def __str__(self):
        return '[[' + ', '.join(self.__list + ['Chuck']) + ']]'

    def __iter__(self): #чтобы использовать фор для вывода поэлементно
         return iter(self.__list + ['Chuck'])

    def __len__(self):
        return len(self.__list) + 1

    def __getitem__(self, item):



list1 = MyList(['Alice', 'Bob']) #если добавим чака то он будет всегда в конце и будет всегда один
list2 = MyList(['Carol'])
merged_list = list1 + list2
print(merged_list._MyList__list) #Обращаемся к скрытому полю из этого списка
print(merged_list)
for x in merged_list:
    print(x)

print(len(merged_list))