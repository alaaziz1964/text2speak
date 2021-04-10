"""
this is for test my github repo
"""
import tkinter
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
f = open("text2speach.txt", "rt")
for line in f:
    engine.say(line)

engine.runAndWait()
engine.stop()