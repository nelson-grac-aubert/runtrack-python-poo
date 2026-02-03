# Créer une classe Voiture qui a pour attributs privés une marque, un modèle,
# une année, un kilométrage et un attribut nommé en_marche initialisé par
# défaut à False.
# Cette classe doit posséder des mutateurs et assesseurs pour chaque attribut.

# _4

# Créer une méthode demarrer qui change la valeur de l’attribut en_marche
# en True, une méthode arreter qui change la valeur de l’attribut en_marche
# en False.
# Ajoutez à la classe Voiture l’attribut privé reservoir qui est initialisé à 50 par
# défaut dans le constructeur. Créer une méthode privée verifier_plein qui
# retourne la valeur de l’attribut reservoir. Cette méthode est appelée dans la
# méthode demarrer. Si la valeur du réservoir est supérieure à 5 la voiture peut
# démarrer.

class Car : 
    def __init__(self, brand, model, year, distance) :
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__distance = distance
        self.__running = False 
        self.__tank = 50

    def set_tank(self, new_tank) : 
        self.__tank = new_tank

    def __get_tank(self) : 
        return self.__tank

    def get_running(self) : 
        return self.__running

    def start(self) :
        if self.get_running() == False : 
            if self.__get_tank() > 5 : 
                self.__running = True
            else : 
                print("Not enough gas to start engine")
        else : 
            print("Car is already running")
    
    def stop(self) : 
        if self.get_running() == True : 
            self.__running = False
        else : 
            print("Engine is already off")

my_car = Car("Toyota", "Prius", "2014", 13000)

my_car.stop()
print(my_car.get_running())
my_car.start()
print(my_car.get_running())
my_car.start()
my_car.stop()
my_car.set_tank(4)
my_car.start()
