def parse_command(command):
    command = command.lower()
    if "notepad" in command:
        return "open_notepad"
    elif "chrome" in command:
        return "open_chrome"
    elif "email" in command:
        return "send_email"
    elif "whatsapp" in command:
        return "send_whatsapp"
    elif "lock" in command:
        return "lock_system"
    elif "shutdown" in command:
        return "shutdown"
    elif "restart" in command:
        return "restart"
    elif "search google" in command:
        return "google_search"
    elif "youtube" in command:
        return "youtube_search"
    elif "weather" in command:
        return "get_weather"
    elif "note" in command:
        return "add_note"
    elif "show notes" in command:
        return "show_notes"
    elif "task" in command:
        return "add_task"
    elif "show tasks" in command:
        return "show_tasks"
    elif "exit" in command:
        return "exit"
    else:
        return "unknown"