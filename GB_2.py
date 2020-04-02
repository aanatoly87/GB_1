# 1
A = ["b", 23, 23.1, [12, 15], {'erf'}, None, True]
for i in range(len(A)):
       print(A[i], type(A[i]))
# 2
A = list(map(int,input('Введите число: ').split()))
print(A)
if len(A)%2 == 0:
    A[::2],A[1::2] = A[1::2],A[::2]
    print(A)
else:
    b = A.pop()
    A[::2], A[1::2] = A[1::2], A[::2]
    A.append(b)
    print(A)

#3_1
m = int(input("Введите номер месяца от 1 до 12: "))
if m <=2:
    print("Зима")
if 2< m <=5:
    print("Весна")
if 5< m <=8:
    print("Лето")
if 8 < m <= 12:
    print("Осень")

# 3_2

m = 4
TimeOfYear = dict()
for i in range(m):
    month = input('Введите название времени года и номера месяцев года соответствующих времени года: ').split()
    for N in month[1:]:
        TimeOfYear[N] = month[0]
print(TimeOfYear)
N = input("Введите номер месяца: ")
print(TimeOfYear.get(N))

# 4


A = list(input('Введите слова через пробел: ').split())
print(A)
for i,j in enumerate(A,1):
    print('{}. {}'.format(i,j[:10:]))

# 5

A = list(map(int, input("Введите числа через пробел: ").split()))
A.append(int(input("Введите новый элемент списка: ")))
A.sort(reverse=True)
print(A)






