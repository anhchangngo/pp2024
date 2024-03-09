# domains/Student.py

from domains.Info import Info
from domains.bcolors import bcolors

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
                
