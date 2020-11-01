import random2
import tkinter
from PIL import ImageTk, Image

root = tkinter.Tk()
root.geometry('300x300')
root.title('Rolling Dice')

heading = tkinter.Label(root,text="The dice rolls to...", fg="red", bg="pink", font = "Arial 16 bold italic")
heading.pack()

dice = ['die1.png','die2.png','die3.png','die4.png','die5.png','die6.png']
diceim=ImageTk.PhotoImage(Image.open(random2.choice(dice)))

imlabel = tkinter.Label(root, image=diceim)
imlabel.image = diceim
imlabel.pack(expand=True)

def rolling():
    diceim=ImageTk.PhotoImage(Image.open(random2.choice(dice)))
    imlabel.configure(image=diceim)
    imlabel.image = diceim

button = tkinter.Button(root, text="Roll the Dice", command=rolling)
button.pack(expand=True)

root.mainloop()