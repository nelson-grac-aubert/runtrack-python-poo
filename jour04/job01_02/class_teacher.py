from class_person import Person

class Teacher(Person) : 
    def __init__(self, subject): 
        super().__init__()
        self.__teached_subject = subject

    def teach(self) : 
        print("The class is starting, be quiet")