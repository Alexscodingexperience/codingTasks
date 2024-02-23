def register_students(num_students):
    # Open the file for writing
    with open("reg_form.txt", "w") as file:
        for _ in range(num_students):
            # Prompt the user for the student ID
            student_id = input("Enter student ID: ")

            # Write the student ID to the file
            file.write(f"{student_id}\n")
            
            # Write a dotted line after each student ID
            file.write("." * 5 + "\n")

    print("Registration complete. Student IDs written to reg_form.txt.")

# Get the number of students to register
num_students = int(input("Enter the number of students to register: "))

# Call the function to register students
register_students(num_students)