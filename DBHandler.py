import sqlite3
from TypeTravail import *

def create_connection():
    return sqlite3.connect("GTADB")

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

if __name__ == "__main__":
    connection = create_connection()
    result = get_all_employees(connection)
    for results in result:
        print(f"RFID Card utilisée  {results[1]} pour l'utilisateur {results[2]}")
    connection.close()
