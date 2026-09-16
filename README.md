# Student Performance Analyzer

## About the Project

Student Performance Analyzer is a simple Python command-line project used to store student details and analyze their academic performance.

The project allows the user to add student information, view student records, calculate performance, and save student data in a text file.

## Features

* Add student details
* Enter marks for three subjects
* View student records
* Calculate total marks
* Calculate average
* Calculate percentage
* Assign grades
* Show Pass or Fail result
* Analyze a student using roll number
* Save student data to a text file

## Technologies Used

* Python 3
* File Handling
* Lists
* Dictionaries
* Functions
* Loops
* Conditional Statements
* User Input

## Requirements

* Python 3.x
* Any terminal or command prompt
* No external Python libraries are required.

## Installation

1. Clone the repository:

```bash
https://github.com/bhoomi26mim20125
```

2. Open the project folder:

```bash
cd student-performance-analyzer
```

## How to Run

Run the following command in the terminal:

```bash
python student_performance_analyzer.py
```

## How to Use

After running the program, a menu will appear.

### 1. Add Student

Select option 1 and enter:

* Student name
* Roll number
* Marks for three subjects

### 2. View Students

Select option 2 to display all students currently stored in the program.

### 3. Analyze Student

Select option 3 and enter the student's roll number.

The program displays:

* Total marks
* Average
* Percentage
* Grade
* Pass/Fail result

### 4. Save Data

Select option 4 to save the student information into `students.txt`.

### 5. Exit

Select option 5 to close the program.

## Grading System

| Percentage  | Grade |
| ----------- | ----- |
| 90 or above | A+    |
| 80–89       | A     |
| 70–79       | B     |
| 60–69       | C     |
| 50–59       | D     |
| Below 50    | F     |

The student is considered **Pass** if the percentage is 40 or above.

## Example

```text
================================
   STUDENT PERFORMANCE ANALYZER
================================
1. Add Student
2. View Students
3. Analyze Student
4. Save Data
5. Exit

Enter your choice: 1

Enter student name: Rahul
Enter roll number: 101

Enter marks for 3 subjects:
Enter marks for Subject 1: 80
Enter marks for Subject 2: 75
Enter marks for Subject 3: 85

Student added successfully!
```

## Project Structure

```text
student-performance-analyzer/
│
├── student_performance_analyzer.py
├── students.txt
└── README.md
```

## Learning Outcomes

This project helped in practicing basic Python programming concepts such as:

* Variables
* Input and output
* Lists
* Dictionaries
* Functions
* Loops
* Conditional statements
* File handling
* Basic calculations

## Conclusion

The Student Performance Analyzer provides a simple way to manage student records and calculate academic performance using basic Python programming concepts. The project demonstrates how different Python concepts can be combined to create a useful command-line application.
