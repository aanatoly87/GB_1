

#1 
# class Matrix:
#     def matrix(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2
#         self.matr = []
#         print(f"Матрица {param1} на {param2}")
#     def add (self, *args):
#         self.mylist = []
#         for el in args:
#             self.mylist.append(el)
#         self.matr.append(self.mylist)
#     def __str__(self):
#         for i in self.matr:
#             return (f'Матрица через STR = {str(self.matr)}')
#     def __del__(self):
#         print(f'Матрица через DEL = {self.matr}')
#
# matrix1 = Matrix()
# matrix1.matrix(2,2)
# matrix1.add(5,6)
# matrix1.add(10,12)
# print(matrix1)
#
# matrix2 = Matrix()
# matrix2.matrix(2,2)
# matrix2.add(34,35)
# matrix2.add(45,49)
# print(matrix2)

#2

# class Goods:
#     def __init__(self,size, height):
#         self.size = size
#         self.height = height
#         print(self.size)
#         print(self.height)
#     @property
#     def goods(self):
#         coat = (self.size / 6.5 + 0.5)
#         suit = (2*self.height + 0.3)
#         sum = coat + suit
#         print(coat)
#         print(suit)
#         print(sum)
#
# material = Goods(6.5,1)
# sum = material.goods


#3

# class Cellular:
#     def __init__(self,size_cell):
#         self.size_cell = size_cell
#         print(f'Количество ячеек в клетке {self.size_cell} штук')
#     def __add__(self, other):
#         return Cellular(self.size_cell + other.size_cell)
#     def __sub__(self, other):
#         if self.size_cell > other.size_cell:
#             return Cellular(self.size_cell - other.size_cell)
#         else:
#             print('Incorrect, ошибочкА')
#     def __mul__(self, other):
#         return Cellular (self.size_cell * other.size_cell)
#     def __truediv__(self, other):
#         return Cellular(self.size_cell // other.size_cell)
#     def make_order (self,*args):
#         print('Введите количество ячеек в клетках через запятую')
#         self.sum = []
#         self.size_cell = args
#         for el in args:
#             self.sum.append(el)
#         print(self.sum)
#         self.sum.sort()
#         for i in self.sum:
#             print(f'****\n****{i}\n***')
# kletka1 = Cellular(87)
# kletka2 = Cellular(67)
# kletka2.make_order(12,34,23,78)
#
# kletka3 = kletka1 + kletka2
# kletka4 = kletka1 - kletka2
# kletka5 = kletka1 * kletka2
# kletka6 = kletka1 / kletka2

