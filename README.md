# Student Registration Portal

A Python-based student registration system that demonstrates the Software Development Life Cycle (SDLC) process. This command-line application allows users to register students and view registered student records.

## Overview

This project implements a simple yet functional student registration portal that manages student information including name, email, and course enrollment. The application serves as a practical demonstration of fundamental programming concepts and the SDLC methodology.

## Features

- **Student Registration**: Add new students with name, email, and course information
- **View All Students**: Display a formatted list of all registered students
- **Interactive Menu**: User-friendly command-line interface
- **Data Validation**: Input handling and error checking
- **Session-based Storage**: Maintains student records during runtime

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Clone the repository:
```bash
git clone https://github.com/teniolahannah/student-registration-portal.git
```

2. Navigate to the project directory:
```bash
cd student-registration-portal
```

3. Run the program:
```bash
python student_record.py
```

## Usage

When you run the program, you'll see a menu with three options:

```
1. Register Student
2. View Students
3. Exit
```

### Registering a Student

1. Select option `1` from the main menu
2. Enter the student's name when prompted
3. Enter the student's email address
4. Enter the course name
5. The system will confirm successful registration

**Example:**
```
Enter your choice: 1
Enter student name: John Doe
Enter student email: john.doe@university.edu
Enter course: Computer Science
Student registered successfully!
```

### Viewing Registered Students

1. Select option `2` from the main menu
2. The system will display all registered students in a numbered list
3. If no students are registered, you'll see a message indicating this

**Example Output:**
```
--- Registered Students ---
1. John Doe | john.doe@university.edu | Computer Science
2. Jane Smith | jane.smith@university.edu | Mathematics
```

### Exiting the Program

Select option `3` to safely exit the application.

## Project Structure

```
student-registration-portal/
│
├── student_record.py    # Main application file
└── README.md           # Project documentation
```

## SDLC Process

This project demonstrates the following SDLC phases:

1. **Planning**: Identified need for student registration system
2. **Analysis**: Defined requirements for student data management
3. **Design**: Created simple, intuitive menu-based interface
4. **Implementation**: Developed Python application with core features
5. **Testing**: Validated functionality through user scenarios
6. **Maintenance**: Code structured for easy updates and enhancements

## Future Enhancements

Potential improvements for future versions:

- Persistent data storage (CSV, JSON, or database)
- Student ID auto-generation
- Search and filter functionality
- Update and delete student records
- Email validation
- Export student records
- GUI implementation

## Technical Details

- **Language**: Python 3
- **Data Structure**: List of dictionaries
- **Programming Paradigm**: Procedural programming
- **Interface**: Command-line interface (CLI)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational purposes.

## Author

**Teniola Hannah**
- GitHub: [@teniolahannah](https://github.com/teniolahannah)

## Acknowledgments

This project was created as part of a Software Development Life Cycle learning assignment.

---

**Note**: This is a demonstration project. For production use, consider implementing data persistence, input validation, and security measures.
