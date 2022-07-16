import unittest
from custom_exceptions import EmptyStackException
from custom_logging import Logger


class StackEmptyFunctions():

    # Constructor function for initialising all the required variables
    def __init__(self, stack_list):
        self.stack_data = stack_list

    def empty(self):
        # Checks if the stack list is empty.
        if len(self.stack_data):
            return False
        return True


class StackEmptyTest(unittest.TestCase):

    # Constructor function for initialising all the required variables
    def __init__(self, test_name, stack_list = [1,2,3,4,5]):
        super(StackEmptyTest, self).__init__(test_name)
        self.stack_list = stack_list

    # help to create resources on a per-test basis
    def setUp(self):
        self.stack_function = StackEmptyFunctions(self.stack_list)
        
    def test_empty_from_stack(self):
        Logger.info(f'\n TestCase empty() \n Output =>>> {self.stack_function.empty()}')