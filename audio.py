import pyttsx3  # Built-in module to read text

def audio(text):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()

