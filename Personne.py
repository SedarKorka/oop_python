class Personne:
    def __init__(self,name, surname, address, tel, gender):
        self.name = name
        self.surname = surname
        self.address = address
        self.tel = tel
        self.gender = gender

    #Print person Information
    def printPersonneInformation(self):
        if self.gender == "male":
            print(f"His name is {self.name} {self.surname}, his address is {self.address} and his phone number is {self.tel}.")
        else:
            print(f"Her name is {self.name} {self.surname}, her address is {self.address} and her phone number is {self.tel}.")

    # modifier les informations personnelles
    def editPersonInformation(self,name=None, surname=None, address=None, tel=None):
        if name:
            self.name = name
        elif surname:
            self.surname = surname
        elif address:
            self.address = address
        elif tel:
            self.tel = tel