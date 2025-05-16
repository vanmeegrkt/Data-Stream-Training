# Write a menu driven program to perform the following operations:
# 1. Write a file
# 2. Read a file
# 3. Append a file
# 4. Exit

# Each operation should be in a separate function
# With Exception handling
# Exit the program if the user enters 4


def write_file():
    try:
        filename = input("Enter the file name: ")
        with open(filename, "w") as file:
            file.write("Hello, world!")
        print(f"File '{filename}' created successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")


def read_file():
    try:
        filename = input("Enter the file name: ")
        with open(filename, "r") as file:
            content = file.read()
        print(f"File content: {content}")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {str(e)}")


def append_file():
    try:
        filename = input("Enter the file name: ")
        with open(filename, "a") as file:
            content = input("Enter the content to append: ")
            file.write(content)
        print(f"File '{filename}' appended successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")


def exit_program():
    print("Exiting the program.")
    exit()


while True:
    print("\nMenu:")
    print("1. Write a file")
    print("2. Read a file")
    print("3. Append a file")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        write_file()
    elif choice == "2":
        read_file()
    elif choice == "3":
        append_file()
    elif choice == "4":
        exit_program()
    else:
        print("Invalid choice. Please try again.")