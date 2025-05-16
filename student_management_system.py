# Project: Student Management System (OOP-Based App)

# Project Title: Student Management System

# Objective:
# To implement a CLI-based application that manages student records (Add, View, Update, Delete) using OOP concepts like:
# - Classes
# - Objects
# - Encapsulation
# - Inheritance (Optional for role separation)
# - Dunder Methods

class Student:
    def __init__(self, id, name, course, mark):
        self.id = id
        self.name = name
        self.course = course
        self.mark = mark

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Course: {self.course}, Mark: {self.mark}"

class StudentManagementSystem:
    def __init__(self):
        self._students = {}

    def add_student(self, id, name, course, mark):
        if id in self._students:
            print("Student with {} already exists.".format(id))
        else:
            student = Student(id, name, course, mark)
            self._students[id] = student
            print(f"Student {name} added successfully.")

    def view_student(self, id):
        if id in self._students:
            print(self._students[id])
        else:
            print(f"Student with ID '{id}' not found")

    def view_all_students(self):
        if not self._students:
            print("No students in the system.")
        else:
            print("All Students:")
            for student in self._students.values():
                print(student)

    def update_student(self, id, name=None, course=None, mark=None):
        if id in self._students:
            if name:
                self._students[id].name = name
            if course:
                self._students[id].course = course
            if mark:
                self._students[id].mark = mark

            print(f"Student {name} updated successfully.")
        else:
            print(f"Student with ID '{id}' not found")

    def delete_student(self, id):
        if id in self._students:
            del self._students[id]
            print(f"Student with ID '{id}' deleted successfully.")
        else:
            print(f"Student with ID '{id}' not found")

if __name__ == "__main__":
    sms = StudentManagementSystem()

    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Student")
        print("3. View all students")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            course = input("Enter student course: ")
            mark = input("Enter student mark: ")
            sms.add_student(id, name, course, mark)
        elif choice == "2":
            id = input("Enter student ID: ")
            sms.view_student(id)
        elif choice == "3":
            sms.view_all_students()
        elif choice == "4":
            id = input("Enter student ID: ")
            name = input("Enter student name (optional): ")
            course = input("Enter student course (optional): ")
            mark = input("Enter student mark (optional): ")
            sms.update_student(id, name or None, course or None, mark or None)
        elif choice == "5":
            id = input("Enter student ID: ")
            sms.delete_student(id)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please choose a valid option.")