# Créer une classe nommée Forme possédant une méthode nommée aire qui
# renvoie 0.
# Créer une classe Rectangle qui hérite de la classe Forme et qui possède deux
# attributs largeur et hauteur. Surcharger la méthode aire dans la classe
# Rectangle afin qu’elle ne renvoie plus 0, mais l’aire du rectangle.
# Écrire en console le résultat de la méthode aire de la classe Rectangle.

from class_shape import Shape
from class_rectangle import Rectangle
from class_circle import Circle

shape_1 = Shape()
rectangle_1 = Rectangle(3,4)

print(rectangle_1.surface())
print(shape_1.surface())

# Récupérer votre classe Forme crée juste au-dessus.

# Créer une classe fille nommée Cercle qui hérite de la classe Forme et
# possédant un attribut radius.
# Surcharger la méthode aire dans la classe Cercle pour qu'elle renvoie l’aire
# du cercle.
# Créez une instance de chaque classe Rectangle et Cercle et utilisez-les pour
# tester les différentes surcharges de la méthode aire en affichant les résultats
# en console.

circle_1 = Circle(5)

print(circle_1.surface())