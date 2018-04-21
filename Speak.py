import pyaudio
import wave
import time

from pydub import AudioSegment
from pydub.playback import play

#define stream chunk   
chunk = 1024  

#list of stings to pass into Speak()
#open a wav format

def Speak(pList):
    pause = AudioSegment.from_wav(r"Phonetic Sounds v2/SPC.wav", "rb")
    letterPair = []
    for f in pList:
        print(f)
        #USES "SPC" for a space between words
        if f != 'SPC':
            letterPair.append(f)
        # print(letterPair, len(letterPair))
        if f == 'SPC':
            print("this is said:", letterPair)
            combined_word = AudioSegment.empty()
            # create dictionary of audio files
            for ph in letterPair:
                combined_word += AudioSegment.from_wav(r"Phonetic Sounds v2/" + ph + ".wav", "rb")

            play(combined_word)
            play(pause)

            letterPair.clear()

# public functions to access text to speech
def sayThis(list):
    Speak(list)

