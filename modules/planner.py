TASK_FILE = "tasks.txt"

def add_task(task):
    with open(TASK_FILE, "a") as f:
        f.write(task + "\n")

def show_tasks():
    try:
        with open(TASK_FILE, "r") as f:
            print("\nYour Tasks:")
            for line in f:
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print("No tasks found.")