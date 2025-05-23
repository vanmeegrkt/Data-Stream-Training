from pymongo import MongoClient

def connect_to_mongo():
    """
    Connect to MongoDB and return the client, database, and collection.
    """
    client = MongoClient("mongodb://localhost:27017/")
    db = client["training"]
    collection = db["students"]
    return client, db, collection

def insert_student():
    id = input("Enter student id: ")
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    student = {"id": id, "name": name, "age": age, "grade": grade}
    collection.insert_one(student)
    print("Student inserted successfully.")

def insert_multiple_students():
    n = int(input("How many students to insert? "))
    students = []
    for _ in range(n):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        age = int(input("Enter student age: "))
        grade = input("Enter student grade: ")
        students.append({"id": id, "name": name, "age": age, "grade": grade})
    collection.insert_many(students)
    print(f"{n} students inserted.")

def view_students():
    students = list(collection.find())
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

def update_student():
    id = input("Enter the id of the student to update: ")
    new_age = int(input("Enter new age: "))
    new_grade = input("Enter new grade: ")
    result = collection.update_one({"id": id}, {"$set": {"age": new_age, "grade": new_grade}})
    if result.modified_count:
        print("Student updated.")
    else:
        print("Student not found.")

def find_students_by_age():
    min_age = int(input("Enter minimum age: "))
    max_age = int(input("Enter maximum age: "))
    students = list(collection.find({"age": {"$gte": min_age, "$lte": max_age}}))
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

def find_students_by_grade():
    grade = input("Enter grade: ")
    students = list(collection.find({"grade": grade}))
    if not students:
        print("No students found.")
    else:
        for student in students:
            print(student)

def delete_student():
    id = input("Enter the id of the student to delete: ")
    result = collection.delete_one({"id": id})
    if result.deleted_count:
        print("Student deleted.")
    else:
        print("Student not found.")

def delete_multiple_students(grade):
    result = collection.delete_many({"grade": grade})
    print(f"Deleted {result.deleted_count} students.")

def main():
    global collection
    client, db, collection = connect_to_mongo()

    while True:
        print("\n1. Insert Student")
        print("2. Insert Multiple Students")
        print("3. View Students")
        print("4. Update Student")
        print("5. Find Students by Age")
        print("6. Find Students by Grade")
        print("7. Delete Student")
        print("8. Delete Multiple Students")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            insert_student()
        elif choice == "2":
            insert_multiple_students()
        elif choice == "3":
            view_students()
        elif choice == "4":
            update_student()
        elif choice == "5":
            find_students_by_age()
        elif choice == "6":
            find_students_by_grade()
        elif choice == "7":
            delete_student()
        elif choice == "8":
            delete_multiple_students()
        elif choice == "9":
            break
        else:
            print("Invalid choice. Please try again.")
    
if __name__ == "__main__":
    main()