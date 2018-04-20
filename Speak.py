import pyaudio
import wave
import time

#define stream chunk   
chunk = 1024  

#list of stings to pass into Speak()
#open a wav format music
pList = ["R", "EY1", "D", "AA2", "R"]

def Speak(data):
    #data = []
    i = 0
    for f in pList:
        #USES "SPC" for a space between words
        if f == "SPC":
            time.sleep(.3)
            i += 1
        else:
            f = wave.open(r"PhoneticSoundsv2/" + pList[i] + ".wav","rb")

            #instantiate PyAudio
            p = pyaudio.PyAudio()
            #open stream
            stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                        channels = f.getnchannels(),
                        rate = f.getframerate(),
                        output = True)
            #read data
            data=f.readframes(chunk)
            i+= 1

            #play stream
            while data:
                stream.write(data)
                data = f.readframes(chunk)
    # stop stream
    stream.stop_stream()
    stream.close()

    # close PyAudio
    p.terminate()



#takes a list of strings
Speak(pList)
