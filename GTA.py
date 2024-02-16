from tkinter import *
from DBHandler import *
import sys
from TypeTravail import *

root = Tk()
root.title("Badgeuse")
root.attributes("-fullscreen", True)

def clickExit():
    sys.exit()

def adminView():
    adminPage = Toplevel(root)
    adminPage.title("Vue administrateur")
    adminPage.geometry("500x300")
    radioButtonVariable = IntVar()
    horraireEmploye = Radiobutton(adminPage, text="Horraire", variable=radioButtonVariable, value=TypeTravail.HORRAIRE.value).pack() 
    journeeEmploye = Radiobutton(adminPage, text="Journée", variable=radioButtonVariable, value=TypeTravail.JOURNEE.value).pack()
    #TODO: Mettre la lecture du badge ici
    ajoutNouvelEmployeButton = Button(adminPage, text = "Ajouter une nouvel employé",padx=200, pady = 50, 
                                       command=lambda: create_new_employee(create_connection(),,, radioButtonVariable.get())).pack()
    
entreeButton = Button(root, text="Entrée", padx = (root.winfo_screenwidth() * 0.15), pady = (root.winfo_screenheight() * 0.2),bg="green")
sortieButton = Button(root, text="Sortie", padx = (root.winfo_screenwidth() * 0.15), pady = (root.winfo_screenheight() * 0.2), bg="red")
exitButton = Button(root, text="Quitter", command=clickExit)
adminButton = Button(root, text="Admin", command=adminView)

exitButton.pack(side = 'bottom')
adminButton.pack(side="bottom")
entreeButton.pack(side = "left")
sortieButton.pack(side = "right")

root.mainloop()

