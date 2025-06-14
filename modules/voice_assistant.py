import speech_recognition as sr
import pyaudio
from modules.tts_engine import speak

recognizer=sr.Recognizer()

def listen_command():
  with sr.Microphone() as source:
    print("Listening....")
    recognizer.adjust_for_ambient_noise(source,duration=1)
    audio=recognizer.listen(source)
    try:
      command=recognizer.recognize_google(audio)
      print("You said:",command)
      return command.lower()
    except sr.UnknownValueError:
      speak("Sorry,I didn't understand that.")
      return ""
    except sr.RequestError:
      speak("Sorry,my speech service is not available right now.")
      return ""

