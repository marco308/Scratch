
# https://www.youtube.com/watch?v=jCzT9XFZ5bw
# Tutorial 6: Property Decorators - Getters, Setters, and Deleters
# above has not be show here

class Employee:
    # class variable
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first 
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@perdy.com' 
 
        Employee.num_of_emps += 1 

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    # let you create this class by passing a string 
    # 'constructor' normally start with from_
    # e.g.
    # new_emp_1 = 'James-Smith-200'
    # emp_3 = Employee.from_string(new_emp_1)
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay) #creates the new employee 

    # import datetime
    # my_date = datetime.date(2016,7,10)
    # print(Employee.is_workday(my_date))
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True 

    #####################
    # specail methods 
    #####################
    # return a string that you can use to recreate the object 
    # emp_1 = Employee('marcus', 'williams', 1000)
    # without __repr__ then print(emp_1) gives:: <__main__.Employee object at 0x10b2b1100>
    # with __repr__ then print(emp_1) gives:: Employee('marcus', 'williams', '1000')
    # designed for the devloper not the end user to look at
    def __repr__(self):
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    # desinged to be helpful to the end user
    # emp_1 = Employee('marcus', 'williams', 1000) 
    # print(emp_1) gives:: marcus - williams
    def __str__(self):
        return "{} - {}".format(self.first, self.last)


#####################
# subclasses  
#####################
# inherits all of the func from Employee parent class 
class developer(Employee):
    raise_amt = 1.1 #over write the raise_amt inhet from Employee

    def __init__(self, first, last, pay, program_lag):
        super().__init__(first,last,pay) #let parent class 'Employee' handle creating the first,last,pay
        self.program_lag = program_lag   








#####################
#####################
#####################

#####################
#####################
#####################

  
emp_1 = Employee('marcus', 'williams', 1000)
emp_2 = Employee('Test', 'User', 20000)



new_emp_1 = 'James-Smith-200'

emp_3 = Employee.from_string(new_emp_1)

print(Employee.num_of_emps)
 
dev1 = developer('dev', 'user', 5000, 'phyton')

print(dev1.first)
print(dev1.program_lag)
print(Employee.num_of_emps)
print(dev1.num_of_emps)

  
print(emp_1)