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
