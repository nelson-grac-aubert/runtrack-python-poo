# Créer une classe pour représenter un joueur ainsi qu'une classe pour
# représenter une équipe de foot.

# La classe Joueur doit avoir les attributs suivants : nom, numéro, position,
# nombre de buts marqués, passes décisives effectuées, cartons jaunes reçus
# et cartons rouges reçus. Tous ces attributs doivent être initialisés lors de la
# création de l’objet Joueur.

# Cette classe doit posséder les méthodes suivantes :
# ➔ marquerUnBut,
# ➔ effectuerUnePasseDecisive,
# ➔ recevoirUnCartonJaune,
# ➔ recevoirUnCartonRouge,
# ➔ afficherStatistiques.

# Ces méthodes permettent de mettre à jour les statistiques du joueur.

# La classe Equipe doit avoir les attributs nom et liste de joueurs. Le nom de
# l’équipe et la liste de joueurs (liste vide par défaut) doivent être initialisés
# dans le constructeur.

# Ajouter les méthodes suivantes dans la classe Equipe :
# - ajouterJoueur : cette méthode ajoute un joueur à l’équipe.
# - AfficherStatistiquesJoueurs : cette méthode permet d’afficher toutes
# les statistiques de l’ensemble des joueurs.
# - mettreAJourStatistiquesJoueur : cette méthode permet de mettre à
# jour les statistiques d’un joueur (buts, cartons ...).

# Créez plusieurs joueurs avec les paramètres de votre choix et ajoutez-les aux
# équipes.

# Présenter l’ensemble des joueurs de chaque équipe. Utiliser les différentes
# méthodes afin de simuler un match, marquer un but, avoir un carton rouge...
# Et afficher à nouveau les statistiques des joueurs.

class Player():
    def __init__(self, name, id, position, goal_ammount=0, assists_ammount=0, red_card_ammount=0, yellow_card_ammount=0) : 
        self.__name = name
        self.__id = id
        self.__position = position
        self.__goal_ammount = goal_ammount
        self.__assists_ammount = assists_ammount
        self.__red_card_ammount = red_card_ammount
        self.__yellow_card_ammount = yellow_card_ammount

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_position(self):
        return self.__position
    
    def get_goals(self):
        return self.__goal_ammount
    def score_goal(self) : 
        self.__goal_ammount += 1

    def get_assists(self):
        return self.__assists_ammount   
    def assist_goal(self) :
        self.__assists_ammount += 1 
    
    def get_red_cards(self):
        return self.__red_card_ammount
    def add_red_card(self):
        self.__red_card_ammount +=1
    
    def get_yellow_cards(self):
        return self.__yellow_card_ammount
    def add_yellow_card(self):
        self.__yellow_card_ammount +=1 
        if self.__yellow_card_ammount %2 == 0 : 
            self.__red_card_ammount += 1
    
    def show_stats(self) : 
        print(f"------ {self.get_name()} ------")
        print(f"ID : {self.get_id()}")
        print(f"Position : {self.get_position()}")
        print(f"Stats this season : {self.get_goals()} goals, {self.get_assists()} assists, {self.get_red_cards()} red cards, {self.get_yellow_cards()} yellow cards")

class Team():
    def __init__(self, name, player_list = []):
        self.__name = name
        self.__player_list = player_list
    
    def get_name(self): 
        return self.__name()
    def set_name(self, new_name): 
        self.__name = new_name

    def get_player_list(self): 
        return self.__player_list()
    def add_player(self, new_player : Player):
        self.__player_list.append(new_player)
    
    def show_all_stats(self):
        for element in self.__player_list : 
            element.show_stats()
    
    def update_player_goals(self, player):
        for element in self.__player_list : 
            if element == player : 
                element.score_goal()
    def update_player_assists(self, player):
        for element in self.__player_list : 
            if element == player : 
                element.assist_goal()
    def update_player_red_cards(self, player):
        for element in self.__player_list : 
            if element == player : 
                element.add_red_card()
    def update_player_yellow_cards(self, player):
        for element in self.__player_list : 
            if element == player : 
                element.add_yellow_card()

player1 = Player("Pau López", 1, "Gardien de but")
player2 = Player("Jonathan Clauss", 2, "Arrière droit")
player3 = Player("Chancel Mbemba", 3, "Défenseur central")
player4 = Player("Leonardo Balerdi", 4, "Défenseur central")
player5 = Player("Quentin Merlin", 5, "Arrière gauche")
player6 = Player("Jordan Veretout", 6, "Milieu central")
player7 = Player("Geoffrey Kondogbia", 7, "Milieu défensif")
player8 = Player("Amine Harit", 8, "Milieu offensif")
player9 = Player("Iliman Ndiaye", 9, "Ailier droit")
player10 = Player("Pierre-Emerick Aubameyang", 10, "Avant-centre")
player11 = Player("Ismaïla Sarr", 11, "Ailier gauche")

o_m = Team("Olympique de Marseille")

o_m.add_player(player1)
o_m.add_player(player2)
o_m.add_player(player3)
o_m.add_player(player4)
o_m.add_player(player5)
o_m.add_player(player6)
o_m.add_player(player7)
o_m.add_player(player8)
o_m.add_player(player9)
o_m.add_player(player10)
o_m.add_player(player11)

# o_m.show_all_stats()

o_m.update_player_goals(player11)
o_m.update_player_goals(player9)
o_m.update_player_assists(player10)
o_m.update_player_assists(player10)
o_m.update_player_yellow_cards(player8)
o_m.update_player_yellow_cards(player8)
o_m.update_player_red_cards(player11)
o_m.update_player_red_cards(player7)

o_m.show_all_stats()