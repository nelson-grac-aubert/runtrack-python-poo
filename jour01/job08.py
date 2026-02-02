class Cercle() : 

    def __init__(self, rayon) : 
        self.rayon = rayon

    def changerRayon(self, new_rayon) : 
        self.rayon = new_rayon

    def circonference(self) : 
        circ = self.rayon * 3.141592653 * 2 
        return circ

    def diamètre(self) : 
        diam = self.rayon * 2 
        return diam
    
    def aire(self) : 
        aire = self.rayon ** 2 * 3.141592653
        return aire

    def afficherInfos(self) : 
        print(f"Un cercle de rayon {self.rayon}, de diamètre {self.diamètre()}, de circonférence {self.circonference()} et d'aire {self.aire()}")

mon_cercle = Cercle(4)
mon_cercle.afficherInfos()

mon_cercle.changerRayon(7)
mon_cercle.afficherInfos()