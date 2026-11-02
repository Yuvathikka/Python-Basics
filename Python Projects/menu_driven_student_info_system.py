students ={}
def add_students():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    students[roll] = {"Name": name, "Department": dept}
    print("Student added successfully.")

def view_students():
    if not students:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for roll, data in students.items():
        print("Roll No:", roll,
              "| Name:", data["Name"],
              "| Department:", data["Department"])

def search_students():
    roll = input("Enter Roll No to search: ")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")

def  delete_students():
    roll = input("Enter Roll No to delete: ")
    if roll in students:
        del students[roll]
        print("Student deleted successfully.")
    else:
        print("Student not found.")

def update_students():
    roll = input("Enter Roll No to update: ")
    if roll in students:
        name = input("Enter new Name: ")
        dept = input("Enter new Department: ")
        students[roll] = {"Name": name, "Department": dept}
        print("Student updated successfully.")
    else:
        print("Student not found.")

while True:
    print("\n--- Student Information System ---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        add_students()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_students()
    elif choice == '4':
        delete_students()
    elif choice == '5':
        update_students()
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")