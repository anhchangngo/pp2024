# domains/Class.py

import math
import os
import numpy as np
from .bcolors import bcolors
from datetime import datetime
from input import new_student, new_course, new_marks

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
    
    def validate_date(self, date_text):
        try:
            datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            print(f"{bcolors.FAIL}OOPS data format is Invalid, should be YYYY-MM-DD. {bcolors.ENDC}")
            return False

    def new_student(self):
        # new_student(self.get_students())
        new_student(self)
        
    def new_course(self):
        # new_course(self.get_courses())
        new_course(self)
        
    def list_students_info(self):
        if not self.get_students():
            print(f"{bcolors.FAIL}List of students is empty. {bcolors.ENDC}")
        else:
            print(f"{bcolors.OKGREEN}List of students : {bcolors.ENDC}")
        for i, student in enumerate(self.get_students(), 1):  # enumerate simply means I want to print the value along with its index
            student.display_info(self.get_courses())
                      
    def avg_gpa(self, student):
        if not student.get_marks():
            return 0.0
        
        marks = np.array(list(student.get_marks().values()))
        credits = np.array([course.get_credits() for course in self.get_courses()])
        gpa = np.sum(marks * credits) / np.sum(credits)
        gpa = math.floor(gpa * 10) / 10
        return gpa
    
    def sort_gpa(self):
        self.__students.sort(key=lambda x: self.avg_gpa(x), reverse=True)
        
    def gpa_des(self):
        self.sort_gpa()
        print(f"{bcolors.OKGREEN}Student list sorted by GPA (descending):{bcolors.ENDC}")
        for i, student in enumerate(self.get_students(), 1):
            print(f"{i}. {student.get_name()} - GPA: {self.avg_gpa(student)}")
                    
    def new_marks(self):
        # new_marks(self.get_students(), self.get_courses())
        new_marks(self)
        