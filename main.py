from modules.command_parser import parse_command
from modules import open_apps,send_email,whatsapp,system_control,webbrowser,notes,planner,get_weather
from modules.voice_assistant import listen_command
from modules.tts_engine import speak


def main():
  speak("Hello Devayush,I am vora,how may I help you:")
  while True:
    command=listen_command()
    action=parse_command(command)

    if action == "open_notepad":
      open_apps.open_notepad()
    elif action == "open_chrome":
      open_apps.open_chrome()
    elif  action =="send_email":
      speak("Please provide the recipient email, the subject and the content of the mail")
      to=input("To:")
      subject=input("Subject:")
      body=input("Body:")
      send_email.send_email(to,subject,body)
    elif action == "send_whatsapp":
      speak("Please provide the recipient whatsapp number and the content of the message")
      number=int(input("Number:"))
      message=input("Message:")
      whatsapp.send_message(number,message)
    elif action == "lock_system":
      system_control.lock_system()
    elif action == "shutdown":
      system_control.shutdown()
    elif action == "restart":
      system_control.restart()
    elif action == "google_search":
      speak("What do you want to search?")
      query = input("Search Query: ")
      webbrowser.search_google(query)
    elif action == "youtube_search":
      speak("What do you want to watch?")
      query = input("YouTube Query: ")
      webbrowser.search_youtube(query)
    elif action == "get_weather":
      city = input("Enter city name: ")
      get_weather.get_weather(city)
    elif action == "add_note":
      note = input("Enter note: ")
      notes.add_note(note)
    elif action == "show_notes":
      notes.show_notes()
    elif action == "add_task":
      task = input("Enter task: ")
      planner.add_task(task)
    elif action == "show_tasks":
      planner.show_tasks()
    elif action == "exit":
      speak("Goodbye!")
      break
    else:
      speak("I didn't understand that.I'm sorry")
  

if __name__=="__main__":
  main()