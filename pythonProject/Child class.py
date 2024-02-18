class Staff:
    def __init__(self, name, title, salary):
        self.name = name
        self.title = title
        self.salary = salary

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Title: {self.title}")
        print(f"Salary: {self.salary}")
class Teacher(Staff):
    def __init__(self, name, title, salary, subject):
        super().__init__(name, title, salary)
        self.subject = subject

    def display_details(self):
        super().display_details()
        print(f"Subject: {self.subject}")

teacher1 = Teacher("John Doe", "Teacher", 50000, "Math")
teacher2 = Teacher("Don Caleb", "Principal", 800000, "Chemistry")
teacher1.display_details()
teacher2.display_details()