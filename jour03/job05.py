import random
import time

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

class Character():
    def __init__(self, name : str, health : int) : 
        self.__name = name
        self.__health = health
    
    def get_name(self):
        return self.__name
    
    def get_health(self):
        return self.__health
    def set_health(self, new_health) : 
        self.__health = new_health
        
    def attack(self, other):
        damage = random.randint(10,15)
        other.set_health(other.get_health() - damage)
        print(f"{self.get_name()} has dealt {damage} damage to {other.get_name()}!!!")
        print(f"{other.get_name()} has {other.get_health()} health remaining\n")
    
    def check_death(self):
        if self.get_health() <= 0 : 
            return True
        else : 
            return False

class Game():
    def __init__(self): 
        self.__active_characters = []
        self.__difficulty = self.chose_difficulty()
        self.launch_game()
        self.game_loop()

    def chose_difficulty(self):
        while True : 
            choice = input("Chose a difficulty : easy, medium or hard : ")

            if choice == "easy" or choice == "medium" or choice == "hard" : 
                return choice
            else : 
                print("Difficulty must be one of the three, it's case sensitive, type more carefully")
    def get_difficulty(self):
        return self.__difficulty

    def launch_game(self) : 
        if self.get_difficulty() == "easy" : 
            player_health = 100
            enemy_health = 80

        elif self.get_difficulty() == "medium" : 
            player_health = 100
            enemy_health = 90
        else : 
            player_health = 100
            enemy_health = 100
        
        print(f"\nDifficulty {self.get_difficulty()} has been chosen")
        print(f"Enemy spawned with {enemy_health} health")
        print(f"Player spawned with {player_health} health\n")

        player = Character("Player", player_health)
        enemy = Character("Enemy", enemy_health)
        self.__active_characters.append(player)
        self.__active_characters.append(enemy)

        time.sleep(2)
        
    def game_loop(self) : 
        running = True
        while running :
            for element in self.__active_characters : 
                target = self.__active_characters[0] if element == self.__active_characters[1] else self.__active_characters[1]
                element.attack(target)
                
                check = target.check_death()
                if check == True : 
                    print(f"{element.get_name()} is victorious! {target.get_name()} is defeated!")
                    running = False
                    break

                time.sleep(1)

current_game = Game()
