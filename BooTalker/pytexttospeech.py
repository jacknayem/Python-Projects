# The pyttsx3 or python text to speech version 3 is a offline based speech simulation module.
import pyttsx3

myText = "Hello I know your Identity"
# The init() function initialize Text-to-Speech engine
engine = pyttsx3.init()

# The getProperty function use to get number details about current speaking rate,volume(min = 0
# and max=1) and voices(Male or Female). On the other hand, the setProperty() use to set the value
# for speaking rate, the value of voice and assign the gender.
rate = engine.getProperty('rate')
print(rate)
engine.setProperty('rate', 150)

volume = engine.getProperty('volume')
print(volume)
engine.setProperty('volume', 0.8)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# say() function use to convert the Text to Speech
engine.say(myText)

# Save the voice to a mp3 file
engine.save_to_file(myText, 'test.mp3')
# To play the speech, the runAndWait() function has been used.
engine.runAndWait()


