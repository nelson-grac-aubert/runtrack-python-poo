from class_part import Part

class Ship:
    def __init__(self, parts : dict):
        self.__parts = parts
    
    def get_parts(self):
        return self.__parts
    def set_parts(self, new_parts : dict):
        self.__parts = new_parts

    def add_part(self, new_part : Part): 
        """
        Add a new part to the ship that is self

        :param self: The ship object targeted by this method
        :type self: Ship
        :param new_part: The Part you want to add to your ship
        :type new_part: Part
        """
        self.get_parts()[str(len(self.get_parts())+1)] = new_part

    def display_state(self): 
        """ Print a human friendly recap of all parts on the ship """

        print("\n ----- Current state of the boat -----")
        for key in self.get_parts() : 
            print(self.get_parts()[key])

    def replace_part(self, replaced_part_name : str, new_part : Part):
        """
        Replace a part (chosen by it's name attribute) by a new one.
        
        :param self: The ship object targeted by this method
        :type self: Ship
        :param replaced_part_name: Name attribute of the place you want to replace
        :type replaced_part_name: str
        :param new_part: Part object that will replace the named one
        :type new_part: Part
        """
        for key in self.get_parts(): 
            if self.get_parts()[key].get_name() == replaced_part_name :
                old_part = self.get_parts()[key] 
                self.get_parts()[key] = new_part
                print(f"{old_part} has been replaced by {new_part}")
    
    def change_part(self, part_name : str, new_material : str): 
        """
        Replace a part's (chosen by it's name attribute) material.
        
        :param self: The ship object targeted by this method
        :type self: Ship
        :param part_name: Name attribute of the part whose material you want to change
        :type part_name: str
        :param new_material: New material for that part
        :type new_material: str
        """
        for key in self.get_parts():
            if self.get_parts()[key].get_name() == part_name : 
                self.get_parts()[key].set_material(new_material)
                print(f"\n{part_name} is now made of {new_material}")



