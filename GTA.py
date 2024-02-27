from tkinter import *
from DBHandler import *
import sys
from Enums.TypeTravail import *
from Enums.TypeBagdage import *
import time
from RFID_read import *

root = Tk()
root.title("Badgeuse")
root.attributes("-fullscreen", True)
infoText = StringVar()
infoLabel = Label(root, textvariable=infoText, font=("Verdana", 25), wraplength = root.winfo_screenwidth()).pack()

def get_RFID_reading():
    infoText.set("Lecture du badge en attente...")
    (RFIDCardID, RFIDCardName) = get_reading()
    return str(RFIDCardID)

def clickExit():
    root.quit()

def clickSortie():
    semaineActuel = datetime.today().strftime("%W")
    dateActuel = datetime.today().strftime("%d.%m.%Y")
    heureActuel = datetime.today().strftime("%H:%M:%S")
    RFIDCardActuel = get_RFID_reading()
    con = create_connection()
    if is_RFID_used(con, RFIDCardActuel): 
        if not(get_Personne_TypeTravail(con, RFIDCardActuel) == TypeTravail.JOURNEE): 
            if not(is_Personne_logged_off(con, RFIDCardActuel)):
                create_new_badge_entry(con, RFIDCardActuel, semaineActuel, dateActuel, heureActuel, TypeBadgage.SORTIE.value)
                infoText.set(f"{get_Personne(con, RFIDCardActuel)} a badgé sa sortie le {dateActuel} à {heureActuel}. Bonne journée !")
            else:
                infoText.set(f"Vous avez déjà badgé votre sortie !")
        else:
            infoText.set(f"Vous n'avez pas besoin de badger votre sortie")
    else:
        infoText.set(f"Votre badge n'est pas enregistré, veuillez contacter Solène Dalmar")

def clickEntree():
    semaineActuel = datetime.today().strftime("%W")
    dateActuel = datetime.today().strftime("%d.%m.%Y")
    heureActuel = datetime.today().strftime("%H:%M:%S")
    RFIDCardActuel = get_RFID_reading()
    con = create_connection()
    if is_RFID_used(con, RFIDCardActuel):  
        if not(is_Personne_logged_in(con, RFIDCardActuel)):
            create_new_badge_entry(con, RFIDCardActuel, semaineActuel, dateActuel, heureActuel, TypeBadgage.ENTREE.value)
            infoText.set(f"{get_Personne(con, RFIDCardActuel)} a badgé son entrée le {dateActuel} à {heureActuel}. Merci !")
        else:
            infoText.set(f"Vous avez déjà badgé votre entrée !")
    else:
        infoText.set(f"Votre badge n'est pas enregistré, veuillez contacter Solène Dalmar")

def adminView():
    adminPage = Toplevel(root)
    adminPage.title("Vue administrateur")
    adminPage.geometry("500x300")
    radioButtonVariable = IntVar()
    horraireEmploye = Radiobutton(adminPage, text="Horraire", variable=radioButtonVariable, value=TypeTravail.HORRAIRE.value).pack() 
    journeeEmploye = Radiobutton(adminPage, text="Journée", variable=radioButtonVariable, value=TypeTravail.JOURNEE.value).pack()
    inputText = Entry(adminPage).pack()
    #TODO: Mettre la lecture du badge ici
    #ajoutNouvelEmployeButton = Button(adminPage, text = "Ajouter une nouvel employé",padx=200, pady = 50, 
                                       #command=lambda: create_new_employee(create_connection(),,, radioButtonVariable.get())).pack()
    
entreeButton = Button(root, text="Entrée", padx = (root.winfo_screenwidth() * 0.15), pady = (root.winfo_screenheight() * 0.2),bg="green", font = ("Verdana", 30), fg = "#FFFFFF", command=clickEntree)
sortieButton = Button(root, text="Sortie", padx = (root.winfo_screenwidth() * 0.15), pady = (root.winfo_screenheight() * 0.2), bg="red", font = ("Verdana", 30), fg = "#FFFFFF", command=clickSortie)
exitButton = Button(root, text="Quitter", command=clickExit)
adminButton = Button(root, text="Admin", command=adminView)

exitButton.pack(side = 'bottom')
adminButton.pack(side="bottom")
entreeButton.pack(side = "left")
sortieButton.pack(side = "right")

root.mainloop()

