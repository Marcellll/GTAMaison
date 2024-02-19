select Badgage.RFIDCard,
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