#1

from sys import argv

param1, param2, param3 = argv

print("Выработка в часах: ", param1)
print("Ставка: ", param2)
print("Премия: ", param3)

salary = (param1*param2) + param3

print("Заработная плата сотрудника: ", salary)


#2_1

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = list()
for i in range(1,len(old_list)):
    if old_list[i] > old_list[i-1]:
        new_list.append(old_list[i])
print(new_list)

#2_2

old_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = list(old_list[i]  for i in range(1,len(old_list)) if old_list[i] > old_list[i-1])

print(new_list)


#3


mylist = [elem for elem in range(20, 241) if elem%20 ==0 or elem%21 ==0]
print(mylist)


#4 НЕ ОЧЕНЬ РЕШЕНА (НЕ СМОГ УДАЛИТЬ ДУБЛИУЮЩИЕ ЭЛЕМЕНТЫ ПОЛНОСТЬЮ)


old_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_list = list(dict.fromkeys(old_list))
print(new_list)

#5

from functools import reduce
mylist = [elem for elem in range(100, 1001) if elem%2 ==0]
print(mylist)
sum = reduce(lambda x, y: x + y, mylist)
print(sum)

#6_1

from itertools import count
for i in count(3,1):
    if i > 10:
        break
    else:
        print(i)

#6_2

from itertools import cycle
GB = []
count = 1
for i in cycle("GeekBrains "):
    if i ==" ":
        break
    else:
        GB.append(i)
print("".join(GB) + " ЧМОКИ")

#7

def factor(c):
    sum = 1
    for i in range(1,c+1):
        sum = sum*i
        i +=i
        yield sum

n = int(input('Введите число: '))
gener = factor(n) #Генератор

for el in gener:
    print(el, end=" # ")
