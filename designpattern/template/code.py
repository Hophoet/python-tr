class Person:
    
    def __init__(self, name):
        self.name = name

    def _display(self):
        raise NotImplemented
    def show(self):
        self._display()

class Student(Person):

    def __init__(self, name):
        Person.__init__(self, name)

    def _display(self):
        print('Student '+self.name)

alex = Person('alex')
alex.show()

lili = Student('lili')
lili.show()