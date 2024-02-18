class Person:
    def __init__(self, name, country, year_of_birth):
        self.name = name
        self.country = country
        self.year_of_birth = year_of_birth

    def age(self):
        year = 2024
        age = year - int(self.year_of_birth)
        return age

p1 = Person("Caleb Mutwiri", "Kenya", "2005")

print(p1.age())
