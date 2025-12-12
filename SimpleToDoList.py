"""
Simple To-Do List Application
Teaches: Lists, File Handling (Read/Write), CRUD(Create, Read, Update, Delete) Operations
"""
"""
RECIPE

1. Start the program
2. Check for existing tasks
    - Look for a file called tasks.txt.
    - If the file exists, open it and read each line as a task.
    - Remove any extra space or newlines from each task.
    - Store all tasks in a list in memory.
    - If the file does not exist, start with an empty list.
3. Show the main menu
    - View all tasks
    - Add a new task
    - Remove a task
    - Mark a task as complete
    - Search tasks
    - Clear all tasks
    - Exit the program
4. Ask the user to choose an option
5. Handle the user choice
    a) If user chooses “View all tasks”:
        - Show each task with a number.
        - If no tasks exist, tell the user the list is empty.

    b) If user chooses “Add a new task”:
        - Ask the user for the task description.
        - If the input is not empty, add it to the list.
        - Save all tasks to the file immediately.
      
    c) If user chooses “Remove a task”:
        - Show all tasks with numbers.
        - Ask the user which task number to remove.
        - If the number is valid, remove the task from the list.
        Save the updated list to the file.

    d) If user chooses “Mark a task as complete”:
        - Show all tasks with numbers.
        - Ask the user which task number to mark.
        - If the number is valid and task is not already marked, add a checkmark or symbol to the task.
        - Save the updated list.

    e) If user chooses “Search tasks”:
        - Ask the user for a keyword.
        - Look through all tasks and find any that contain the keyword.
        - Show the matching tasks with their numbers.
        - If no match, inform the user.
    
    f) If user chooses “Clear all tasks”:
        - Ask the user for confirmation before deleting everything.
        - If confirmed, remove all tasks from the list.
        - Save the empty list to the file.

    g) If user chooses “Exit”:
        - Save all tasks to the file one last time.
        - Thank the user and end the program.

6. Repeat the menu
    - After each action (except exit), show the menu again and ask for the next choice.

"""



import os  # For file operations to check if files exist on the computer

# File to store tasks
# TASKS_FILE is a constant variable (UPPERCASE by convention) where we will save tasks.
TASKS_FILE = "tasks.txt"

# ========== FILE HANDLING FUNCTIONS ==========
def load_tasks():               # Reading from File
    """Load tasks from file into a list"""
    tasks = []                  # Create an empty list to hold all our to do items.
    
    # Check if file exists
    if os.path.exists(TASKS_FILE):       # asks: "Does tasks.txt exist?"
        try:
            with open(TASKS_FILE, 'r') as file:     # Open and read the file
                # Read each line and add to tasks list
                for line in file:
                    task = line.strip()          # Remove whitespace/newlines
                    if task:                     # Ignore empty lines
                        tasks.append(task)       # Add the cleaned task to the list
            print(f"✓ Loaded {len(tasks)} task(s) from file.")
        except Exception as e:
            print(f"❌ Error loading tasks: {e}")
    else:
        print("📝 No existing tasks file found. Starting fresh!")
    
    return tasks


def save_tasks(tasks):           # Writing to File
    """Save tasks list to file"""
    try:
        with open(TASKS_FILE, 'w') as file:
            # Write each task on a new line
            for task in tasks:
                file.write(task + '\n')
        print("✓ Tasks saved successfully!")
        return True
    except Exception as e:
        print(f"❌ Error saving tasks: {e}")
        return False


# ========== TASK MANAGEMENT FUNCTIONS ==========
def display_tasks(tasks):
    """Display all tasks with numbers"""
    print("\n" + "="*50)
    print("           YOUR TO-DO LIST")
    print("="*50)
    
    if not tasks:  # If list is empty
        print("\n  📭 No tasks yet! Your list is empty.")
        print("     Add a task to get started!")
    else:
        print()
        for index, task in enumerate(tasks, start=1):
            # enumerate() gives us both index and value
            # start=1 makes numbering begin at 1 instead of 0
            print(f"  {index}. {task}")
    
    print("="*50)


def add_task(tasks):
    """Add a new task to the list"""
    print("\n--- Add New Task ---")
    task = input("Enter task description: ").strip()
    
    if task:  # Check if task is not empty
        tasks.append(task)  # Add to the end of the list
        print(f"✓ Added: '{task}'")
        save_tasks(tasks)  # Save to file immediately
    else:
        print("❌ Task cannot be empty!")


