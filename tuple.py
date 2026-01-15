student = []

while True:
    print('---------------------------------------')
    print("-----Student Exam Data Management------")
    print('---------------------------------------')
    print('1. Add Student')
    print('2. View Student')
    print('3. Remove Student')
    print('4. Exit')
    print('---------------------------------------')

    choice = input('Enter your choice: ')
    print('---------------------------------------')

    # ADD STUDENT
    if choice == '1':
        name = input('Enter Student Name: ')
        roll_no = input('Enter Student Roll No: ')
        marks = input('Enter Student Marks: ')

        student.append((name, roll_no, marks))
        print('Student added successfully.')

    # VIEW STUDENT
    elif choice == '2':
        if not student:
            print('No student found.')
        else:
            print("Name\tRoll No\tMarks")
            for name, roll_no, marks in student:
                print(f'{name}\t{roll_no}\t{marks}')

    # REMOVE STUDENT
    elif choice == '3':
        roll = input('Enter Roll No to remove: ')
        found = False

        for s in student:
            if s[1] == roll:
                student.remove(s)
                found = True
                print('Student removed successfully.')
                break

        if not found:
            print('Student not found.')

    # EXIT
    elif choice == '4':
        print('Exiting program...')
        break

    else:
        print('Invalid choice. Please try again.')
