import speech_recognition as sr
from googletrans import Translator
import pyttsx3

# Initialize speech recognition, translator, and text-to-speech engines
recognizer = sr.Recognizer()
translator = Translator()
text_to_speech = pyttsx3.init()

# Define a function to recognize and translate speech
def recognize_and_translate():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        user_input = recognizer.recognize_google(audio, language='te')  # Replace 'your-language' with your language code
        print(f"You said: {user_input}")

        # Translate the user input to English
        translation = translator.translate(user_input, src='te', dest='en')  # Replace 'your-language' with your language code
        print(f"Translation: {translation.text}\n")

        # Speak the translated text
        text_to_speech.say(translation.text)
        text_to_speech.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that.")
    except sr.RequestError as e:
        print("Could not request results. Check your internet connection.")
while True:
    recognize_and_translate()
