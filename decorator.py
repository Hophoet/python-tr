import time

def deco(fun):
    print('runing deco')
    #defined inner function
    def inner(*args, **kwargs):
        print('runing inner()')
        fun(*args, **kwargs)
    return inner

def timer(fun):
    def inner(*args):
        t0 = time.perf_counter()
        result = fun(*args)
        t1 = time.perf_counter()
        args_str = ' ,'.join(repr(arg) for arg in args)
        fun_name = fun.__name__
        runtime = t1 - t0
       	print(f'{fun_name}({args_str})  runtime({runtime}) ===> {result}')
    return inner

@timer
@deco
def test_function():
    print('runing test_function')


