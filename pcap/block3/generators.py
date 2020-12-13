
def getDataItems(data):
    for item in data:
        yield item
    

data = getDataItems('life easy to others'.split(' '))

print(next(data))