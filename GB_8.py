
#1

class Data:
    def __init__(self,number):
        self.number = str(number)

    @classmethod
    def S(cls,number = str(input("Введите дату: "))):
        r = list(number.split('-'))
        print('Число:' + r[0])
        print('Месяц:' + r[1])
        print('Год:'+ r[2])
    @staticmethod
    def valid(self,number = str(input("Введите дату: "))):
        r = list(number.split('-'))
        if 0 > int(r[1]) or int(r[1]) > 13:
            print("Месяц введен не корректно")
        else:
            print('Месяц введен корректно')

t = Data("01-01-01")
Data.S() #Через название класса
t.S()    #Через экземпляр класса
Data.valid("01-01-01")


#2

class ErrorExcep(Exception):
    def __init__(self,param):
        self.param = param
param1 = int(input("Введите первое число: "))
# param2 = int(input("Введите второе число: "))
try:
    param2 = int(input("Введите второе число: "))
    if param2 == 0:
        raise ErrorExcep("Вы ввели НОЛЬ")
    print(param1/param2)
except:
    print("Ввели НОЛЬ")
    print(param1)

#3 ОНО РАБОТАЕТ (Я НЕ БЕЗНАДЕЖЕН)

class ErrorExcep(Exception):
    def __init__(self,param):
        self.param = param
data = input('Введите число: ')
numbers = list()
while data != "stop" or " ":
    try:
        if data == "stop":
            break
        elif data.isdigit() is not True:
            raise ErrorExcep("Не число")
        else:
            numbers.append(data)
        data = input('Введите число: ')
    except:
        print("Ввели не число")
        data = input('Введите число: ')
        if data == "stop":
            break

print(numbers)


#4

class warehouse:
    def __init__(self,name, quantity):
        self.name = name
        self.quantity = quantity
        # self.volume = volume
        # self.serial_number = serial_number

    def __str__(self):
        return self.name +" " + self.quantity


class Printer(warehouse):
    def __init__(self, name, quantity,volume):
        super().__init__(name, quantity)
        self.volume = volume

class Scanner(warehouse):
    def __init__(self, name, quantity, serial_number):
        super().__init__(name, quantity)
        self.volume = serial_number
