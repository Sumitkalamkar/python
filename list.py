task =[]

while True:

    print("\n------TO-DO-LIST------\n")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")


    choice=input("Enter choice: ")

    if choice=='1':

      new_task = input("Enter Task:")
      task.append(new_task)
      print("Task added successfully.")

    elif choice=='2':

      if not task:
            print("No tasks found.")

      else:
            for i, item in enumerate(task):

                print(f'{i+1}.{item}')

    elif choice=='3':

        if not task:
            print('No tasks found.')
        else:
            task_index=int(input('Enter a index of the task:'))
            # Check if index is valid
            if 0 <= task_index - 1 < len(task):
                removed_task = task.pop(task_index-1)
                print(f"'{removed_task}' is removed successfully.")
            else:
                print("Invalid task index.")

    elif choice=='4':
          print("Exiting the program, Thank You.")
          break
