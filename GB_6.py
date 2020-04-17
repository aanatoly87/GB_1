
#1 Не решил с последовательностью.

class TrafficLight:
    print("Светофор работает")
    def __init__(self, color, time):
        self._color = color
        self.__time = time
    def running (self):
        print(self._color + " горит " + str(self._TrafficLight__time) + " секунд")

light = TrafficLight("Крассный", 7)
light_2  = TrafficLight("Желтый", 2)
light_3  = TrafficLight("Зеленый", 10)
print("************Режимы работы*******************")
print(light._color, light._TrafficLight__time)
print(light_2._color, light_2._TrafficLight__time)
print(light_3._color, light_3._TrafficLight__time)
print("**************************")
light.running()
light_2.running()
light_3.running()


#2

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width
        print("Длина дороги: " + str(lenght),"Ширина дороги: " + str(width))
    def summma (self, lenght, width, mass, thickness):
        s = print("Масса асфальты в кг: " + str((self._lenght*self._width*mass*thickness)/1000))
print("***Масса асфальта для дороги*** ")
road_1 = Road(20,5000)
road_1.summma(20, 5000, 25, 5)

#3 Не могу связать со словарем

class Worker:
    def __init__(self, name, surname, position,income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income
        print(self.name + " " + self.surname +" зарабатывает " + str(self.income))
class Position (Worker):
    def get_full_name(self, name, surname):
        self.full_name = name + "" + surname
        print("Полное имя сотрудника: " + name + " " + surname)
#

petrov = Position("Ivan", "Petrov","worker", 1000)
petrov.get_full_name("Ivan", "Petrov")


#4 Прога работает


class Car:
    # _ispolice = None
    def __init__(self, speed,color, name,goodornot):
        self.speed = speed
        self.color = color
        self.name = name
        self._ispolice = goodornot

    def setisgood(self,goodornot):
        self._ispolice = goodornot
    def go(self,name, moving):
        print("Машина повернула/едет прямо" + moving)
    def showspeed(self,speed,name):
        self.speed = speed
        self.name = name
        if name == "towncar" and speed > 60:
            print("Скорость превышена")
        elif name == "workcar" and speed > 40:
            print("Скорость превышена")

class TownCar(Car):
    pass
class SportCar(Car):
    pass
class WorkCar(Car):
    pass
class PoliceCar(Car):
    pass


towncar = Car (100,"red","lambargini",bool)
workcar = Car (200,"Green","TopWork",bool)
towncar.showspeed(100,"towncar")
workcar.showspeed(200,"workcar")



#5



class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")
class Pen(Stationery):
    def draw(self):
        print("Отрисовка ручкой")
class Pencil(Stationery):
    def draw (self):
        print("Отрисовка грифилем")
class Handle(Stationery):
    def draw(self):
        print("Отрисовка маркером")




pencil = Stationery("Ручка")
pencil.draw()
pen = Handle('Карандаш')
pen.draw()

