import pyttsx3  # Built-in module to read text


def audio(text):
    speaker = pyttsx3.init()
    voices = speaker.getProperty('voices')
    speaker.setProperty('voice', voices[3].id)
    speaker.setProperty('rate', 150)
    speaker.say(text)
    speaker.save_to_file(text, 'CTS2.wav')
    speaker.runAndWait()

# To print the list of voices:
# voices = speaker.getProperty('voices')
# for voice in voices:
#   print(f'{voice}')
