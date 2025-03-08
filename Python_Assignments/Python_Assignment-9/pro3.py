def add_student_record(filename):
    # Function to add a student record to the file
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    grade = input("Enter student grade: ")
    
    # Open the file in append mode, so we don't overwrite existing records
    with open(filename, 'a') as file:
        # Write the student details in the format "Name, Age, Grade"
        file.write(f"{name},{age},{grade}\n")
    
    print(f"Student record for {name} added successfully.\n")

def display_student_records(filename):
    # Function to display all student records from the file
    try:
        # Open the file in read mode
        with open(filename, 'r') as file:
            records = file.readlines()
        
        if records:
            print("\nStudent Records:")
            for record in records:
                print(record.strip())  # Strip newline characters and print each record
        else:
            print("No student records found.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist. Please add some records first.")

def student_management_system():
    filename = "students.txt"  # File where student records will be stored
    
    while True:
        # Display menu options to the user
        print("\nStudent Management System")
        print("1. Add a Student Record")
        print("2. Display All Student Records")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            add_student_record(filename)
        elif choice == '2':
            display_student_records(filename)
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the student management system
student_management_system()
