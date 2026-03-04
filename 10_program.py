# Q11 (4 Marks): Write a Python program to create a class Student with:
# • attributes: name and marks
# • method to compute grade
# Create two objects and print their grades.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def compute_grade(self):
        if self.marks >= 90:
            return 'A'
        elif self.marks >= 80:
            return 'B'
        elif self.marks >= 70:
            return 'C'
        elif self.marks >= 60:
            return 'D'
        else:
            return 'F'      
student1 = Student("Alice", 85)
student2 = Student("Bob", 72)
print(f"{student1.name}'s grade: {student1.compute_grade()}")
print(f"{student2.name}'s grade: {student2.compute_grade()}")
