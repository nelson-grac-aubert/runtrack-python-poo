# Dans cet exercice, vous allez créer votre to do list.

# Créer une classe Tache qui représente une tâche à faire. Cette classe a
# comme attribut un titre, une description et un statut (à faire ou terminer)
# initialisés dans le constructeur.

# Créer une classe ListeDeTaches qui représente la liste des tâches à faire ainsi
# que toutes les méthodes nécessaires à la gestion de celles-ci avec comme
# attribut taches(liste).

# Ajouter les méthodes suivantes :
# ➔ ajouterTache : qui permet d’ajouter une tâche.
# ➔ supprimerTache : qui permet de supprimer une tâche.
# ➔ marquerCommeFinie : qui permet de signaler que la tâche est faite.
# ➔ afficherListe : qui permet de retourner une liste de toutes les tâches.
# ➔ filterListe : qui permet de filtrer les tâches par rapport à un statut et
# retourne cette liste.

# Tester votre code en créant plusieurs instances de Tache, les ajouter à la
# classe listeDeTache, supprimer une tache, changer le statut d’une tâche,
# afficher toutes les tâches et afficher les tâches à faire.

class Task() : 
    def __init__(self, title, description, status = "Pending"):
        self.__title = title
        self.__description = description
        self.__status = status

    def get_title(self) : 
        return self.__title
    
    def get_description(self) : 
        return self.__description  
      
    def get_status(self) : 
        return self.__status
    def set_status(self, new_status) : 
        self.__status = new_status
    

class TaskList() : 
    def __init__(self,tasks) : 
        self.__tasks = tasks 

    def add_task(self, new_task) : 
        self.__tasks.append(new_task)

    def delete_task(self, removed_task) : 
        self.__tasks.remove(removed_task)

    def mark_as_finished(self, finished_task) : 
        for element in self.__tasks : 
            if element == finished_task : 
                if element.get_status() == "Pending" : 
                    element.set_status("Done")
                else : 
                    print("Task was already completed")
    
    def show_all_tasks(self) : 
        for i in range (len(self.__tasks)) : 
            print(f"Task {i+1}----------------------------------")
            print(self.__tasks[i].get_title())
            print(f"Description : {self.__tasks[i].get_description()}")
            print(f"Status : {self.__tasks[i].get_status()}")

    def filter_list(self, filter) : 
        filtered_list = []
        for element in self.__tasks : 
            if element.get_status() == filter : 
                filtered_list.append(element)
                
        filtered_tasklist = TaskList(filtered_list)
        return filtered_tasklist
    
task_1 = Task("Clean", "Buy a mop and use it in bedroom")
task_2 = Task("Cook", "Cook a tasty meal")
task_3 = Task("Study", "Learn C# for an hour")
task_4 = Task("Read(done)", "Placeholder task that is already done", "Done")

task_list = TaskList([task_1, task_2])

task_list.show_all_tasks()
task_list.add_task(task_3)
task_list.show_all_tasks()
task_list.mark_as_finished(task_1)
task_list.show_all_tasks()

pending_task_list = task_list.filter_list("Pending")
pending_task_list.show_all_tasks()

task_list.add_task(task_4)
done_task_list = task_list.filter_list("Done")
done_task_list.show_all_tasks()