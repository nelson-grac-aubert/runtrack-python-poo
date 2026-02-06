from class_part import Part

class Ship:
    def __init__(self, parts : dict):
        self.__parts = parts
    
    def get_parts(self):
        return self.__parts
    def set_parts(self, new_parts):
        self.__parts = new_parts

    def add_part(self, new_part : Part): 
        self.get_parts()[str(len(self.get_parts())+1)] = new_part

    def display_state(self): 
        print("\n ----- Current state of the boat -----")
        for key in self.get_parts() : 
            print(self.get_parts()[key])

    def replace_part(self, replaced_part_name : str, new_part : Part):
        """ Replace a part with a brand new one """
        for key in self.get_parts(): 
            if self.get_parts()[key].get_name() == replaced_part_name :
                old_part = self.get_parts()[key] 
                self.get_parts()[key] = new_part
                print(f"{old_part} has been replaced by {new_part}")
    
    def change_part(self, part_name : str, new_material : str): 
        """ Pick a current ship piece by its name and change its material """
        for key in self.get_parts():
            if self.get_parts()[key].get_name() == part_name : 
                self.get_parts()[key].set_material(new_material)
                print(f"\n{part_name} is now made of {new_material}")



