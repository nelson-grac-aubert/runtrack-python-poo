class Livre : 
    def __init__(self, titre, auteur, nb_pages) : 
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages 
        self.__disponible = True

    def get_titre(self):
        return self.__titre
    def set_titre(self, new_titre):
        self.__titre = new_titre

    def get_auteur(self):
        return self.__auteur
    def set_auteur(self, new_auteur):
        self.__auteur = new_auteur

    def get_nb_pages(self):
        return self.__nb_pages
    def set_nb_pages(self, new_nb_pages):
        if type(new_nb_pages) == int and new_nb_pages > 0 : 
            self.__nb_pages = new_nb_pages
        else : 
            print("Le nombre de pages doit être un entier positif")

    def verification(self):
        return self.__disponible
    
    def emprunter(self):
        if self.verification() == True : 
            self.__disponible = False
        else : 
            print("Le livre est déjà emprunté")

    def rendre(self):
        if self.verification() == False : 
            self.__disponible = True
        else : 
            print("Le livre est déjà en stock")

mon_livre = Livre("Une histoire", "Un auteur", 250)

print(mon_livre.verification())
mon_livre.emprunter()
print(mon_livre.verification())
mon_livre.rendre()
print(mon_livre.verification())