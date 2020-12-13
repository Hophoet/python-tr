numbers = [8, 4, 3, 2, 34]
filtedNumbers = filter(lambda x:x<10 , numbers)

print('numbers', numbers)
print('filted numbers', list(filtedNumbers))
