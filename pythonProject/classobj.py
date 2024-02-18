class Employees:
    raise_amt = 1.04
    def __init__(self,first_name,last_name,pay):
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + 'doncalebm@gamil.com'
    def full_name(self):
            return '{} {}'.format(self.first_name, self.last_name)
    def apply_raise(self):
            self.pay = int(self.pay * self.raise_amt)
    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount
class Developer(Employees):
    def __init__(self,first_name,last_name,pay,language):
        super().__init__(first_name,last_name,pay)
        self.language = language
class Watchman(Employees):
    def __init__(self,first_name,last_name,pay,Gender):
        super().__init__(first_name,last_name,pay)
        self.Gender = Gender
emp1 = Employees("Don", "Marocho", 20000)
emp2 = Employees("Teddy", "Kamau", 50000)
print(emp1.first_name)
print(emp2.first_name)
print(emp1.email)
print(emp2.email)
print(f"{emp1.first_name} {emp1.last_name}salary is {emp1.pay}")
print(f"{emp2.first_name} {emp2.last_name}salary is {emp2.pay}")
print(emp1.full_name())
print(emp2.full_name())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
emp2.apply_raise()
print(emp2.pay)
Employees.raise_amt =2.05
print(Employees.raise_amt)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
Employees.set_raise_amt =(1.05)
print(Employees.raise_amt)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
dev1 = Developer("John", "Smith", 20000,"python")
dev2 = Developer("Esther","Kinuthia",20000,"c++")
print(dev1.language)
print(dev2.language)

class Colors:
    def get_color(self):
        return "color not specified"



class Red(Colors):
    def get_color(self):
        return "red"
class Blue(Colors):
    def get_color(self):
        return "blue"
red_object = Red()
blue_object = Blue()
print(red_object.get_color())
print(blue_object.get_color())