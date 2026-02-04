# Créer une classe CompteBancaire avec les
# attributs privés, numéro de compte, nom,
# prénom et solde. Cette classe doit posséder
# les méthodes suivantes :

# ➔ afficher : qui affiche le détail sur le compte.
# ➔ afficherSolde : cette méthode affiche dans le terminal le solde du
# client.
# ➔ versement : cette méthode prend un paramètre le montant du
# versement et ajoute celui-ci au solde du client.
# ➔ retrait : cette méthode prend un entier en argument (le montant à
# retirer), enlève ce montant au solde du compte et affiche le nouveau
# solde.

# Veillez à ce que le compte possède bien le montant disponible sinon un
# message d’erreur est affiché.

# Créez un compte avec les valeurs de construction de votre choix et faites
# appel aux différentes méthodes afin de vérifier que tout fonctionne
# correctement.

# Ajoutez l’attribut découvert à votre classe CompteBancaire, cet attribut aura
# pour valeur un booléen. Si le client a le droit à un découvert, la valeur de cet
# attribut sera True et des opérations pourront être effectuées même si le solde
# est de zéro (méthode retrait).

# Ajouter les méthodes suivantes :
# ➔ agios : cette méthode permet d’appliquer des agios au solde du
# compte si celui-ci est négatif.
# ➔ virement : cette méthode prend en paramètre une référence, un
# compte bancaire (celui qui reçoit l’argent) et un montant. Un message
# de confirmation ou d'erreur doit être affiché.

# Créez une deuxième instance de la classe CompteBancaire. Ce deuxième
# compte doit être à découvert (solde négatif). Faire un versement du premier
# compte vers celui à découvert afin de le remettre à zéro.

class BankAccount() : 
    def __init__(self, id, first_name, last_name, balance, overdraft): 
        self.__id = id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance
        self.__overdraft = overdraft

    def show_details(self) : 
        print(f"ID : {self.__id}")
        print(f"Owner first name : {self.__first_name}")
        print(f"Owner last name : {self.__last_name}")

    def get_balance(self) : 
        return self.__balance
    def set_balance(self, new_amount) : 
        self.__balance = new_amount
    def show_balance(self):
        print(f"Account n°{self.__id} balance : {self.__balance}€")
    
    def deposit(self, ammount) :
        try : 
            self.__balance += ammount
            print(f"{ammount} € have been added to the account n°{self.__id}")
            self.show_balance()
        except TypeError : 
            print("Ammount must represent money : use a positive int or float")

    def withdrawal(self, ammount) : 
        try : 
            if self.__balance - ammount >= 0 and self.__overdraft == False or self.__overdraft == True : 
                self.__balance -= ammount
                print(f"{ammount} € have been withdrawed from the account n°{self.__id}")
                self.show_balance()
            else : 
                print(f"You wish to withdraw {ammount}€ but your balance is {self.__balance}€, insufficient funds")
        except TypeError : 
            print("Ammount must represent money : use a positive int or float")
    
    def penalty(self) : 
        if self.__balance < 0 : 
            self.__balance *= 1.01 
            print("You've spend too much time in overdraft. 1% penalty has been applied")
            self.show_balance()
            
    def transfer(self, other, ammount) : 
        try : 
            if self.__balance - ammount >= 0 and self.__overdraft == False or self.__overdraft == True : 
                self.__balance -= ammount
                other.set_balance(other.get_balance() + ammount)
                print(f"{ammount} € have been withdrawed from the account n°{self.__id}")
                self.show_balance()
                other.show_balance()
            else : 
                print(f"You wish to transfer {ammount}€ but your balance is {self.__balance}€, insufficient funds")
        except TypeError : 
            print("Ammount must represent money : use a positive int or float")

account_1 = BankAccount("01", "Nelson", "Grac", 2500, False)

account_1.show_details()
account_1.show_balance()
account_1.deposit(100)
account_1.deposit("error")
account_1.withdrawal(["wrong","type"])
account_1.withdrawal(9999)
account_1.withdrawal(1000)

account_2 = BankAccount("02", "Mila", "Grac", 2500, True)

account_2.withdrawal(9999)
account_2.penalty()

account_1.transfer(account_2, 7573.99)
account_1.deposit(10000)
account_1.transfer(account_2, 7573.99)