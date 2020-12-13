class Person:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name 

zir = Person('zir')
alex = Person('alex')
lili = Person('lili')


persons = [zir, alex, lili]
print('persons befor sorting', persons)
sorted_persons = sorted(persons, key=lambda person: person.name)
print('persons after sorting', sorted_persons)