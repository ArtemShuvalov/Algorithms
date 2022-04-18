# Problem 1
class MinQueueStack:
    '''
    A class to represent a queue based on 2 stack with min support
    Attributes:
        queue (str) - stack to store current values
        queue_min (str) - stack to store min values
    Methods:
        push(self, val) - Add the values to the beginning with O(1).
        pop(self) - Remove value from the end with O(1).
        get_min(self) -  Return min value with O(1).
        get_max(self) -  Return max value with O(1).
    '''

    def __init__(self):
        '''
        Initialize objects to store current and min values
        Args:
            None
        Outputs:
            None
        '''
        self.queue = []
        self.queue_min = []

    def push(self, val) -> None:
        '''
        Add the values to the beginning with O(1).
        Args:
            val (any) - value to add
        Outputs:
            None
        '''
        # Add values to queue
        self.queue.append(val)
        # If the size of queue is not 0, update new min
        while len(self.queue_min) > 0 and self.queue_min[-1] > val:
            self.queue_min.pop(0)
        # Otherwise, add value
        self.queue_min.append(val)

    def pop(self) -> int:
        '''
        Remove value from the end with O(1).
        Args:
            None
        Outputs:
            val (int) - popped value
        '''
        val = self.queue.pop(0)

        if self.queue_min[0] == val:
            self.queue_min.pop(0)
        return val

    def get_min(self):
        '''
        Return min value with O(1).
        Args:
            None
        Outputs:
            val (int) - min value
        '''
        return self.queue_min[0]
    def get_max(self) -> None:
        '''
        Return max value with O(1).
        Args:
            None
        Outputs:
            val (any) - min value
        '''
        return self.queue_min[-1]

def max_string(str_list: list) -> None:
    '''
    Function to get maximum of the list of the strings
    Args:
        str_list (list) - gets the list of strings
    Outputs:
        max_element(str) - maximum string
    '''

    queue = MinQueueStack()
    for element in str_list:
        queue.push(element)

    print(queue.get_max())

max_string(['aba', 'baa'])

### LRU Cache Decorator
import pickle
def lru_cache(function, cache_size=None):
    if isinstance(function, int):
        def wrapper(f):
            return lru_cache(f, function)
        return wrapper

    cache = {}
    keys = []

    def wrapper(*args, **kwargs):
        key = pickle.dumps((args, kwargs))
        try:
            keys.append(keys.pop(keys.index(key)))
        except ValueError:
            cache[key] = function(*args, **kwargs)
            keys.append(key)
            if cache_size is not None and len(keys) > cache_size:
                del cache[keys.pop(0)]
        return cache[key]
    return wrapper

@lru_cache(10)
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

@lru_cache(2)
def foo(value):
    print(f'calculate foo for {value}')
    return value

print(fib(498))
foo(1)
foo(2)
foo(1)
foo(2)
foo(3)
foo(1)

def types(*types):
    def check_types(function):
        assert len(types) == function.__code__.co_argcount

        def new_function(*args, **kwds):
            for (a, t) in zip(args, types):
                try:
                    assert isinstance(a, t), f"Argument {a} does not match the type {t}"
                except AssertionError:
                    raise TypeError(f"Argument {a} does not match the type {t}")
            return function(*args, **kwds)
        new_function.__name__ = function.__name__
        return new_function
    return check_types

@types(int, (int,float))
def addition(a, b):
    return a + b

addition(3, 2)
addition(3, '2')
