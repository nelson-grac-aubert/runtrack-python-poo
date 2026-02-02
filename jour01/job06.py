class Animal() : 

    def __init__(self) : 
        self.age = 0
        self.nom = "Vide" 

    def vieillir(self) : 
        self.age += 1 
        print("L'animal a vieilli")
    
    def afficher_age(self) : 
        print(f"Age de l'animal : {self.age} an(s)")

    def nommer(self, nom) : 
        self.nom = nom
        print(f"L'animal a été nommé {self.nom}")

poule = Animal()

poule.afficher_age()
poule.vieillir()
poule.afficher_age()
poule.vieillir()
poule.afficher_age()

poule.nommer("Cocotte")
