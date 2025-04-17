grades = {}

while True:
    print("\n1. Add/Update Grade\n2. Print All Grades\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        grades[name] = grade
        print(f"{name}'s grade is now {grade}.")
    elif choice == '2':
        for student, grade in grades.items():
            print(f"{student}: {grade}")
    elif choice == '3':
        break
    else:
        print("Invalid choice. Try again.")
