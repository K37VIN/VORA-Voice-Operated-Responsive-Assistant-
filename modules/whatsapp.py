import pywhatkit 

def send_whatsapp(number,message):
  try:
    pywhatkit.sendwhatmsg_instantly(number,message)
  except Exception as e:
    print(f"Error:{e}")