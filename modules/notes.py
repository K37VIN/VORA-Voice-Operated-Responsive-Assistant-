NOTES_FILE = "notes.txt"

def add_note(note):
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")

def show_notes():
    try:
        with open(NOTES_FILE, "r") as f:
            print("\nYour Notes:")
            for line in f:
                print(f"- {line.strip()}")
    except FileNotFoundError:
        print("No notes found.")