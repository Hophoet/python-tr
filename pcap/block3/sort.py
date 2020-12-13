liste = [4, 8, 0, 2]
persons = [{'name': 'lili', 'age':45}, {'name':'hophoet', 'age':21}]
print('liste', liste)
print('persons', persons)
liste.sort()
persons.sort(key=lambda x: x.get('age'))
print('liste after the call of sort', liste)
print('persons after the call of sort(using key param)', persons)
