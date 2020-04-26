import datetime


class Employee():

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    # Pueden ser llamados directamente sin necesidad de haber creado el objeto
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # Llamadas directas que no tenga mucha realcion con la instancia del objeto
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Shafter', 500)
emp_2 = Employee('Test', 'Employee', 600)

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
