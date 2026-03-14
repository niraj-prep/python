import math

class Student:
    def __init__(self, name, department, year, semester, section, roll_number):
        self.name = name
        self.department = department
        self.year = year
        self.semester = semester
        self.section = section
        self.roll_number = roll_number


class Marksheet(Student):
    def __init__(self, name, department, year, semester, section, roll_number, subject_marks):
        super().__init__(name, department, year, semester, section, roll_number)
        self.subject_marks = subject_marks

    def display_marksheet(self):
        print("STUDENT MARKSHEET")
        print("Name:", self.name)
        print("Department:", self.department)
        print("Year:", self.year)
        print("Semester:", self.semester)
        print("Section:", self.section)
        print("Roll Number:", self.roll_number)

        for i in range(5):
            print(f"Subject {i + 1} Marks: {self.subject_marks[i]:.1f}")
        total = sum(self.subject_marks)
        percentage = total / 5
        print(f"Total Marks: {total:.1f}")
        print(f"Percentage: {percentage:.2f}%")


try:
    name = input("Name: ")
    department = input("Department: ")
    year = input("Year: ")
    semester = input("Semester: ")
    section = input("Section: ")
    roll_number = input("Roll Number: ")

    subject_marks = []
    for i in range(1, 6):
        mark = float(input(f"Enter marks for subject {i}: "))
        subject_marks.append(mark)

    student_marksheet = Marksheet(
        name, department, year, semester, section, roll_number, subject_marks
    )

    student_marksheet.display_marksheet()

except ValueError:
    print("\nError: Please ensure marks are entered as valid numbers (integers or decimals).")
except Exception as e:
    print(f"\nAn unexpected error occurred: {e}")
