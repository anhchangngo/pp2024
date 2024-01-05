'''
My code need python3 to run, so in terminal run the command python3 ../../../1.student.mark.py
Note:
    - ID of a student must be [2 digits] BI [3 or more digits], for example: 22BI13075 (It's my student ID ====))
    - When you have added marks to a course but then select the add marks option, 
      the final mark printed is the last modified mark.
    - When choosing the add marks option, you can only add it once, because I think it will be easier to manage
'''
import re
import os  # clear terminal
from datetime import datetime

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

def insert(args):
    return int(input(f"Enter the number of {args} in this class: "))

def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")
# When I get to the next selection I want to clear the information I entered before, making the terminal easier to see
# And I get ideal from https://stackoverflow.com/questions/2084508/clear-terminal-in-python

def validate(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        print(f"{bcolors.FAIL}OOPS data format is Invalid, should be YYYY-MM-DD. {bcolors.ENDC}")
        return False
# When I get to the next selection I want to make sure I entered the correct date format
# And I get ideal from https://stackoverflow.com/questions/44716920/how-do-i-check-date-of-birth-format-is-correct

def add_student(students_list):
    idx_student = insert("students")
    for _ in range(idx_student):
        student = {}
        student['id'] = input("Enter student ID: ")
        while True:
            if not re.match(r"\d{2}BI\d{3}", student['id']):
                student['id'] = input(f"{bcolors.FAIL}OOPS ID is Invalid, Enter again: {bcolors.ENDC}")
                continue
            if any(ext_student["id"] == student['id'] for ext_student in students_list):
                student['id'] = input(f"{bcolors.FAIL}OOPS ID already exists, Enter again: {bcolors.ENDC}")
                continue
            break
        
        student['name'] = input("Enter student name: ")
        
        while True:
            dob_input = input("Enter date of birth (YYYY-MM-DD): ")
            if validate(dob_input):
                student['DoB'] = dob_input
                break
                
        students_list.append(student)
    print("Student information added successfully.")

def add_course(courses_list):
    idx_course = insert("courses")
    for _ in range(idx_course):
        course = {}
        course['id'] = input("Enter course ID: ")
        while True:
            if any(ext_course["id"] == course['id'] for ext_course in courses_list):
                course['id'] = input(f"{bcolors.FAIL}OOPS course ID already exists, Enter again: {bcolors.ENDC}")
                continue
            break
        course['name'] = input("Enter course name: ")
        while True:
            if any(ext_course["name"] == course['name'] for ext_course in courses_list):
                course['name'] = input(f"{bcolors.FAIL}OOPS Course already exists, Enter again: {bcolors.ENDC}")
                continue
            break
        
        courses_list.append(course)
    print("Course information added successfully.")

def list_students_info(students_list, courses_list):
    if not students_list:
        print(f"{bcolors.FAIL}List of students is empty. {bcolors.ENDC}")
    else:
        print(f"{bcolors.OKGREEN}List of students : {bcolors.ENDC}")
        for i, student in enumerate(students_list, 1): # enumerate simply means I want to print all the values in the list along with its index i
            print(f"{i}. {student['id']} - {student['name']} - {student['DoB']}") # Use f-string to create a format string to print out student information
            if 'marks' in student:
                print("Marks:")
                for course_id, mark in student['marks'].items():
                    course_name = next((course['name'] for course in courses_list if course['id'] == course_id), None)
                    print(f"   - Course {course_id} ({course_name}): {mark}")
                # Check for courses not mark and print as NULL
                missing_courses = set(course['id'] for course in courses_list) - set(student['marks'].keys())
                for course_id in missing_courses:
                    course_name = next((course['name'] for course in courses_list if course['id'] == course_id), None)
                    print(f"   - Course {course_id} ({course_name}): NULL")
            else:
                print(f"{bcolors.FAIL}No marks available for this student.{bcolors.ENDC}")
                print("List of courses:")
                for j, course in enumerate(courses_list, 1):
                    print(f"   {j}. {course['id']} - {course['name']}")

def add_marks(students_list, courses_list):
    if not students_list and not courses_list:
        print(f"{bcolors.FAIL}Add students and courses first.{bcolors.ENDC}")
        return
    elif not students_list:
        print(f"{bcolors.FAIL}Add students first.{bcolors.ENDC}")
        return 
    elif not courses_list:
        print(f"{bcolors.FAIL}Add courses first.{bcolors.ENDC}")
        return

    print("List of students:")
    for i, student in enumerate(students_list, 1):
        print(f"{i}. {student['id']} - {student['name']} - {student['DoB']}")

    while True:
        try:
            student_idx = int(input("Enter the index of the student: ")) - 1
            if 0 <= student_idx < len(students_list):
                break
            else:
                print(f"{bcolors.FAIL}OOPS Invalid index. Please enter again.{bcolors.ENDC}")
        except ValueError:
            print(f"{bcolors.FAIL}OOPS Invalid input. Please enter a valid integer.{bcolors.ENDC}")
            
    print("List of courses:")
    for i, course in enumerate(courses_list, 1):
        print(f"{i}. {course['id']} - {course['name']}")
        
    while True:
        try:
            course_idx = int(input("Enter the index of the course: ")) - 1
            if 0 <= course_idx < len(courses_list):
                break
            else:
                print(f"{bcolors.FAIL}OOPS Invalid index. Please enter again.{bcolors.ENDC}")
        except ValueError:
            print(f"{bcolors.FAIL}OOPS Invalid input. Please enter a valid integer.{bcolors.ENDC}")

    student = students_list[student_idx]
    course = courses_list[course_idx]

    if 'marks' not in student:
        student['marks'] = {}

    mark = float(input(f"Enter the mark for {student['name']} in course {course['id']}: "))
    student['marks'][course['id']] = mark
    print(f"{bcolors.OKGREEN}Mark added successfully for {student['name']} in course {course['id']}.{bcolors.ENDC}")

def main():
    students = []
    courses = []

    while True:
        print("----------------- MENU ----------------")
        print("Select an option")
        print("1. Add information of student")
        print("2. Add information of course")
        print("3. Add marks")
        print("4. Show students")
        print("5. Exit")
        print("----------------------------------------")

        option = int(input("Enter an option: "))

        if option == 1:
            add_student(students)
            clear_terminal()
        elif option == 2:
            add_course(courses)
            clear_terminal()
        elif option == 3:
            add_marks(students, courses)
            # I don't want to clear the terminal in option 3, I want to print notification if
            # you input miss information of student or course, because mark need all of them
        elif option == 4:
            list_students_info(students, courses)
            # There are no clear_terminal() because I want to show you =====)
        elif option == 5:
            break
        else:
            print("INVALID OPTION")

if __name__ == "__main__":
    main()
