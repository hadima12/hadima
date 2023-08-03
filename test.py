import pyttsx3 as pt
import os

pt.speak("hello my firends")
pt.speak("waths your name?")
name_user = input("you name:")
pt.speak("ok you name" + name_user)
pt.speak("Pick me a name.")
name_robut = input("my name:")
pt.speak("ok my name then" + name_robut)
pt.speak("Nice to meet you.")
while True:
    pt.speak("What can I do for us?")
    Request = input("Request:")
    if (Request == "tell a joke"):
        pt.spake("joke hahaha")
    if (Request == "web"):
        os.system("Amir.html")
    if (Request == "play game snake"):
        os.system("mar1.py")
    if (Request == "calculator"):
        os.system("mozik.py")
    if (Request == "play game dooz"):
        os.system("dooz.py")
    if (Request == "wikipedia"):
        os.system("wik.py")
