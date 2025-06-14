import os 
import subprocess

def open_notepad():
  subprocess.Popen(["notepad.exe"])

def open_chrome():
  path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
  os.startfile(path)