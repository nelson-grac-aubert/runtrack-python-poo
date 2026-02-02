class Personne() : 


    def __init__(self, nom, prenom) : 

        self.nom = nom
        self.prenom = prenom


    def SePresenter(self): 

        print(f"Je suis {self.prenom} {self.nom}")
        return self.prenom, self.nom

jules = Personne("Dupont", "Jules") 
marie = Personne("Duchêne", "Marie")
nelson = Personne("Grac-Aubert", "Nelson")

jules.SePresenter()
marie.SePresenter()
nelson.SePresenter()