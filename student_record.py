# Student Registration Portal

# List to store student data
students = []

# Function to register student
def register_student():
    name = input("Enter student name: ")
    email = input("Enter student email: ")
    course = input("Enter course: ")
    students.append({"name": name, "email": email, "course": course})
    print("Student registered successfully!\n")

# Function to view all students
def view_students():
    if len(students) == 0:
        print("No students registered yet.\n")
        return
    print("\n--- Registered Students ---")
    for i, s in enumerate(students, start=1):
        print(f"{i}. {s['name']} | {s['email']} | {s['course']}")
    print()

# Main menu
while True:
    print("1. Register Student")
    print("2. View Students")
    print("3. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        register_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.\n")