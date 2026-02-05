# Créer une classe Personne qui aura comme attribut age prenant un entier et
# initialisé à 14 par défaut. Ajouter une méthode afficherAge qui affichera en
# console l'âge de la personne et une méthode bonjour qui écrit en console
# ‘Hello’. Créer une méthode modifierAge prenant en paramètre un entier et
# permettant de modifier l'âge de la personne.
# Créer une classe Eleve qui hérite de la classe Personne qui n’a pas d’attribut
# et une méthode publique allerEnCours qui affiche : “Je vais en cours” ainsi
# qu’une méthode afficherAge qui écrit en console : “J’ai XX ans”.
# Créer une classe Professeur avec un attribut privé matiereEnseignee, qui
# indiquera la matière du professeur, et une méthode publique enseigner qui
# affiche : “Le cours va commencer”.

# Instancier une classe Personne et une classe Eleve. Afficher l'âge par défaut
# de l’élève en console.

from class_person import Person
from class_teacher import Teacher
from class_student import Student

person_1 = Person()
student_1 = Student()
student_1.display_age()

# À l’aide de la classe Personne, Eleve et Professeur créent au-dessus, faites
# dire bonjour à votre élève grâce à la méthode bonjour ainsi que “Je vais en
# cours” grâce à la méthode allerEnCours. Redéfinir l'âge de l’élève à 15 ans.

# Créez un objet Professeur, 40 ans, faites dire bonjour à votre professeur et
# commencez le cours grâce à la méthode enseigner.

student_1.speak()
student_1.go_to_class()

student_1.set_age("test the error condition")
student_1.set_age(15)
student_1.display_age()

teacher_1 = Teacher("Math")
teacher_1.set_age(40)
teacher_1.display_age()
teacher_1.teach()