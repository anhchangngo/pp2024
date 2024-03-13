import gzip
import pickle
import zipfile
import os
from domains import Class

def compress_files():
    try:
        # Serialize the data using pickle
        std = {}
        # with zipfile.ZipFile("students.dat", "w") as z:
        for file_name in ["students.txt", "courses.txt", "marks.txt"]:
            with open(file_name, "rb") as f:
                std[file_name] = f.read()
        # Compress the serialize 
        with zipfile.ZipFile("students.dat", "w") as z:
            pickle.dump(std, z)
        print("Compress successfully")
    except Exception as e:
        print(e)

def decompress_files():
    try:
        if os.path.exists("students.dat"):
            # Decompress the data
            with zipfile.ZipFile("students.dat", "r") as z:
                with z.open(z.namelist()[0], "r") as f:
                    std = pickle.load(z)
            # Deserialize the data
            for file_name, line in std.items():
                with open(file_name, "wb") as f:
                    f.write(line)
            print("Decompress successfully")
        else:
            print("No file name students.dat")
    except Exception as e:
        print(e)

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
            before_closing()
            break
        elif option == 7:
            at_start()
        else:
            print("INVALID OPTION")
            
# Call this function before closing the program to compress data
def before_closing():
    compress_files()

# Call this function at the beginning of your program to decompress data
def at_start():
    decompress_files()

if __name__ == "__main__":
    at_start()  # Call to decompress data at the beginning
    student_management = Class()
    main(student_management)
