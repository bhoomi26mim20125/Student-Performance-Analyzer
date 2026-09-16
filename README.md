# Student Performance Analyzer

## About the Project

Student Performance Analyzer is a simple Python command-line project used to store student details and analyze their academic performance.

The project allows the user to add student information, view student records, calculate performance, and save student data in a text file.

## Features

* Add student details
* Enter marks for three subjects
* View student records
* Analyze student performance
* Calculate total marks
* Calculate average marks
* Calculate percentage
* Assign grades
* Show Pass or Fail result
* Save student data to a text file

## Technologies Used

* Python 3
* Command Line / Terminal
* Text File

## Requirements

* Python 3.x
* Command Prompt or Terminal
* No external Python libraries are required.

## Installation

### 1. Clone the repository

```bash
https://github.com/bhoomi26mim20125/Student-Performance-Analyzer
```

### 2. Open the project folder

```bash
cd Student-Performance-Analyzer
```

## How to Run

Run the following command in the terminal:

```bash
python student_performance_analyzer.py
```

The program will start and display the main menu.

## How to Use

After running the program, the following menu will appear:

```text
================================
   STUDENT PERFORMANCE ANALYZER
================================
1. Add Student
2. View Students
3. Analyze Student
4. Save Data
5. Exit
```

### 1. Add Student

Select option 1 and enter:

* Student name
* Roll number
* Marks for three subjects

### 2. View Students

Select option 2 to view all student records currently stored in the program.

### 3. Analyze Student

Select option 3 and enter the student's roll number.

The program displays:

* Total marks
* Average
* Percentage
* Grade
* Pass/Fail result

### 4. Save Data

Select option 4 to save student information into the `students.txt` file.

### 5. Exit

Select option 5 to close the program.

## Grading System

| Percentage   | Grade |
| ------------ | ----- |
| 90 and above | A+    |
| 80–89        | A     |
| 70–79        | B     |
| 60–69        | C     |
| 50–59        | D     |
| Below 50     | F     |

A student with a percentage of 40 or above is considered **Pass**.

## Example

```text
Enter your choice: 1

Enter student name: Rahul
Enter roll number: 101

Enter marks for 3 subjects:
Enter marks for Subject 1: 80
Enter marks for Subject 2: 75
Enter marks for Subject 3: 85

Student added successfully!
```

For analysis:

```text
===== Student Analysis =====
Name: Rahul
Roll Number: 101
Marks: [80.0, 75.0, 85.0]
Total: 240.0
Average: 80.0
Percentage: 80.0 %
Grade: A
Result: Pass
```

## Project Structure

```text
Student-Performance-Analyzer/
│
├── student_performance_analyzer.py
├── students.txt
└── README.md
```

## Python Concepts Used

This project uses basic Python concepts including:

* Variables
* Data types
* Input and output
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* Arithmetic operators
* File handling

## Learning Outcomes

This project helped in practicing basic Python programming concepts and applying them to a practical command-line application.

It improved understanding of functions, lists, dictionaries, loops, conditional statements, calculations, and file handling.

## Conclusion

Student Performance Analyzer provides a simple way to manage student records and calculate academic performance using Python.

The project demonstrates how basic Python concepts can be combined to create a useful command-line application.

## Future Scope

The project can be improved in the future by:

* Adding more subjects
* Updating and deleting student records
* Searching students by name
* Generating class-level performance statistics
* Adding attendance information
* Using a database for data storage
* Adding graphical reports
