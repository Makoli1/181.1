from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess

root=Tk()
root.geometry("400x400")
root.config(bg="lightgreen")

label_1=Label(root,text="Bienvenido a tu asistente personal")
label_1.place(relx=0.5,rely=0.1,anchor=CENTER)


text_to_speech=pyttsx3.init()
def speak (audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait() 

def b ():
    speech_recognisor=sr.Recognizer()
    
    with sr.Microphone() as source:
        audio = speech_recognisor.listen(source)
        speak("Como puedo ayudarte")
        voice_data=''
        try:
            voice_data=  speech_recognisor.recognize_google(audio, language='es-mx')
        except sr.UnknownValueError:
            print('Por favor, repite. No entendí tu solicitud')
            
    print(voice_data)
    respond(voice_data)

def respond(voice_data):
    if "nombre" in voice_data:
        speak("Mi nombre es Cortana")
        print("Mi nombre es cortana")
        
    if "hora" in voice_data:
        speak("La hora es")
        print("La hora es")
        var3=datetime.now()
        var4=var3.strftime("%H:%M:%S:")
        speak(var4)
        print(var4)
    if "navegador" in voice_data:
        speak("Abriendo google")
        print("Se esta abriendo google")
        webbrowser.get().open("https://www.google.com/")
    if "videos" in voice_data:
        print("Se esta abriendo youtube")
        speak("Abriendo youtube")
        webbrowser.get().open("https://www.youtube.com/")
        
    
    
button_1=Button(root,text="Iniciar",command=b)
button_1.place(relx=0.5,rely=0.2,anchor=CENTER)

root.mainloop()
