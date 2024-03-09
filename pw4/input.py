# input.py

import re
import math
from domains import Course, Student
from domains import bcolors
from domains import Class


def new_student(self):
    idx_student = self.insert("students")
    for _ in range(idx_student):
        student = {}
        student['id'] = input("Enter student ID: ")
        while True:
            if not re.match(r"\d{2}BI\d{3}", student['id']):
                student['id'] = input(f"{bcolors.FAIL}OOPS ID is Invalid, Enter again: {bcolors.ENDC}")
                continue
            if any(ext_student.get_id() == student['id'] for ext_student in self.get_students()):
                student['id'] = input(f"{bcolors.FAIL}OOPS ID already exists, Enter again: {bcolors.ENDC}")
                continue
            break

        student['name'] = input("Enter student name: ")

        while True:
            dob_input = input("Enter date of birth (YYYY-MM-DD): ")
            if self.validate_date(dob_input):
                student['DoB'] = dob_input
                break

        self.get_students().append(Student(student['id'], student['name'], student['DoB']))
    print("Student information added successfully.")

        
def new_marks(self):
        if not self.get_students() and not self.get_courses():
            print(f"{bcolors.FAIL}Add students and courses first.{bcolors.ENDC}")
            return
        elif not self.get_students():
            print(f"{bcolors.FAIL}Add students first.{bcolors.ENDC}")
            return
        elif not self.get_courses():
            print(f"{bcolors.FAIL}Add courses first.{bcolors.ENDC}")
            return

        print("List of students:")
        for i, student in enumerate(self.get_students(), 1):
            print(f"{i}. {student.get_id()} - {student.get_name()} - {student.get_DoB()}")

        while True:
            try:
                student_idx = int(input("Enter the index of the student: ")) - 1
                if 0 <= student_idx < len(self.get_students()):
                    break
                else:
                    print(f"{bcolors.FAIL}OOPS Invalid index. Please enter again.{bcolors.ENDC}")
            except ValueError:
                print(f"{bcolors.FAIL}OOPS Invalid input. Please enter a valid integer.{bcolors.ENDC}")

        print("List of courses:")
        for i, course in enumerate(self.get_courses(), 1):
            print(f"{i}. {course.get_id()} - {course.get_name()}")

        while True:
            try:
                course_idx = int(input("Enter the index of the course: ")) - 1
                if 0 <= course_idx < len(self.get_courses()):
                    break
                else:
                    print(f"{bcolors.FAIL}OOPS Invalid index. Please enter again.{bcolors.ENDC}")
            except ValueError:
                print(f"{bcolors.FAIL}OOPS Invalid input. Please enter a valid integer.{bcolors.ENDC}")

        student = self.get_students()[student_idx]
        course = self.get_courses()[course_idx]

        # if 'marks' not in student:
        if not student.get_marks():
            student.set_marks = {}

        mark = float(input(f"Enter the mark for {student.get_name()} in course {course.get_id()}: "))
        mark = math.floor(mark * 10) / 10   # floor a number to one character after the decimal point
        student.add_mark(course.get_id(), mark)
        print(f"{bcolors.OKGREEN}Mark added successfully for {student.get_name()} in course {course.get_id()}.{bcolors.ENDC}")

def new_course(self):
        idx_course = self.insert("courses")
        for _ in range(idx_course):
            course = {}
            course['id'] = input("Enter course ID: ")
            while True:
                if any(ext_course.get_id() == course['id'] for ext_course in self.get_courses()):
                    course['id'] = input(f"{bcolors.FAIL}OOPS course ID already exists, Enter again: {bcolors.ENDC}")
                    continue
                break
            course['name'] = input("Enter course name: ")
            course['credits'] = int(input("Enter credit number: "))
            while True:
                if any(ext_course.get_name() == course['name'] for ext_course in self.get_courses()):
                    course['name'] = input(f"{bcolors.FAIL}OOPS Course already exists, Enter again: {bcolors.ENDC}")
                    continue
                break
            new_course = Course(course['id'], course['name'], course['credits'])
            self.set_courses(self.get_courses() + [new_course])
        print("Course information added successfully.")

