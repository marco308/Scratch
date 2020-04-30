


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
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay) #creates the new employee 
        


  
emp_1 = Employee('marcus', 'williams', 1000)
emp_2 = Employee('Test', 'User', 20000)

# 
# 

new_emp_1 = 'James-Smith-200'

emp_3 = Employee.from_string(new_emp_1)

print(Employee.num_of_emps)





 