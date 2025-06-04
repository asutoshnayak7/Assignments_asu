
# Create an empty dictionary to store student names and their grades
student_grades = {}

# Start an infinite loop to keep showing the menu until the user chooses to exit
while True:
    # Display the menu options
    print("\n--- Menu ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    # Ask the user to enter their choice
    choice = input("Enter your choice (1-4): ")

    # If the user chooses option 1: Add a new student
    if choice == '1':
        # Ask for the student's name
        name = input("Enter student name: ")
        # Check if the student already exists in the dictionary
        if name in student_grades:
            print("Student already exists.")  # Inform the user if the student is already added
        else:
            # Ask for the student's grade
            grade = input("Enter grade: ")
            # Add the student and grade to the dictionary
            student_grades[name] = grade
            print("Student added.")  # Confirm addition

    # If the user chooses option 2: Update an existing student's grade
    elif choice == '2':
        # Ask for the student's name to update
        name = input("Enter student name to update: ")
        # Check if the student exists in the dictionary
        if name in student_grades:
            # Ask for the new grade
            grade = input("Enter new grade: ")
            # Update the grade in the dictionary
            student_grades[name] = grade
            print("Grade updated.")  # Confirm update
        else:
            print("Student not found.")  # Inform if student doesn't exist

    # If the user chooses option 3: Print all student grades
    elif choice == '3':
        # Check if the dictionary is empty
        if len(student_grades) == 0:
            print("No student data available.")  # Inform if no data
        else:
            print("\n--- Student Grades ---")
            # Loop through the dictionary and print each student's name and grade
            for name in student_grades:
                print(name + ": " + student_grades[name])

    # If the user chooses option 4: Exit the program
    elif choice == '4':
        print("Exiting program.")  # Exit message
        break  # Exit the loop and end the program

    # If the user enters an invalid option
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")  # Error message
