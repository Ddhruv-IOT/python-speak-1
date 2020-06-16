import pyttsx3                            # importing pyttsx3
engine = pyttsx3.init()                   # setting voice engine - .init("sapi5") or leave it empty .init()
rate = engine.getProperty('rate')         # to get the current speech rate
engine.setProperty('rate',140)            # to set the rate
voices = engine.getProperty('voices')     # to get the current voice
engine.setProperty('voice',voices[1].id)  # to set the voice 0-male 1-female
engine.say("hii there!")                  # write the message here you want pyttsx3 to speak
engine.runAndWait()                       # dont forget to add this other the code will not run
