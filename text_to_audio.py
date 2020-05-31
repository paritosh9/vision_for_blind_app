from gtts import gTTS
import os
import time

count = 0
while True:
    if count == 0:

        myText = "Please give me few seconds to get started"

        # language is english
        language = 'en'

        # gTTS is Google text to speech library, speech in english
        output = gTTS(text=myText, lang=language, slow=False)

        # output saved in mp3 file
        output.save("objects_detected_audio.mp3")

        # audio file opened and sent to speaker to be read out loud
        os.system("start objects_detected_audio.mp3")

        count = count + 1
        time.sleep(6)

    time.sleep(4)
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

    # audio file opened and sent to speaker to be read out loud
    os.system("start objects_detected_audio.mp3")

