class Ship:
    def __init__(self, parts : dict):
        self.__parts = parts
    
    def get_parts(self):
        return self.__parts
    def set_parts(self, new_parts):
        self.__parts = new_parts

    def display_state(self): 
        print("\n ----- Current state of the boat -----")
        for key in self.get_parts() : 
            print(self.get_parts()[key])

    def replace_part(self, replaced_part_name, new_part):
        """ Replace a part with a brand new one """
        for key in self.get_parts(): 
            if self.get_parts()[key].get_name() == replaced_part_name : 
                self.get_parts()[key] = new_part
    
    def change_part(self, part_name, new_material): 
        """ Pick a current ship piece by its name and change its material """
        for key in self.get_parts():
            if self.get_parts()[key].get_name() == part_name : 
                self.get_parts()[key].set_material(new_material)



