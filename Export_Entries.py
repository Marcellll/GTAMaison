import pandas
from DBHandler import *

def main():
    con = create_connection()
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
		where Badgage.Semaine = strftime('%W')-1""", con)
    db_df.to_csv(f"""export/export-S{int(datetime.today().strftime("%W"))-1}.csv""", index=False)
    con.close()
    
if __name__ == "__main__":
    main()
