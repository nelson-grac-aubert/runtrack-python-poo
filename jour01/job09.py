class Produit() : 
    def __init__(self, nom, prixHT, TVA) : 
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA 

    def get_nom(self) : 
        return self.nom
    def set_nom(self, new_nom) : 
        self.nom = new_nom

    def get_prixHT(self) : 
        return self.prixHT
    def set_prixHT(self, new_prixHT) : 
        self.prixHT = new_prixHT

    def get_TVA(self) : 
        return self.TVA
    def set_TVA(self, new_TVA) : 
        self.TVA = new_TVA

    def CalculerPrixTTC(self) : 
        return self.prixHT * (1+self.TVA)
    
    def __repr__(self) : 
        return f"{self.nom} qui coute {self.prixHT}€ hors taxe, donc {self.CalculerPrixTTC():.2f}€ après une TVA de {self.TVA * 100}%"

un_objet = Produit("T-shirt", 15, 0.2)
un_plat_au_restaurant = Produit("Entrecôte", 17, 0.1)
un_aliment = Produit("4 Yaourts", 2, 0.055)

print(un_aliment)
print(un_objet)
print(un_plat_au_restaurant)

un_objet.set_nom("Un pull")
print(f"L'objet modifié est {un_objet.get_nom()}")

un_plat_au_restaurant.set_prixHT(19)
print(f"Le nouveau prix du plat est {un_plat_au_restaurant.get_prixHT()}€")

un_aliment.set_nom("Un plat préparé")
un_aliment.set_prixHT(4)
un_aliment.set_TVA(0.1)
print(f"La nouvelle TVA de l'aliment est {un_aliment.get_TVA()*10}%")
print(un_aliment)
