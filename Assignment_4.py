
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display_details(self):
        print()
        print(f" Name: {self.name}, Email: {self.email}")

class Student(Person):
    def __init__(self, name, email, year_of_study):
        super().__init__(name, email)
        self.year_of_study = year_of_study
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)
        print()
        print(f"{self.name} has enrolled for course: {course}")

class Lecturer(Person):
    def __init__(self, name, email, department):
        super().__init__(name, email)
        self.department = department

    def assign_course_material(self, course, material):
        print()
        print(f"{self.name} assigned material '{material}' to course {course}")
        print()

student = Student("Kato Joseph", "josephkato@gmail.com", "Year 2")
lecturer = Lecturer("Dr. Tamale", "tamale@edu.mak.ac", "Computer Science")
print()

student.display_details()
student.add_course("CS101")
student.add_course("MATH201")

print()
lecturer.display_details()
print()