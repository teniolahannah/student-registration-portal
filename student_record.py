"""
Student Registration Portal
A simple command-line application for managing student registrations.
Demonstrates the Software Development Life Cycle (SDLC) process.
"""

# Global list to store student data
students = []


def display_header():
    """Display the application header."""
    print("\n" + "="*50)
    print("     STUDENT REGISTRATION PORTAL")
    print("="*50 + "\n")


def register_student():
    """
    Register a new student by collecting their information.
    Stores student data in the global students list.
    """
    print("\n--- Register New Student ---")
    
    # Collect student information
    name = input("Enter student name: ").strip()
    email = input("Enter student email: ").strip()
    course = input("Enter course: ").strip()
    
    # Validate input (basic validation)
    if not name or not email or not course:
        print("Error: All fields are required. Student not registered.\n")
        return
    
    # Create student record
    student = {
        "name": name,
        "email": email,
        "course": course
    }
    
    # Add to students list
    students.append(student)
    print(f"\n✓ Student '{name}' registered successfully!\n")


def view_students():
    """
    Display all registered students in a formatted table.
    Shows a message if no students are registered.
    """
    if len(students) == 0:
        print("\nNo students registered yet.\n")
        return
    
    print("\n" + "="*70)
    print("                    REGISTERED STUDENTS")
    print("="*70)
    print(f"{'No.':<5} {'Name':<20} {'Email':<25} {'Course':<20}")
    print("-"*70)
    
    for i, student in enumerate(students, start=1):
        print(f"{i:<5} {student['name']:<20} {student['email']:<25} {student['course']:<20}")
    
    print("-"*70)
    print(f"Total Students: {len(students)}\n")


def search_student():
    """
    Search for a student by name.
    Displays matching student records.
    """
    if len(students) == 0:
        print("\nNo students registered yet.\n")
        return
    
    search_name = input("\nEnter student name to search: ").strip().lower()
    
    matches = [s for s in students if search_name in s['name'].lower()]
    
    if not matches:
        print(f"\nNo students found with name containing '{search_name}'.\n")
        return
    
    print(f"\n--- Search Results ({len(matches)} found) ---")
    for i, student in enumerate(matches, start=1):
        print(f"{i}. {student['name']} | {student['email']} | {student['course']}")
    print()


def display_menu():
    """Display the main menu options."""
    print("--- MAIN MENU ---")
    print("1. Register Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")
    print("-"*17)


def get_user_choice():
    """
    Get and validate user menu choice.
    Returns the user's choice as a string.
    """
    choice = input("Enter your choice (1-4): ").strip()
    return choice


def main():
    """
    Main function to run the Student Registration Portal.
    Handles the menu loop and user interactions.
    """
    display_header()
    print("Welcome to the Student Registration Portal!")
    print("Manage student records efficiently.\n")
    
    # Main program loop
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            register_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("\nThank you for using Student Registration Portal!")
            print("Exiting program...\n")
            break
        else:
            print("\n⚠ Invalid choice. Please enter a number between 1 and 4.\n")


# Program entry point
if __name__ == "__main__":
    main()
