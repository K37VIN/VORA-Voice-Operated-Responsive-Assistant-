import webbrowser

def search_google(query):
  webbrowser.open(f"https://www.google.com/search?q={query}")

def search_youtube(query):
  webbrowser.open(f"https://www.youtube.com/results?search_query={query}")