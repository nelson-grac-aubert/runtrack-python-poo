class Point() :


    def __init__(self, x, y) : 
        self.x = x
        self.y = y


    def afficherLesPoints(self) : 
        print(f"Les coordonnées sont ({self.x}, {self.y})")

    def afficherX(self) : 
        print(f"L'absice est {self.x}")

    def afficherY(self) : 
        print(f"L'ordonnée est {self.y}")

    def changerX(self, new_x) : 
        self.x = new_x
    
    def changerY(self, new_y) : 
        self.y = new_y

mon_point = Point(3,5)

mon_point.afficherLesPoints()
mon_point.afficherX()
mon_point.afficherY()

mon_point.changerX(13)
mon_point.changerX(12)

mon_point.afficherLesPoints()
mon_point.afficherX()
mon_point.afficherY()