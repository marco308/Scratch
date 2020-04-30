


class Employee:
    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@perdy.com' 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)





emp_1 = Employee('marcus', 'williams', 1)
emp_2 = Employee('Test', 'User', 2)

print(emp_1.pay)

print(emp_1.fullname())

         



 