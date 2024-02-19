import sqlite3
from Enums.TypeTravail import *
from Enums.TypeBagdage import *
from datetime import datetime

def create_connection():
    return sqlite3.connect("Database\\GTADB")

def create_new_employee(con: sqlite3.Connection, RFIDCardID: str, Personne: str, TypeTravail: TypeTravail):
    cursor = con.cursor()
    cursor.execute(f"""Insert into Personnel (RFIDCardID, Personne, TypeTravail) values ({RFIDCardID}, "{Personne}", {TypeTravail.value}) """)
    con.commit()

def create_new_employee(con: sqlite3.Connection, RFIDCardID: str, Personne: str, TypeTravail: int):
    cursor = con.cursor()
    cursor.execute(f"""Insert into Personnel (RFIDCardID, Personne, TypeTravail) values ({RFIDCardID}, "{Personne}", {TypeTravail}) """)
    con.commit()

def update_employee_card(con: sqlite3.Connection, RFIDCardID: str, Personne: str, TypeTravail: TypeTravail):
    cursor = con.cursor()
    cursor.execute(f"""UPDATE Personnel set Personne = "{Personne}", TypeTravail = {TypeTravail.value} where RFIDCardID = {RFIDCardID}""")
    cursor.commit()

def get_all_employees(con: sqlite3.Connection) -> sqlite3.Cursor:
    cursor = con.cursor()
    return cursor.execute("""Select * from Personnel""")

def create_new_badge_entry(con: sqlite3.Connection, RFIDCardID: str, TypeEntreeSortie: TypeBadgage):
    cursor = con.cursor()
    cursor.execute(f"""Insert into Badgage (RFIDCard, Semaine, Date, Horraire, TypeEntreeSortie)
                   values ({RFIDCardID}, {datetime.today().strftime("%W")}, "{datetime.today().strftime("%d.%m.%Y")}", "{datetime.today().strftime("%H:%M:%S")}", {TypeEntreeSortie.value}) """)
    con.commit()

def create_new_badge_entry(con: sqlite3.Connection, RFIDCardID: str, TypeEntreeSortie: int):
    cursor = con.cursor()
    cursor.execute(f"""Insert into Badgage (RFIDCard, Semaine, Date, Horraire, TypeEntreeSortie)
                   values ({RFIDCardID}, {datetime.today().strftime("%W")}, "{datetime.today().strftime("%d.%m.%Y")}", "{datetime.today().strftime("%H:%M:%S")}", {TypeEntreeSortie}) """)
    con.commit()

def create_new_badge_entry(con: sqlite3.Connection, RFIDCardID: str, Semaine: int, Date: str, Heure: str, TypeEntreeSortie: TypeBadgage):
    cursor = con.cursor()
    cursor.execute(f"""Insert into Badgage (RFIDCard, Semaine, Date, Horraire, TypeEntreeSortie)
                   values ({RFIDCardID}, {Semaine}, "{Date}", "{Heure}", {TypeEntreeSortie.value}) """)
    con.commit()

def create_new_badge_entry(con: sqlite3.Connection, RFIDCardID: str, Semaine: int, Date: str, Heure: str, TypeEntreeSortie: int):
    cursor = con.cursor()
    cursor.execute(f"""Insert into Badgage (RFIDCard, Semaine, Date, Horraire, TypeEntreeSortie)
                   values ({RFIDCardID}, {Semaine}, "{Date}", "{Heure}", {TypeEntreeSortie}) """)
    con.commit()

def get_all_entries(con: sqlite3.Connection) -> sqlite3.Cursor:
    cursor = con.cursor()
    return cursor.execute("""select Badgage.RFIDCard,
	                            Badgage.Semaine,
	                            Badgage.Date,
	                            Badgage.Horraire,
	                            TypeEntreeSortie.EntreeSortie,
	                            Personnel.Personne, 
	                            TypeTravail.TypeTravail 
                            from Badgage
                            left join TypeEntreeSortie on Badgage.TypeEntreeSortie = TypeEntreeSortie.EnumTypeEntreeSortie
                            left join Personnel on Badgage.RFIDCard = Personnel.RFIDCardID
                            left join TypeTravail on Personnel.TypeTravail = TypeTravail.EnumTypeTravail""")

def is_RFID_used(con: sqlite3.Connection, RFIDCard: str) -> bool:
    cursor = con.cursor()
    result = cursor.execute(f"""select count(*) from Personnel where RFIDCardID = "{RFIDCard}" """)
    for results in result:
        if results[0] == 1:
            return True
        else:
            return False

def get_Personne(con: sqlite3.Connection, RFIDCard: str) -> str:
    cursor = con.cursor()
    result = cursor.execute(f"""select Personne from Personnel where RFIDCardID = "{RFIDCard}" """)
    for results in result:
        return results[0]

if __name__ == "__main__":
    connection = create_connection()
    #create_new_badge_entry(connection, "360976183797", TypeBadgage.SORTIE)
    result = get_Personne(connection, 360976183797)
    print(result)
    #for results in result:
        #print(result)
    connection.close()
