import os
import threading
import zipfile
import pickle
from domains import Class

# Function to compress files into students.zip
def compress_files():
    try:
        # Serialize the data using pickle
        std = {}
        for filename in ['students.txt', 'courses.txt', 'marks.txt']:
            with open(filename, "rb") as f:
                std[filename] = f.read()
        # Compress the serialized data
        with zipfile.ZipFile("students.dat", "w") as z:
            pickle.dump(std, z)
            print(f"Compressing {filename}...")
        print("Compression successful.")
    except Exception as e:
        print("Compression failed:", e)

# Function to decompress data from students.zip
def decompress_files():
    try:
        if os.path.exists('students.dat'):
            std = {}
            with open('students.dat', 'r') as z:
                std = pickle.load(z)
            for i in std:
                print(i)
            print("Decompression successful. Extracted files are in:", os.getcwd())
        else:
            print("No compressed file found.")
    except Exception as e:
        print("Decompression failed:", e)

t1 = threading.Thread(target=compress_files)
t2 = threading.Thread(target=decompress_files)
t1.start()
t2.start()
t1.join()
t2.join()

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
