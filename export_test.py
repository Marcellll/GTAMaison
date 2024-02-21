import pandas
import sqlite3

def main():
    con = sqlite3.connect("Database\\GTADB.sqlite3")
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
left join TypeTravail on Personnel.TypeTravail = TypeTravail.EnumTypeTravail""", con)
    db_df.to_csv(f".\export\export.csv", index=False)

#def send_per_mail():
    

if __name__ == "__main__":
    main()
    #send_per_mail()