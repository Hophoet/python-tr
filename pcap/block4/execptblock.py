

def divide_by(x, y):
    """ division function """
    try:
        print('execute try...')
        result = x/y 
    except Exception as error:
        print('execute except...')
        print('Error', error)
        
    else:
        print('execute self...')
        print('result from try', result)

    finally:
        print('execute finally...')


def raise_not_enough(number):
    if number < 10:
        raise ValueError
def assert_not_enough(number):
    assert number >= 10

# divide_by(4, 3)
# divide_by(4, 0)

# raise_not_enough(7)
# raise_not_enough(10)

# assert_not_enough(8)
# assert_not_enough(10)