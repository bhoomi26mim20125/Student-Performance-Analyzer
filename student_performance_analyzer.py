students = []


def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    marks = []

    print("\nEnter marks for 3 subjects:")

    for i in range(1, 4):
        while True:
            try:
                mark = float(input(f"Enter marks for Subject {i}: "))

                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")

            except ValueError:
                print("Please enter a valid number.")

    student = {
        "name": name,
        "roll_no": roll_no,
        "marks": marks
    }

    students.append(student)

    print("\nStudent added successfully!")


def view_students():
    if len(students) == 0:
        print("\nNo student records found.")
        return

    print("\n===== Student Records =====")

    for student in students:
        print("\nName:", student["name"])
        print("Roll Number:", student["roll_no"])
        print("Marks:", student["marks"])


def calculate_result(student):
    marks = student["marks"]

    total = sum(marks)
    average = total / len(marks)
    percentage = (total / (len(marks) * 100)) * 100

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    if percentage >= 40:
        result = "Pass"
    else:
        result = "Fail"

    return total, average, percentage, grade, result


def analyze_student():
    if len(students) == 0:
        print("\nNo student records found.")
        return

    roll_no = input("Enter roll number to analyze: ")

    for student in students:
        if student["roll_no"] == roll_no:

            total, average, percentage, grade, result = calculate_result(student)

            print("\n===== Student Analysis =====")
            print("Name:", student["name"])
            print("Roll Number:", student["roll_no"])
            print("Marks:", student["marks"])
            print("Total:", total)
            print("Average:", round(average, 2))
            print("Percentage:", round(percentage, 2), "%")
            print("Grade:", grade)
            print("Result:", result)

            return

    print("\nStudent not found.")


def save_data():
    if len(students) == 0:
        print("\nNo student data to save.")
        return

    with open("students.txt", "w") as file:
        for student in students:
            file.write("Name: " + student["name"] + "\n")
            file.write("Roll Number: " + student["roll_no"] + "\n")
            file.write("Marks: " + str(student["marks"]) + "\n")
            file.write("\n")

    print("\nStudent data saved successfully.")


def main():
    while True:
        print("\n================================")
        print("   STUDENT PERFORMANCE ANALYZER")
        print("================================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Analyze Student")
        print("4. Save Data")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            analyze_student()

        elif choice == "4":
            save_data()

        elif choice == "5":
            print("\nThank you for using Student Performance Analyzer!")
            break

        else:
            print("\nInvalid choice. Please try again.")


main()
