from Personne import Personne

class Client(Personne):
    def __init__(self,name, surname, address, tel, gender,id_client, list_account):
        super().__init__(name,surname,address,tel,gender)
        self.id_client = id_client
        self.liste_comptes = list_account
        self.account = []

    #ajouter un compte
    def addAccount(self, list_account):
        self.account.append(list_account)

    #  consulter les transactions.
    def Consultation(self):
        if self.account:
            super().printPersonneInformation()