def remove_task(tasks):
    """Remove a task from the list"""
    if not tasks:
        print("\n❌ No tasks to remove!")
        return
    
    display_tasks(tasks)
    
    print("\n--- Remove Task ---")
    try:
        # Get task number from user
        task_num = int(input("Enter task number to remove: "))
        
        # Check if number is valid (1 to length of list)
        if 1 <= task_num <= len(tasks):
            # Convert to list index (subtract 1)
            index = task_num - 1
            removed_task = tasks.pop(index)  # Remove and return the task
            print(f"✓ Removed: '{removed_task}'")
            save_tasks(tasks)
        else:
            print(f"❌ Invalid number! Please choose 1-{len(tasks)}")
    
    except ValueError:
        print("❌ Please enter a valid number!")


def mark_complete(tasks):
    """Mark a task as completed (add ✓)"""
    if not tasks:
        print("\n❌ No tasks to mark as complete!")
        return
    
    display_tasks(tasks)
    
    print("\n--- Mark Task as Complete ---")
    try:
        task_num = int(input("Enter task number to mark complete: "))
        
        if 1 <= task_num <= len(tasks):
            index = task_num - 1
            
            # Check if already marked
            if "✓" not in tasks[index]:
                tasks[index] = "✓ " + tasks[index]  # Add checkmark
                print(f"✓ Marked complete: '{tasks[index]}'")
                save_tasks(tasks)
            else:
                print("⚠ Task is already marked as complete!")
        else:
            print(f"❌ Invalid number! Please choose 1-{len(tasks)}")
    
    except ValueError:
        print("❌ Please enter a valid number!")


def clear_all_tasks(tasks):
    """Clear all tasks from the list"""
    if not tasks:
        print("\n❌ No tasks to clear!")
        return
    
    print("\n--- Clear All Tasks ---")
    confirm = input(f"Are you sure you want to delete all {len(tasks)} task(s)? (yes/no): ")
    
    if confirm.lower() in ['yes', 'y']:
        tasks.clear()  # Remove all items from list
        save_tasks(tasks)
        print("✓ All tasks cleared!")
    else:
        print("⚠ Clear cancelled.")


def search_tasks(tasks):
    """Search for tasks containing a keyword"""
    if not tasks:
        print("\n❌ No tasks to search!")
        return
    
    print("\n--- Search Tasks ---")
    keyword = input("Enter search keyword: ").strip().lower()
    
    if not keyword:
        print("❌ Please enter a keyword!")
        return
    
    # Find matching tasks
    matches = []
    for index, task in enumerate(tasks, start=1):
        if keyword in task.lower():  # Case-insensitive search
            matches.append((index, task))
    
    if matches:
        print(f"\n✓ Found {len(matches)} matching task(s):")
        print("-"*50)
        for num, task in matches:
            print(f"  {num}. {task}")
    else:
        print(f"\n❌ No tasks found containing '{keyword}'")


# ========== MENU DISPLAY ==========
def display_menu():
    """Display the main menu"""
    print("\n" + "="*50)
    print("              MAIN MENU")
    print("="*50)
    print("  1. View All Tasks")
    print("  2. Add New Task")
    print("  3. Remove Task")
    print("  4. Mark Task as Complete")
    print("  5. Search Tasks")
    print("  6. Clear All Tasks")
    print("  7. Exit")
    print("="*50)


# ========== MAIN PROGRAM ==========
def main():
    """Main program loop"""
    print("\n" + "="*50)
    print("       WELCOME TO YOUR TO-DO LIST!")
    print("="*50)
    
    # Load tasks from file when program starts
    tasks = load_tasks()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-7): ").strip()
        
        if choice == '1':
            display_tasks(tasks)
        
        elif choice == '2':
            add_task(tasks)
        
        elif choice == '3':
            remove_task(tasks)
        
        elif choice == '4':
            mark_complete(tasks)
        
        elif choice == '5':
            search_tasks(tasks)
        
        elif choice == '6':
            clear_all_tasks(tasks)
        
        elif choice == '7':
            print("\n✓ Saving your tasks...")
            save_tasks(tasks)
            print("👋 Thank you for using To-Do List!")
            print("   Your tasks have been saved.\n")
            break
        
        else:
            print("\n❌ Invalid choice! Please enter 1-7.")
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()