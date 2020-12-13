import time
import decorator
import closure

@decorator.timer
def loop():
    # for num in range(1000):
    time.sleep(5)

if __name__ == '__main__':
    print('main as script')
    decorator.test_function()
    loop()
    #avg = closure.Average()
    avg = closure.average_function()
    avg(40)
    avg(4)
else:
    print('main as module')

