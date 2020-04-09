#1

def div(A,B):
    while B == 0:
        B = int(input("Число B еще раз: "))
    C = A/B
    return C

A2 = int(input("Число А: "))
B2 = int(input("Число B: "))
div2 = div(A2,B2)
print(div2)



#2

def datafunc(**kwargs):
    result = " *** ".join(str(key)+ ": " + str(value) for key,value in kwargs.items())
    print(result)
a = input("Введите имя: ")
b = input("Введите фамилию: ")
c = int(input("Введите возраст: "))
d = input("Введите город проживания: ")
i = input("Введите email: ")

datafunc(Name = a, Surname = b, Age = c, City = d, Email = i)


#3 Написал как ребенок, но работает)

def summa(x,y,z):
    A = [x,y,z]
    for i in A:
        A.sort(reverse=True)
    del A[2]
    sum = A[0]+A[1]
    print("Сумма двух больших чисел равна: " + str(sum))

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

summa(num1,num2,num3)

#4_1

def my_func(x,y):
    num = 1/(x**abs(y))
    print(num)

num1 = int(input("Введите число: "))
num2 = int(input("Введите степень числа: "))

my_func(num1,num2)

#4_2

def my_func(x,y):
    num = 1
    i = 1
    while i != abs(y)+1:
        num = num*1/x
        i+=1
    print(num)

num1 = int(input("Введите число: "))
num2 = int(input("Введите степень числа: "))

my_func(num1,num2)



#6

def int_func(a):
    print(a.title())

a = str(input("Введите слово: "))
int_func(a)
b = str(input("Введите несколько слов: "))
int_func(b)

