import pandas
import sqlite3
import DBHandler

def main():
    con = DBHandler.create_connection()
    db_df = pandas.read_sql_query("""select Badgage.RFIDCard,
	   Badgage.Semaine,
	   Badgage.Date,
	   Badgage.Horraire,
	   TypeEntreeSortie.EntreeSortie,
	   Personnel.Personne, 
	   TypeTravail.TypeTravail 
from Badgage
left join TypeEntreeSortie on Badgage.TypeEntreeSortie = TypeEntreeSortie.EnumTypeEntreeSortie
left join Personnel on Badgage.RFIDCard = Personnel.RFIDCardID
left join TypeTravail on Personnel.TypeTravail = TypeTravail.EnumTypeTravail
where Badgage.Semaine = strftime('%W')""", con)
    db_df.to_csv(f"export/export.csv", index=False)
    

if __name__ == "__main__":
    main()
