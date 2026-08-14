class Student:
    def __init__(self, name, m1, m2, m3):
        self.name = name
        self.marks = [m1, m2, m3]
    @staticmethod
    def input():
        name = input("Enter name: ")
        m1 = int(input("Enter mark 1: "))
        m2 = int(input("Enter mark 2: "))
        m3 = int(input("Enter mark 3: "))
        return Student(name, m1, m2, m3)

    def average(self):
        print(sum(self.marks) / len(self.marks))


s1 = Student.input()
s1.average()
