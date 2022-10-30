class Person:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

    def go_to_the_school(self):
        print(f"{self.name} should go to the school everyday")


class Student(Person):
    def exam(self):
        print(f"{self.name} should pass an exam soon")


class Teacher(Person):
    def sal(self, salary):
        print(f"{self.name} will receive {salary}$ in the end of the month")


student = Student("Vlad", 29, "ukrainian")
student.go_to_the_school()


teacher = Teacher("Hanna Vasylivna", 45, "ukrainian")
teacher.sal(1221)
