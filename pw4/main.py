from domains import Class

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
            self.new_student()
            self.clear_terminal()
        elif option == 2:
            self.new_course()
            self.clear_terminal()
        elif option == 3:
            self.new_marks()
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
    main(student_management)
