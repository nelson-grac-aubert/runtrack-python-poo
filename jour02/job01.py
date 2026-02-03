class Rectangle : 
    def __init__(self, largeur, longueur) : 
        self.__largeur = largeur
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur
    def set_largeur(self, new_largeur):
        self.__largeur = new_largeur

    def get_longueur(self):
        return self.__longueur
    def set_longueur(self, new_longueur):
        self.__longueur = new_longueur

mon_rectangle = Rectangle(5, 10)

print(mon_rectangle.get_largeur())
print(mon_rectangle.get_longueur())

mon_rectangle.set_longueur(12)
mon_rectangle.set_largeur(6)

print(mon_rectangle.get_largeur())
print(mon_rectangle.get_longueur())


