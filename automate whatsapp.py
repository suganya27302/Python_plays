import pywhatkit as pw
import pyttsx3
import speech_recognition as sr
engine = pyttsx3.init()
listener =sr.Recognizer()
try:
    with sr.Microphone() as source:
        print("listening...")
        voice = listener.listen(source)
        cmd = listener.recognize_google(voice)
        engine.say(cmd)
        engine.runAndWait()
        print(cmd)
#pw.sendwhatmsg("+919750549966",'hii',16,20)
        pw.playonyt(cmd)
except:
    pass

# automate whatsapp msg and youtube