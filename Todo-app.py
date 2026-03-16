def load_tasks():
    tasks = []
    try:
        with open("tasks.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    tasks.append(line)
    except FileNotFoundError:
        pass
        
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet! Add one first.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    print()
 
def add_task(tasks):
    task = input("Enter your task: ").strip()
    if task:
        tasks.append("[ ] " + task)
        save_tasks(tasks)
        print("Task added successfully!")
    else:
        print("Task cannot be empty!")
       

def mark_done(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            # Swaps the empty brackets for [DONE]
            tasks[num - 1] = tasks[num - 1].replace("[ ]", "[DONE]")
            save_tasks(tasks)
            print("Task marked as done!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")       

def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            # .pop() removes the item and returns it so we can print it
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a number.")                    

def main():
    tasks = load_tasks()
    while True:   
        print("\n====== MY TO-DO APP ======")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1 to 5.")
            

main()     