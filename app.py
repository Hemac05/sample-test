import json
import os

# Task file name
FILE_NAME = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(FILE_NAME):
        file = open(FILE_NAME, "r")
        tasks = json.load(file)
        file.close()
        return tasks
    else:
        return []

# Save tasks to file
def save_tasks(tasks):
    file = open(FILE_NAME, "w")
    json.dump(tasks, file, indent=4)
    file.close()

# View all tasks
def view_tasks(tasks):
    print("\n--- My Tasks ---")
    if len(tasks) == 0:
        print("No tasks found!")
    else:
        for i in range(len(tasks)):
            task = tasks[i]
            if task["status"] == "done":
                mark = "[DONE]"
            else:
                mark = "[    ]"
            print(str(i + 1) + ". " + mark + " " + task["name"])
    print("----------------\n")

# Add new task
def add_task(tasks):
    name = input("Enter task name: ")
    if name == "":
        print("Please enter a task name!")
        return
    new_task = {
        "name": name,
        "status": "not done"
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print("Task added successfully!")

# Mark task as done
def mark_done(tasks):
    if len(tasks) == 0:
        print("No tasks available!")
        return
    view_tasks(tasks)
    number = input("Enter task number: ")
    if number.isdigit() == False:
        print("Please enter a valid number!")
        return
    number = int(number)
    if number < 1 or number > len(tasks):
        print("Task not found!")
        return
    index = number - 1
    tasks[index]["status"] = "done"
    save_tasks(tasks)
    print("Task marked as done!")

# Delete a task
def delete_task(tasks):
    if len(tasks) == 0:
        print("No tasks to delete!")
        return
    view_tasks(tasks)
    number = input("Enter task number to delete: ")
    if number.isdigit() == False:
        print("Please enter a valid number!")
        return
    number = int(number)
    if number < 1 or number > len(tasks):
        print("Task not found!")
        return
    index = number - 1
    task_name = tasks[index]["name"]
    tasks.pop(index)
    save_tasks(tasks)
    print(task_name + " deleted!")

# ---- Main Program Starts Here ----

tasks = load_tasks()

while True:
    print("===== TO DO APP =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark as Done")
    print("4. Delete Task")
    print("5. Exit")
    print("=====================")

    choice = input("Choose (1-5): ")

    if choice == "1":
        view_tasks(tasks)
    elif choice == "2":
        add_task(tasks)
    elif choice == "3":
        mark_done(tasks)
    elif choice == "4":
        delete_task(tasks)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Wrong choice! Try again.")