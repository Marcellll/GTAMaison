import sqlite3
from Enums.TypeTravail import *
from Enums.TypeBagdage import *
from datetime import datetime

def create_connection():
    return sqlite3.connect("Database/GTADB.db")

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

def is_Personne_logged_in(con:sqlite3.Connection, RFIDCard: str) -> bool:
    cursor = con.cursor()
    result = cursor.execute(f""" select count(*) from Badgage where RFIDCard = "{RFIDCard}" and Date = "{datetime.today().strftime("%d.%m.%Y")}" and TypeEntreeSortie = {TypeBadgage.ENTREE.value}""")
    for results in result:
        if results[0] == 1:
            return True
        else:
            return False

def is_Personne_logged_off(con:sqlite3.Connection, RFIDCard: str) -> bool:
    cursor = con.cursor()
    result = cursor.execute
    result = cursor.execute(f""" select count(*) from Badgage where RFIDCard = "{RFIDCard}" and Date = "{datetime.today().strftime("%d.%m.%Y")}" and TypeEntreeSortie = {TypeBadgage.SORTIE.value}""")
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

def get_Personne_TypeTravail(con: sqlite3.Connection, RFIDCard: str) -> TypeTravail:
    cursor = con.cursor()
    result = cursor.execute(f"""select EnumTypeTravail from Personnel
                                left join TypeTravail on Personnel.TypeTravail = TypeTravail.EnumTypeTravail
                                where RFIDCardID = "{RFIDCard}" """)
    for results in result:
        if results[0] == 1:
            return TypeTravail.HORRAIRE
        if results[0] == 2:
            return TypeTravail.JOURNEE
        else:
            return None

def get_badging_time(con:sqlite3.Connection, RFIDCard: str, EntreeSortie: TypeBadgage, date: str) -> str:
    cursor = con.cursor()
    result = cursor.execute(f""" select Horraire from Badgage where RFIDCard = {RFIDCard} and TypeEntreeSortie = {EntreeSortie} and Date = "{date}" """)
    for results in result:
        return results[0]

def get_10days_badging(con:sqlite3.Connection, RFIDCard: str) -> sqlite3.Cursor:
    cursor = con.cursor()
    return cursor.execute(f"""select Entree.Date,
                                    Entree.Horraire as "Horraire Entrée",
                                    Sortie.HorraireSortie as "Horraire Sortie",
                                    Personnel.Personne
                            from Badgage as Entree
                            left join Personnel on Entree.RFIDCard = Personnel.RFIDCardID
                            left join TypeTravail on Personnel.TypeTravail = TypeTravail.EnumTypeTravail
                            left join (select Badgage.Date as "DateSortie",
                                        Badgage.Horraire as "HorraireSortie",
                                        Personnel.Personne
                                        from Badgage
                                        left join Personnel on Badgage.RFIDCard = Personnel.RFIDCardID
                                        left join TypeTravail on Personnel.TypeTravail = TypeTravail.EnumTypeTravail
                                            where 
                                                strftime('%s', substr(Date, 7) || '-' || substr(Date, 4, 2) || '-' || substr(Date, 1, 2)) > strftime('%s', date('now', '-20 days'))
                                                and RFIDCard = "{RFIDCard}"
                                                and TypeEntreeSortie = 2) Sortie on Sortie.DateSortie = Entree.Date
                            where 
                                strftime('%s', substr(Date, 7) || '-' || substr(Date, 4, 2) || '-' || substr(Date, 1, 2)) > strftime('%s', date('now', '-20 days'))
                                and RFIDCard = "{RFIDCard}"
                                and TypeEntreeSortie = 1""")

if __name__ == "__main__":
    connection = create_connection()
    #create_new_employee(connection, "360976183797", "Marcel", TypeTravail.JOURNEE)
    result = get_10days_badging(connection, "384186254439").fetchall()
    for line in result:
        print(line)
    connection.close()
