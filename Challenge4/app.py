def to_do():
    tasks = []

    initPrompt = """
    Please select from the following options:\n
        1. Add Tasks\n
        2. Show Tasks\n
        3. Mark Task as Done\n
        4. Exit Program\n
    """
    
    while True:
        try:
            selection = int(input(initPrompt))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        match selection:
            case 1:
                try:
                    numberOfTasks = int(input("Indicate Number of Tasks: "))
                    for i in range(numberOfTasks):
                        task = input("Enter the task: ")
                        tasks.append({'task': task})
                        print("Task added!")
                except ValueError:
                    print("Invalid input for number of tasks.")

            case 2: 
                if not tasks:
                    print("No tasks to show.")
                else:
                    for index, task in enumerate(tasks):
                        print(f"{index + 1}. {task['task']}")
            
            case 3:
                if not tasks:
                    print("No tasks to mark as done.")
                    continue
                try:
                    task_index = int(input("Enter the task number marked as complete: "))
                    if 1 <= task_index <= len(tasks):
                        tasks.pop(task_index - 1)
                        print("Task removed!")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number.")

            case 4:
                print("Program terminated")
                break


if __name__ == "__main__":
    to_do()
