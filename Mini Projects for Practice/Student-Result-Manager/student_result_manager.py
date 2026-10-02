# Student Manager App
student = {}

while True:
    print("\n----- STUDENT MANAGER APP ---------")
    print("1. Add Student")
    print("2. View Students Dashboard")
    print("3. Check Result")
    print("4. Exit")

    choice = input("Enter Your Choice: ")

    # Add Student
    if choice == "1":
        name = input("Enter Student Name: ").strip()
        if not name:
            print("⚠️ Please enter a valid name!")
            continue
        try:
            marks = int(input("Enter Marks (0-100): "))
            if marks < 0 or marks > 100:
                print("⚠️ Invalid Marks! Must be between 0 and 100.")
                continue
        except ValueError:
            print("⚠️ Marks must be a number!")
            continue

        student[name] = marks
        print(f"✅ {name} successfully added!")

    # View Students
    elif choice == "2":
        if not student:
            print("⚠️ No Student Found!")
        else:
            print("\n------- Student Dashboard ---------")
            for name, marks in student.items():
                print(f"{name} : {marks}")

    # Check Result
    elif choice == "3":
        if not student:
            print("⚠️ Student Data is Empty!")
        else:
            print("\n------- Student's Name List ---------")
            for name in student.keys():
                print(name)
            name = input("Enter Student Name: ").strip()
            if name in student:
                marks = student[name]
                print("\n --- Result ----")
                print("PASS ✅" if marks >= 40 else "FAIL ❌")
            else:
                print("⚠️ Student Not Found!")

    # Exit
    elif choice == "4":
        print("👋 Exiting... Goodbye!")
        break

    else:
        print("⚠️ Invalid Input! Please choose 1-4.")
