'''
My code need python3 to run, so in terminal run the command python3 ../../../2.student.mark.py
Note:
    - ID of a student must be [2 digits] BI [3 or more digits], for example: 22BI13075 (It's my student ID ====))
    - When you have added marks to a course but then select the add marks option, 
      the final mark printed is the last modified mark.
    - When choosing the add marks option, you can only add it once, because I think it will be easier to manage
    - If you don't have any points then gpa = 0
    - GPA scores are only calculated for subjects that have been entered
'''

import re
import os  # clear terminal
from datetime import datetime
import math # Import math library
import numpy as np

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# When there is an error or duplicate information, there will be a message with a different color on the terminal
# And I get ideal from https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal

class Info:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        
    def get_id(self):
        return self.__id
        
    def set_id(self, id):
        self.__id = id
        
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        self.__name = name

class Student(Info):
    def __init__(self, student_id, name, dob):
        super().__init__(student_id, name)
        self.__DoB = dob
        self.__marks = {}
# I use self.marks = {} , because I care about every Student object having a marks, even if it's empty, 
# and I don't care about passing the value in from outside
# You can read from https://stackoverflow.com/questions/73558505/python-classes-exam-marks-project

    def get_DoB(self):
        return self.__DoB
        
    def get_marks(self):
        return self.__marks

    def add_mark(self, course_id, mark):
        self.__marks[course_id] = mark

    def display_info(self, courses_list):
        print(f"{self.get_id()} - {self.get_name()} - {self.get_DoB()}")
        if self.__marks:
            print("Marks:")
            for course_id, mark in self.__marks.items():       # items : Return a list of pairs
                course_name = next((course.get_name() for course in courses_list if course.get_id() == course_id), None)
                course_credit = next((course.get_credits() for course in courses_list if course.get_id() == course_id), None)
                print(f"   - Course {course_id} ({course_name}): {mark} ({course_credit} credit{'s' if course_credit != 1 else ''})")
            missing_courses = set(course.get_id() for course in courses_list) - set(self.__marks.keys())    # Set is used to create collections containing unique elements
            for course_id in missing_courses:
                course_name = next((course.get_name() for course in courses_list if course.get_id() == course_id), None)
                course_credit = next((course.get_credits() for course in courses_list if course.get_id() == course_id), None)
                print(f"   - Course {course_id} ({course_name}): NULL ({course_credit} credit{'s' if course_credit != 1 else ''})")
        else:
            print(f"{bcolors.FAIL}No marks available for this student.{bcolors.ENDC}")
            print("List of courses:")
            for i, course in enumerate(courses_list, 1):
                print(f"   {i}. {course.get_id()} - {course.get_name()} - {course.get_credits()} credit{'s' if course.get_credits() != 1 else ''}")   # enumerate is used to iterate through the courses_list along with the index of each element.

class Course:
    def __init__(self, course_id, name, credits):
        self.__id = course_id
        self.__name = name
        self.__credits = credits
        
    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        self.__id = id
        
    def get_name(self):
        return self.__name
        
    def set_name(self, name):
        self.__name = name
        
    def get_credits(self):
        return self.__credits
    
    def set_credits(self, credits):
        self.__credits = credits

class Class:
    def __init__(self):
        self.__students = []
        self.__courses = []
        
    def get_students(self):
        return self.__students
    
    def set_students(self, students):
        self.__students = students
        
    def get_courses(self):
        return self.__courses
    
    def set_courses(self, courses):
        self.__courses = courses

    def insert(self, args):
        return int(input(f"Enter the number of {args} in this class: "))

    def clear_terminal(self):
        os.system("cls" if os.name == "nt" else "clear")
# When I get to the next selection I want to clear the information I entered before, making the terminal easier to see
# And I get ideal from https://stackoverflow.com/questions/2084508/clear-terminal-in-python

    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            print(f"{bcolors.FAIL}OOPS data format is Invalid, should be YYYY-MM-DD. {bcolors.ENDC}")
            return False
# I want to make sure I entered the correct date format
# And I get ideal from https://stackoverflow.com/questions/44716920/how-do-i-check-date-of-birth-format-is-correct

    def add_student(self):
        idx_student = self.insert("students")
        for _ in range(idx_student):    # When you are not interested in some values returned by a function we use underscore in place of variable name . Basically it means you are not interested in how many times the loop is run till now just that it should run some specific number of times overall.
            student = {}
            student['id'] = input("Enter student ID: ")
            while True:
                if not re.match(r"\d{2}BI\d{3}", student['id']):    # By using the "r" character before the regular expression, the characters "" in the regular expression will not be treated as special characters, but as ordinary characters.
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

            self.get_students().append(Student(student['id'], student['name'], student['DoB'])) # The append() method appends an element to the end of the list.
        print("Student information added successfully.")

    def add_course(self):
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

    def list_students_info(self):
        if not self.get_students():
            print(f"{bcolors.FAIL}List of students is empty. {bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}List of students : {bcolors.ENDC}")
            for i, student in enumerate(self.get_students(), 1):  # enumerate simply means I want to print the value along with its index
                student.display_info(self.get_courses())
                
    def avg_gpa(self, student):
        if not student.get_marks():
            return 0.0 # Return 0.0 if no marks available
        
        marks = np.array(list(student.get_marks().values()))
        credits = np.array([course.get_credits() for course in self.get_courses()])
        gpa = np.sum(marks * credits) / np.sum(credits)
        gpa = math.floor(gpa * 10) / 10
        return gpa
    
    def sort_gpa(self):
        self.__students.sort(key=lambda x: self.avg_gpa(x), reverse=True)
        
    def gpa_des(self):  # student_list_by_gpa_descending
        self.sort_gpa()
        print(f"{bcolors.OKGREEN}Student list sorted by GPA (descending):{bcolors.ENDC}")
        for i, student in enumerate(self.get_students(), 1):
            print(f"{i}. {student.get_name()} - GPA: {self.avg_gpa(student)}")
                    
    def add_marks(self):
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

    def main(self):
        while True:
            print("----------------- MENU ----------------")
            print("Select an option")
            print("1. Add information of student")
            print("2. Add information of course")
            print("3. Add marks")
            print("4. Show students")
            print("5. Student list by GPA descending")
            print("6. Exit")
            print("----------------------------------------")

            option = int(input("Enter an option: "))

            if option == 1:
                self.add_student()
                self.clear_terminal()
            elif option == 2:
                self.add_course()
                self.clear_terminal()
            elif option == 3:
                self.add_marks()
            elif option == 4:
                self.list_students_info()
            elif option == 5:
                self.gpa_des()
            elif option == 6:
                break
            else:
                print("INVALID OPTION")

if __name__ == "__main__":
    student_management = Class()
    student_management.main()
