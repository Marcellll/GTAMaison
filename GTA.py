from tkinter import *
from enum import Enum

class TypeTravail(Enum):
    HORRAIRE = 1
    JOURNEE = 2

root = Tk()
root.title("Badgeuse")
root.attributes("-fullscreen", True)

def clickEntree():
    myLabel = Label(root, text = input.get())
    myLabel.pack()

input = Entry(root)
firstLabel = Button(root, text="Entrer le nom de la personne", command=clickEntree)
firstLabel.pack()
input.pack()

root.mainloop()

