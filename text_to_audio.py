from gtts import gTTS
import os

# open() python function to open file
fh = open("objects_detected.txt", "r")
myText = fh.read().replace("\n", " ")
myText = "I see " + myText + " in front of us "

# language is english
language = 'en'

#gTTS is Google text to speech library, speech in english
output = gTTS(text=myText, lang=language, slow=False)

#output saved in mp3 file
output.save("objects_detected_audio.mp3")

# audio file opened and sent to speaker to be read ut loud
os.system("start objects_detected_audio.mp3")
