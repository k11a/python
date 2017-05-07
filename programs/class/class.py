#test work with class

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)



class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)
    def __str__(self):
        return str(self.person)

# class Manager(Person):
#     def __init__(self, name, pay):  # Переопределенный конструктор
#         Person.__init__(self, name, 'mgr', pay) # Вызов оригинального
#                                                 # конструктора со значением
#                                                 # 'mgr' в аргументе job
#     def giveRaise(self, percent, bonus=.10):
#         Person.giveRaise(self, percent + bonus)



if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Jones', 50000) # Указывать должность не требуется:
    tom.giveRaise(.10)  # Подразумевается/устанавливается
    print(tom.lastName())  # классом
    print(tom)



class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)
print('----class Department----')
development = Department(bob, sue) # Встраивание объектов в составной объект
development.addMember(tom)
development.giveRaises(.10)  # Вызов метода giveRaise вложенных объектов
development.showAll()  # Вызов метода __str__ вложенных объектов

