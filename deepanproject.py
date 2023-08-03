#importing json module 
import json
#creating a variable
STUDENT_DOCUMENT = "DEEPAN_students.json"

#creating a function called load_students to open and read the file
def load_students():
    try:
        with open(STUDENT_DOCUMENT, 'r') as file:
            students = json.load(file)
    except FileNotFoundError:
        students = []
    return students

#creating a function 'save_students' to open in a 'write mode'
def save_students(students):
    with open(STUDENT_DOCUMENT, 'w') as file:
        json.dump(students, file, indent=4)

#creating a function to get input
def d_add_students():
    d = input("Enter student's Name: ")
    e = int(input("Enter student's Age: "))
    e = input("Enter student's Grade: ")
    p = input("Enter student's Contact details: ")

#the function 'load_students' is stored in a 'students' variable 
    students = load_students()
    students.append({"Name": d, "Age": e, "Grade": e, "Contact": p})
    save_students(students)
    print("Student details added successfully!")


def e_view_students():
    students = load_students()
    if students:
        print("\nStudent details:")
        for student in students:
            print(f"Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}, Contact: {student['Contact']}")
    else:
        print("No student details found.")


def e_search_student():
    query = input("Enter the name or grade of the student to search: ")

    students = load_students()
    found_students = []
    for student in students:
        if query.lower() in student['Name'].lower() or query.lower() == student['Grade'].lower():
            found_students.append(student)

    if found_students:
        print("\nFound Students:")
        for student in found_students:
            print(f"Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}, Contact: {student['Contact']}")
    else:
        print("No matching student details found.")


def p_update_student():
    query = input("Enter the name of the student to update: ")

    students = load_students()
    for student in students:
        if query.lower() in student['Name'].lower():
            print(f"Student Found: Name: {student['Name']}, Age: {student['Age']}, Grade: {student['Grade']}, Contact: {student['Contact']}")
            new_age = int(input("Enter updated Age: "))
            new_grade = input("Enter updated Grade: ")
            new_contact = input("Enter updated Contact details: ")
            student['Age'] = new_age
            student['Grade'] = new_grade
            student['Contact'] = new_contact
            save_students(students)
            print("Student details updated successfully!")
        else:
            print("No matching student found.")


def an_delete_student():
    query = input("Enter the name of the student to delete: ")

    students = load_students()
    updated_students = [student for student in students if query.lower() not in student['Name'].lower()]

    if len(updated_students) < len(students):
        save_students(updated_students)
        print("Student details deleted successfully!")
    else:
        print("No matching student found.")


def main():
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            d_add_students()
        elif choice == '2':
            e_view_students()
        elif choice == '3':
            e_search_student()
        elif choice == '4':
            p_update_student()
        elif choice == '5':
            an_delete_student()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()