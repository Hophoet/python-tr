def generator():
    for nb in range(10):
        yield nb

gen = generator()
print('Generator', gen)
print('list', list(gen))
