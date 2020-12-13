from fruit import Fruit, Banana
from human import Teacher, Person



# fruit = Fruit("banana")
# fruit = Fruit("apple")
# banana = Banana('africa summer  banana')
# print('banana', banana.name)

t = Teacher('lili', 28, "software development")
# t.greet()

# print(t.name, 'object __dict__', t.__dict__)
# print('Teacher class __dict__', Teacher.__dict__)

# # print(t.name, 'object __name__', t.__name__)
# print('Teacher class __name__', Teacher.__name__)

# print(t.name, 'object __module__', t.__module__)
# print('Teacher class __module__', Teacher.__module__)

# # print(t.name, 'object __bases__', t.__bases__)
# print('Teacher class __bases__', Teacher.__bases__)



# print('hasattr(t, \'field\')', hasattr(t, 'field'))
# print('hasattr(Teacher, \'field\')', hasattr(Teacher, 'field'))

# print('hasattr(t, \'number\')', hasattr(t, 'number'))
# print('hasattr(Teacher, \'number\')', hasattr(Teacher, 'number'))


#TYPE
# print(type(t))
# print(type(Teacher))

#ISSUBCLASS
# print(issubclass(Teacher, Person))

#ISINSTANCE
# print(isinstance(t, Teacher))

#SUPER
print(super(type, str))