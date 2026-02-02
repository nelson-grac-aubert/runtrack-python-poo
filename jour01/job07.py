class Personnage() : 
    def __init__(self, x, y) : 
        self.x = x
        self.y = y 

    def gauche(self) : 
        self.x -= 1 
    
    def droite(self) : 
        self.x += 1 

    def haut(self) : 
        self.y += 1 
    
    def bas(self) : 
        self.y -= 1 

    def position(self) : 
        print(f"La position du joueur est ({self.x}, {self.y})")
        return (self.x, self.Y)

joueur = Personnage(2,3)

joueur.position()

joueur.haut()
joueur.droite()

joueur.position()