# Créer une classe Commande avec les attributs privés, numéro de
# commande, liste de plats commandés et statut de la commande (en cours,
# terminée ou annulée).

# Ajouter des méthodes permettant d’ajouter un plat à la commande, annuler
# une commande, calculer le total d’une commande privée et afficher une
# commande avec son total à payer, ainsi qu’une méthode permettant de
# calculer la TVA.

# Utiliser l’encapsulation et l’abstraction pour créer cette classe de manière que
# les attributs ne puissent pas être modifiés de l’extérieur. La liste des plats
# commandés doit être représentée sous forme de dictionnaire avec les noms
# des plats, le prix ainsi que le statut de la commande.

class Order : 
    def __init__(self, id, dishes, status) :
        self.__id = id
        self.__dishes = dishes
        self.__status = status

    def get_id(self) : 
        return self.__id
    def __set_id__(self, new_id) : 
        self.__id = new_id

    def get_status(self) : 
        return self.__status
    def __set_status__(self, new_status) : 
        self.__status = new_status
        # self.get_status() = new_status

    def get_dishes(self) : 
        return self.__dishes
    def add_dish(self, new_dish_name, new_dish_price) : 
        self.__dishes[new_dish_name] = new_dish_price

    def cancel_order(self) : 
        if self.get_status() == "Pending" : 
            self.__set_status__("Cancelled")
        elif self.get_status() == "Pending" : 
            print("Can't cancel an order that's delivered")
        elif self.get_status() == "Cancelled" : 
            print("Order was already cancelled")
    
    def __get_total__(self) : 
        return sum(self.get_dishes().values())
    
    def __calculate_taxes(self) : 
        return self.__get_total__() * 0.1
    
    def __calculate_total_with_taxes(self) : 
        return self.__get_total__() + self.__calculate_taxes()
    
    def the_ultimate_recap(self) : 

        print(f"Order ID : {self.get_id()}")
        print(f"Order status : {self.get_status()}")
        
        for key in self.get_dishes() : 
            print(f"{key} that costs {self.get_dishes()[key]} €")

        print(f"Total excluding taxes : {self.__get_total__()}")
        print(f"Tax : {self.__calculate_taxes()}")
        print(f"Please pay : {self.__calculate_total_with_taxes()}")
    
my_order = Order("01", {"A salad" : 9, "A meat" : 17, "A dessert" : 5}, "Pending")

# Add a dish to the order 
my_order.add_dish("A glass of wine", 4)
print(my_order.get_dishes())


# Cancel the order
print(my_order.get_status())
my_order.cancel_order()
print(my_order.get_status())

print("\n -------------------------------------------- \n")

my_order.the_ultimate_recap()