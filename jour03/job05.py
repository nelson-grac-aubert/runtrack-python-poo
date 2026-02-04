# Créez un jeu de combat en utilisant la POO.

# À tour de rôle, votre personnage et l’ennemi attaquent. Le but étant de
# vaincre l’ennemi (vie à zéro).

# Votre programme doit contenir au minimum deux classes, Personnage et
# Jeu.

# Commencer par créer une classe nommée Personnage prenant des
# paramètres de construction : nom (string) et vie(int).
# Créez au minimum une méthode attaquer qui enlève des points à son
# adversaire.

# Ensuite créer la classe Jeu ne prenant pas de paramètre. Créer une méthode
# choisirNiveau qui permet de demander au joueur le niveau de difficulté.
# Celui-ci sera stocké dans l’attribut niveau.

# En fonction du niveau choisi, le nombre de points de vie du joueur ainsi que
# de l'ennemi seront différents.
# Créer lancerJeu, méthode qui utilise l’attribut niveau. Cette méthode aura
# pour but d’instancier deux objets Personnage, un qui représente le joueur et
# l’autre l'ennemi avec un nombre de points défini en fonction du niveau.

# Implémenter le déroulement d’une partie en demandant au joueur le niveau
# de difficulté et pensez à ajouter une méthode qui vérifie la santé de vos
# personnages ainsi qu’une méthode permettant de vérifier qui a gagné.