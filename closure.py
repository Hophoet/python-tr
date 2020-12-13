
class Average:
    def __init__(self):
        self.series = []
    def __call__(self, serie):
        self.series.append(serie)
        avg = sum(self.series)/len(self.series)
        print(f'AVG: {avg}')

def average_function():
    count = 0
    total = 0

    def average(serie):
        nonlocal count, total
        count += 1
        total += serie
        avg = total/count
        print(f'AVG: {avg}')
        return avg

    return average

