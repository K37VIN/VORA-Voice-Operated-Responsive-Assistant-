import os
import ctypes

def lock_system():
  ctypes.windll.user32.LockWorkStation()
def shutdown():
  os.system("shutdown /s /t 1")
def restart():
  os.system("shutdown /r /t 1")
  