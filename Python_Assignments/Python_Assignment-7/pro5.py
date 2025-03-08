class Department:
    def __init__(self, name):
        # Initializer to set the department's name
        self.name = name
    
    def __str__(self):
        # Return the name of the department
        return f"Department: {self.name}"

class University:
    def __init__(self, name, location):
        # Initializer to set university's name, location, and initialize an empty departments list
        self.name = name
        self.location = location
        self.departments = []
    
    def add_department(self, department):
        # Add a department to the university
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")
    
    def display_university_details(self):
        # Display the university's details including all departments
        print(f"\nUniversity Name: {self.name}")
        print(f"Location: {self.location}")
        if self.departments:
            print("\nDepartments:")
            for dept in self.departments:
                print(dept)
        else:
            print("No departments available.")

# Function to interact with the system
def university_system():
    # Create a University object
    university_name = input("Enter the university name: ")
    university_location = input("Enter the university location: ")
    university = University(university_name, university_location)
    
    while True:
        # Display options to the user
        print("\nUniversity System Menu:")
        print("1. Add a Department")
        print("2. Display University Details")
        print("3. Exit")
        
        # Get the user choice
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            # Add a department to the university
            dept_name = input("Enter department name: ")
            department = Department(dept_name)
            university.add_department(department)
 
