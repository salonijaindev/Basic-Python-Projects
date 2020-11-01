from tkinter import *
from playsound import playsound
from gtts import gTTS

root = Tk()
root.geometry('350x300')
root.configure(bg='ghost white')
root.title("Text-to-Speech")

Label(root,text="Text-to-Speech Converter",font='arial 20 bold', bg='white smoke').pack()
msg = StringVar()
Label(root,text="Enter text", font='arial 15 bold', bg='white smoke').place(x=20,y=60)
blank = Entry(root,textvariable = msg,width='50')
blank.place(x=20,y=100)

def tts():
    msg=blank.get()
    speech=gTTS(text = msg)
    speech.save('tts.mp3')
    playsound('tts.mp3')

def Exit():
    root.destroy()

def Reset():
    msg.set("")

Button(root, text = "PLAY", font = 'arial 15 bold' , command = tts ,width = '4').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

root.mainloop()