# Créer une classe Rectangle avec comme attribut privé longueur et largeur.
# Créer la méthode perimetre permettant de calculer le périmètre du
# rectangle ainsi que la méthode surface permettant de calculer la surface du
# rectangle.

# Créer les assesseurs et mutateurs permettant de manipuler les attributs de
# la classe.

# Créer une classe Parallelepipede héritant de la classe Rectangle avec en
# plus un attribut hauteur et une autre méthode volume, permettant de
# calculer le volume du parallélépipède.

# Instancier la classe Rectangle et assurez-vous que toutes les méthodes
# fonctionnent.

from class_rectangle import Rectangle
from class_parallelepiped import Parallelepiped

rectangle_1 = Rectangle(3,4)
print(rectangle_1.perimeter())
print(rectangle_1.surface())

parallelepiped_1 = Parallelepiped(3,4,5)
print(parallelepiped_1.volume())

parallelepiped_1.set_height(6)
parallelepiped_1.set_length(7)
parallelepiped_1.set_width(8)
print(parallelepiped_1.volume())