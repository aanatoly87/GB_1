#1
A = []
N = int(input("Введите количество переменных: "))
for i in range(N):
    a = input()
    A.append(a)
print(A)


#2
seconds =int(input('Введите количество секунд: '))
hour = seconds//3600
minute = (seconds%3600)//60
second = (seconds%3600)%60
print(str(hour).rjust(4,"0"),':',str(minute).rjust(4,"0"),':',str(second).rjust(4,"0"))

#3
N = int(input('Введите число: '))
c = 3
sum = 0
i = 1
while i <= c:
    n = str(N)*i
    i = i+1
    sum = sum + int(n)
print(sum)

#4
N = int(input("Введите число: "))
A =[]
L = len(str(N))
i = 0
while N:
    n = N%10
    A.append(n)
    N = N//10
print (A)
print(max(A))

#5
receipt = int(input("Значение выручки: "))
cost = int(input("Значение издержек: "))
people = int(input("Количество работников: "))
if cost > receipt:
    print("Финрез отрицательный")
elif cost == receipt:
    print("Точка безубыточности")
else:
    print("Работаем хорошо")
    profit = receipt - cost
    rent = profit/receipt*100
    perEmployee = profit/people
    print("Рентабельность компании {} %".format(rent))
    print("Прибыль на одного сотрудника {} рублей ".format(perEmployee))

#6
a = float(input("Количество км в первый день: "))
b = float(input("Сколько должен пробежать: "))
i = 1
while a<=b:
    a=a*1.1
    i = i + 1
print("На {} день пробежит не менее {} км".format(i,b))