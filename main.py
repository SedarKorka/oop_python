from Personne import Personne
from client import Client


print(Client)
person =  Client("Korka","Diallo","Dippach","+352 661 117 437","male",1,10)

person.printPersonneInformation()

person.editPersonInformation("Mamadou Korka","Diallo","Dippach","+352 661 117 437")

person.printPersonneInformation()