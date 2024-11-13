
from operations import add_task, view_tasks, delete_task
from utility import read_input

def display_menu():
    print("To-Do List App")
    print("a. Add a new to-do list")
    print("b. View all to-do list")
    print("c. Delete an list by its index")
    print("d. Exit")

def main():
    while True:  
        display_menu() 
        choice = read_input("Choose an option : ")  

        if choice == 'a':
            task = read_input("Enter the new task: ") 
            add_task(task)  
            print("Task added")
        elif choice == 'b':
            tasks = view_tasks()  
            if tasks:
                print("Your to-do list:")
                for index, task in enumerate(tasks):
                    print(f"{index + 1}. {task}")  
            else:
                print("No tasks available.")
        elif choice == 'c':
            tasks = view_tasks()  
            if tasks:
                index = int(read_input("Enter the index of the task to delete: ")) - 1  
                deleted_task = delete_task(index)  
                if deleted_task is not None:
                    print(f"Deleted task: {deleted_task}")
                else:
                    print("Invalid index. Please try again.")
            else:
                print("No tasks available to delete.")
        elif choice == 'd':
            print("over and out")
            break  
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
