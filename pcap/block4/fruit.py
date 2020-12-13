class Fruit:
    number = 0

    #constructor
    def __init__(self, name):
        self.name = name
        Fruit.number += 1

    def _get_name(self):
        try:
            return self.name 
        except Exception as error:
            print("name don't exists!")
    
    def _set_name(self, name):
        self.name = name 

    def _del_name(self):
        del self.name

    def __repr__(self):
        return self.name

    name = property(_get_name, _set_name, _del_name, "attribute name")

    @classmethod
    def getNumber(cls):
        return Fruit.number

    
class Banana(Fruit):

    def __init__(self, name):
        Fruit.__init__(self, name)
        self.type = "summer"
        

    def get_name(self):
        print('child method')
        return self.name