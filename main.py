def to_do_list():

    tasks = []
    while True:
        print("1.add task")
        print("2.remove task")
        print("3.show tasks")
        print("4.quit")
        choice = input("enter your choice:")

        if choice == "1":
            task = input("enter task:")
            tasks.append(task)
        elif choice == "2":
            task = input("enter a task to remove")
            if task in tasks:
                    tasks.remove(task)
            else:
                 print("task not found")
        elif choice == "3":
             for task in tasks:
                  print("# "+ task)
        elif choice == "4":
             break
        else:
             print("incorrect input")

to_do_list()