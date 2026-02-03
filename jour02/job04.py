class Student : 
    def __init__(self, last_name, first_name, id) : 
        self.__last_name = last_name
        self.__first_name = first_name
        self.__id = id 
        self.__credits = 0
        self.__level = self.__studentEval()

    def get_last_name(self) : 
        return self.__last_name
    
    def get_first_name(self) : 
        return self.__first_name
    
    def get_id(self) : 
        return self.__id

    def get_credits(self) : 
        return self.__credits
    
    def get_level(self) : 
        return self.__level
    def set_level(self) : 
        self.__level = self.__studentEval()
    
    def add_credits(self, amount) : 
        if type(amount) == int and amount > 0 : 
            self.__credits += amount 
        else : 
            print("The amount of credits added must be a positive integer")

    def __studentEval(self) : 
        if self.__credits >= 90 : 
            return "Excellent"
        elif 90 > self.__credits >= 80 : 
            return "Very Good"
        elif 80 > self.__credits >= 70 : 
            return "Good"
        elif 70 > self.__credits >= 60 : 
            return "Acceptable"
        elif 60 > self.__credits : 
            return "Insufficient"
    
    def studentInfo(self) : 
        self.set_level()
        print(f"Student name : {self.get_last_name()}")
        print(f"Student first name : {self.get_first_name()}")
        print(f"Student ID : {self.get_id()}")
        print(f"Student level : {self.get_level()}")

my_student = Student("Doe", "John", 145)
my_student.studentInfo()
my_student.add_credits(65)
my_student.studentInfo()
my_student.add_credits(10)
my_student.studentInfo()
my_student.add_credits(20)
my_student.studentInfo()