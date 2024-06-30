def task():
    tasks = [] #emty list
    print(".....Tasks Managenet System.....")

    total_tasks = int(input("How many tasks you want you add = "))
    for i in range(1, total_tasks+1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
    
    print(f"Todays tasks are \n {tasks}")

    while True:
        operation = int(input("Enter \n 1-Add \n 2-Update \n 3-Delete \n 4-View \n 5-Exit"))
        if operation == 1:
            add = input("Enter the new task = ")
            tasks.append(add)
            print(f"Task {add} has been added successfully")

        elif operation == 2:
            update_val = input("Enter the task name that want to update = ")
            if update_val in tasks:
                up = input("Enter new task = ")
                ind = tasks.index(update_val)
                tasks[ind] = up
                print("Updated task {up}")
        
        elif operation == 3:
            del_val = input("Enter the task that you want delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"The {del_val} task has been deleted")
        
        elif operation == 4:
            print(f"Total tasks are = {tasks} ")


        elif operation == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid Input")

task()