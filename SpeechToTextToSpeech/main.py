
import speech_recognition as sr
import pyttsx3

# Define initialization and Recognizer function.
engineText = pyttsx3.init()
engineSpeech = sr.Recognizer()

# Using Microphone function ind
with sr.Microphone() as source:
    print('Speak Anything: ')
    # Obtain the speech from the microphone
    audio = engineSpeech.listen(source)
    # Recognize the speech, there are seven recognizer function to recognize the speech.
    # I have used google recognizer. I could use ibm, wit, bing, sphinx, houndify, google_cloud.
    text = engineSpeech.recognize_google(audio)
    print('You said: {}'.format(text))
engineText.say(text)
engineText.runAndWait()