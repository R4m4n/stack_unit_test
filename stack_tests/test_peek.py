import unittest
from custom_exceptions import EmptyStackException
from custom_logging import Logger


class StackPeekFunctions():

    def __init__(self, stack_list):
        self.stack_data = stack_list

    def peek(self):
        if not len(self.stack_data):
            raise(EmptyStackException('Cannot run peek, stack is empty.'))
        return self.stack_data[-1]


class StackPeekTest(unittest.TestCase):

    def __init__(self, test_name, stack_list = [1,2,3,4,5]):
        super(StackPeekTest, self).__init__(test_name)
        self.stack_list = stack_list

    # help to create resources on a per-test basis
    def setUp(self):
        self.stack_function = StackPeekFunctions(self.stack_list)
        
    def test_peek_from_stack(self):
        Logger.info(f'')
        Logger.info(f'\n TestCase peek() \n Output =>>> {self.stack_function.peek()}')