class Livre() : 
    def __init__(self, titre, auteur, nb_pages) : 
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages 

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