# class Person():
#     def __init__(self, name, age, tz):
#         self.name = name
#         self.age = age
#         self.tz = tz
#
#     def drink_water(self):
#         print('{} drank water'.format(self.name))
#
#     def eat(self):
#         print('Bon appetit')
#
# class Diploma(Person):
#     def __init__(self, degree, year, name, age, tz):
#         self.degree = degree
#         self.year = year
#         Person.__init__(self, name, age, tz)
#
#     def congratulations(self):
#         print('{} just earned a new diploma in {}'.format(self.name, self.degree))
#
# new_diploma = Diploma(degree='Doctor', name="David", year=2018, age=27, tz=342439522)
#
# new_diploma.eat()

class Person():
    def __init__(self, name, age, tz):
        self.name = name
        self.age = age
        self.tz = tz


class Employee(Person):
    def __init__(self, name, age, tz, emp_number, job):
        self.job = job
        self.emp_number = emp_number
        Person.__init__(self, name, age, tz)

    def promotion(self):
        print('you got a promotion')

class Boss(Employee):
    def __init__(self, name, age, tz, emp_number, job, salary):
        self.salary = salary
        super().__init__(name, age, tz, emp_number, job)

    def hire_new_employee(self):
        new_employee = Employee(name='jqsklf', age=22, tz=2434213413, emp_number=30984322, job='developer')
        new_employee.promotion()


new_boss = Boss(name='david', age=24, tz=389789343, emp_number=75857969, job='developer', salary=220482)
new_boss.promotion()