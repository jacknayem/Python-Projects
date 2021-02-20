# The gtts or Google Text to Speech module is a online base simulating module, which is
# simulate the human speech during Text to Speech conversion.
from gtts import gTTS
# the os or Operating System module have been using to communicate with system.
import os

# Assigning my speech
myText = "I know your identity"

# The gTTS function is takes more parameters, But I have used here only three parameters. The first
# parameter contains text to read, 'lang' used to select language and 'slow' parameter is to read the
# text more slowly. There are 60 different language to assign 'lang' parameter's variable.
output = gTTS(myText, lang='en', slow='false')
# output = gTTS('bonjour', lang='fr')

# Using save() function we just save the converted speech into mp3 format.
output.save('test.mp3')
# system function is called to play that save audio file defined by path.
os.system('start test.mp3')

