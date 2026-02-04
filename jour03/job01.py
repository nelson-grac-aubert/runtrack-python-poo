# Créer une classe Ville avec comme attributs privés un nom et un nombre
# d'habitants.
# Créer une classe Personne avec les attributs privés suivants : nom, âge et un
# objet de la classe ville.
# Ajouter la méthode ajouterPopulation dans la classe Personne qui permet
# d’augmenter de 1 le nombre d’habitants de la ville.

# Créer un objet Ville avec comme arguments “Paris” et 1000000.
# Afficher en console le nombre d’habitants de la ville de Paris.

# Créer un autre objet Ville avec comme arguments “Marseille” et 861635.
# Afficher en console le nombre d’habitants de la ville de Marseille.

# Créer les objets suivants :
# - John, 45 ans, habitant à Paris
# - Myrtille, 4 ans, habitant à Paris.
# - Chloé, 18 ans, habitant à Marseille.

# _1

# Afficher le nombre d’habitants de Paris et de Marseille après l’arrivée de ces
# nouvelles personnes.

class Town() : 
    def __init__(self, name, inhabitants_count) : 
        self.__name = name
        self.__inhabitants_count = inhabitants_count

    def get_name(self):
        return self.__name
    def get_inhabitants_count(self):
        return self.__inhabitants_count

class Person() : 
    def __init__(self, name, age, town) : 
        self.__name = name
        self.__age = age
        self.__town = town 
        self.add_population()

    def add_population(self) : 
        self.__town.__inhabitants_count += 1

paris = Town("Paris", 1000000)

print(f"Number of inhabitants in {paris.get_name()} : {paris.get_inhabitants_count()}")