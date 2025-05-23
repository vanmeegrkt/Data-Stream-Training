import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="data_stream_training"
)
print("Connected to MySQL database!", conn)

cursor = conn.cursor()

def create_dtable():
    # table creation
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS students (
                   id INT AUTO_INCREMENT PRIMARY KEY,
                   name VARCHAR(100),
                   age INT
                   )""")
    conn.commit()
    
def insert_data():
    # insert data
    sql = "INSERT INTO students (name, age) VALUES (%s, %s)"
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    val = (name, age)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "record inserted.")

def delete_data():
    # delete data
    sql = "DELETE FROM students WHERE name = %s"
    name = input("Enter name: ")
    val = (name,)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "record deleted.")

def view_data():
    # view data
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    for row in result:
        print(row)

def update_data():
    # update data
    # Update age or name of a student by name
    sql = "UPDATE students SET age = %s and name = %s WHERE id = %s"
    id = input("Enter id: ")
    age = int(input("Enter age: "))
    name = input("Enter name: ")
    val = (age, name, id)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "record updated.")

def update_specific_data():
    # Generic function to update any specific column
    column = input("Enter the column name to update (e.g., name, age): ")
    new_value = input(f"Enter the new value for {column}: ")
    condition_column = input("Enter the column name for condition (e.g., id, name): ")
    condition_value = input(f"Enter the value for {condition_column} to identify the record: ")

    # Prepare sql and values
    sql = f"UPDATE students SET {column} = %s WHERE {condition_column} = %s"
    val = (new_value, condition_value)
    cursor.execute(sql, val)
    conn.commit()
    print(cursor.rowcount, "record(s) updated.")

def search_data():
    # search data
    sql = "SELECT * FROM students WHERE name = %s"
    name = input("Enter name: ")
    val = (name,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    for row in result:
        print(row)

def alter_data():
    # alter data
    sql = "ALTER TABLE students ADD COLUMN email VARCHAR(100)"
    cursor.execute(sql)
    conn.commit()
    print(cursor.rowcount, "record updated.")

def main():
    while True:
        print("\nMenu:")
        print("1. Create table")
        print("2. Insert data")
        print("3. Delete data")
        print("4. View data")
        print("5. Update data")
        print("6. Update specific data")
        print("7. Search data")
        print("8. Alter data")
        print("9. Exit\n")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            create_dtable()
        elif choice == 2:
            insert_data()
        elif choice == 3:
            delete_data()
        elif choice == 4:
            view_data()
        elif choice == 5:
            update_data()
        elif choice == 6:
            update_specific_data()
        elif choice == 7:
            search_data()
        elif choice == 8:
            alter_data()
        elif choice == 9:
            break

    # create_dtable()
    # insert_data()

if __name__ == "__main__":
    main()