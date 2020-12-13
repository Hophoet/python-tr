class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age 

    def greet(self):
        print('human', self.name, 'says', 'hello')

    def __str__(self):
        return self.name


class Student:
    def __init__(self, field):
        self.field = field

    def greet(self):
        print("student says", "hello")

    
class Teacher( Student, Person):
    """ Teachers representation class """
    number = 0
    def __init__(self, name, age, field):
        Person.__init__(self, name, age)
        Student.__init__(self, field)

   
    



