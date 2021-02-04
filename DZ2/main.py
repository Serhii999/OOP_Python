class Employee(object):
    name = ''
    mail = ''
    daily_pay =0

    def work (self):

        return "{} come to the office" .format(self.name)

    def check_salary(self, days):
        return "Zarabotok za {} dney = {}".format(days, days*self.daily_pay)



class Recruiter(Employee):
    def work(self):
        return "{} come to the office and start to hiring ".format(self.name)

    def __str__(self):
        return ("{}: {}".format(self.name, self.__class__.__name__))


class Programmer(Employee):

    def work(self):
        return "{} come to the office and start coding".format(self.name)

    def __str__(self):
        return ("{}: {}".format(self.name, self.__class__.__name__))

Anya =Recruiter()
Anya.name = 'Anya'
Anya.mail = 'anna@gmail.com'
Anya.daily_pay = 30

Slava =Employee()
Slava.name = 'Vyacheslav'
Slava.mail = 'slavik@gmail.com'
Slava.daily_pay = 20

Sveta =Employee()
Sveta.name = 'Svetlana'
Sveta.mail = 'svetlana@gmail.com'
Sveta.daily_pay = 15

Dima =Recruiter()
Dima.name = 'Dmitriy'
Dima.mail = 'dimon@gmail.com'
Dima.daily_pay = 35

Serhii =Programmer()
Serhii.name = 'Serhii'
Serhii.mail = 'seriy@gmail.com'
Serhii.daily_pay = 40

print(Anya.__str__())
print(Anya.check_salary(25),'\n')

print(Serhii.work(),'\n',  Serhii.check_salary(30), '\n')
print(str(Serhii))
print(str(Anya))