import unittest
from custom_exceptions import EmptyStackException
from custom_logging import Logger


class StackPopFunctions():

    def __init__(self, stack_list):
        self.stack_data = stack_list

    def pop(self):
        if not len(self.stack_data):
            raise(EmptyStackException('Cannot run pop, stack is empty.'))
        return self.stack_data.pop(-1)


class StackPopTest(unittest.TestCase):

    def __init__(self, test_name, stack_list = [1,2,3,4,5]):
        super(StackPopTest, self).__init__(test_name)
        self.stack_list = stack_list
    
    # help to create resources on a per-test basis
    def setUp(self):
        self.stack_function = StackPopFunctions(self.stack_list)
        
    def test_pop_from_stack(self):
        Logger.info(f'\n TestCase pop() \n Output =>>> {self.stack_function.pop()}')