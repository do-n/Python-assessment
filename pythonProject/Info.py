class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def get_person_details(self):
        return f"Name: {self.name}, Country: {self.country}, Date of Birth: {self.date_of_birth}"

class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def get_employee_details(self):
        return f"Employee ID: {self.employee_id}, Salary: {self.salary}"

class Student:
    def __init__(self, student_id, grade):
        self.student_id = student_id
        self.grade = grade

    def get_student_details(self):
        return f"Student ID: {self.student_id}, Grade: {self.grade}"

class PersonInfo(Employee, Student, Person):
    def __init__(self, name, country, date_of_birth, employee_id, salary, student_id, grade):
        Person.__init__(self, name, country, date_of_birth)
        Employee.__init__(self, employee_id, salary)
        Student.__init__(self, student_id, grade)


    @property
    def get_person_info(self):
        person_details = self.get_person_details()
        employee_details = self.get_employee_details()
        student_details = self.get_student_details()
        return f"{person_details}, {employee_details}, {student_details}"

# Example usage
person_info = PersonInfo("Caleb MUtwiri", "Kenya", "2000-05-15", "E123", 670000, "S456", "B")
print(person_info.get_person_info)
