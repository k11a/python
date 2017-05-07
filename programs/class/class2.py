# import random
# import string
# x=1
# l=[]
# while x<1000000:
#     x += 1
#     l.append(' '.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for c in range(512)))
#     if x % 10000 == 0:
#         print (x,end='\n')
#         print (l[-1],end='\n')
# print()
# x=1
# input()
# while x<100:
#     x += 1
#     print (x,end='\n')
#     if 'adsgkfbadsjfka' in l: pass





# #test work with class
#
# class FirstClass:
#     def setdata(self, value):
#         self.data = value
#     def display(self):
#         print(self.data)
#
# class SecondClass(FirstClass):# Наследует setdata
#     def display(self):# Изменяет display
#         print('Current value = “%s”' % self.data)
#
# class ThirdClass(SecondClass):# Наследует SecondClass
#     def __init__(self, value):# Вызывается из ThirdClass(value)
#         self.data = value
#     def __add__(self, other):# Для выражения “self + other”
#         return ThirdClass(self.data + str(other))
#     def __str__(self):# Вызывается из print(self), str()
#         return '[ThirdClass: %s]' % self.data
#     def mul(self, other):
#         self.data *= other
#
# while True:
#     pass
#     break
#
# a = ThirdClass('abc')
# a.display()
# print(a)
# b = (a + 'xyz') + 'rst'
# b.display()
# print('b', b)
# a.mul(3)
# a.display()
# print(a)
# print(list(SecondClass.__dict__.keys()))
# print(list(ThirdClass.__dict__.keys()))
# print(__name__)






# # manynames.py
# X = 11  # Глобальное (в модуле) имя/атрибут (X, или manynames.X)
# A=0
# def f():
#     print(X)  # Обращение к глобальному имени X (11)
# def g():
#     global A
#     X = 22  # Локальная (в функции) переменная (X, скрывает имя X в модуле)
#     print(X)
#     print('A=', A)
#     def h():
#         global A
#         nonlocal X
#         print(X,'- h()')
#         print(A,'- h()')
#         X+=1
#         print(X,'- h()')
#         def i():
#             global A
#             A+=1
#             print(X,'- i()')
#             print(A,'- i()')
#         i()
#     h()
# class C:
#     X = 33  # Атрибут класса (C.X)
#     def m(self):
#         X = 44  # Локальная переменная в методе (X)
#         self.X = 55 # Атрибут экземпляра (instance.X)
#
# if __name__ == '__main__':
#     print('11: модуль (за пределами файла manynames.X)',end=':   ')
#     print(X)  # 11: модуль (за пределами файла manynames.X)
#     print('11: глобальная',end=':   ')
#     f()  # 11: глобальная
#     print('22: локальная',end=':   ')
#     g()  # 22: локальная
#     A=1
#     g()
#     print('11: переменная модуля не изменилась',end=':   ')
#     print(X)     # 11: переменная модуля не изменилась
#     print('Создать экземпляр')
#     obj = C()  # Создать экземпляр
#     print('переменная класса, унаследованная экземпляром',end=':   ')
#     print(obj.X) # 33: переменная класса, унаследованная экземпляром
#     print('Присоединить атрибут X к экземпляру')
#     obj.m()  # Присоединить атрибут X к экземпляру
#     print('55: экземпляр',end=':   ')
#     print(obj.X)    # 55: экземпляр
#     print('33: класс (она же obj.X, если в экземпляре нет X)',end=':   ')
#     print(C.X)    # 33: класс (она же obj.X, если в экземпляре нет X)
#     #print(C.m.X)  # ОШИБКА: видима только в методе
#     #print(g.X)  # ОШИБКА: видима только в функции





import sys
from time import sleep
instream = open('class2.py')
outstream = sys.stdout
data = True
while data:
    data = instream.read(1)
    if data != '\n': data = chr(ord(data)+7)
    outstream.write(data)
    sleep(0.01)
else:
    instream.close()
