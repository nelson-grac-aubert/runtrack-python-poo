# 1. Création de la classe Part
# ○ Définissez une classe Part avec les attributs name (ex. "Mât") et
# material (ex. "Bois").
# ○ Ajoutez une méthode change_material(new_material) pour
# modifier le matériau.
# ○ Implémentez une méthode __str__ pour afficher une
# description de la pièce.
# 2. Création de la classe Ship
# ○ Définissez une classe Ship avec un nom et un dictionnaire privé
# __parts contenant plusieurs instances de Part.
# ○ Ajoutez une méthode display_state() pour lister les pièces du
# bateau.
# ○ Implémentez une méthode replace_part(part_name,
# new_part) pour remplacer une pièce existante.

# 3. Passage par référence
# a. Ajoutez une méthode change_part(part_name, new_material)
# pour changer directement le matériau d'une pièce existante.

# b. Montrez que les objets Part sont modifiés directement en
# mémoire.
# c. Création de la classe dérivée RacingShip
# d. Créez une classe RacingShip qui hérite de Ship.
# e. Ajoutez un attribut supplémentaire max_speed.
# ○ Ajoutez une méthode display_speed() pour afficher la vitesse
# maximale.

# 4. Interaction et personnalisation
# ○ Créez un menu interactif avec des options pour remplacer des
# pièces, modifier des matériaux, ou afficher l'état du bateau.
# ○ Ajoutez un historique des modifications pour suivre l'évolution du
# bateau.

from class_part import Part
from class_ship import Ship
from class_racing_ship import RacingShip

part_1 = Part("Deck", "wood")
print(part_1)
part_2 = Part("Sail", "cloth")
part_3 = Part("Long rope", "nylon")

ship_1 = Ship({"1" : part_1, "2" : part_2})
ship_1.display_state()

ship_1.replace_part("Deck", part_3)
ship_1.display_state()

ship_1.change_part("Sail", "stronger, thicker cloth")
ship_1.display_state()

racing_ship_part_1 = Part ("Massive 2000 horsepower gasoline motor", "plastic and metal")
racing_ship_1 = RacingShip({"1" : part_1, "2": racing_ship_part_1}, 100)

racing_ship_1.display_state()
