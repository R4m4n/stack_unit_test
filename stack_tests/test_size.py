import unittest
from custom_logging import Logger

class StackSizeFunctions():

    def __init__(self, stack_list):
        self.stack_data = stack_list

    def size(self):
        return len(self.stack_data)


class StackSizeTest(unittest.TestCase):

    def __init__(self, test_name, stack_list = [1,2,3,4,5]):
        super(StackSizeTest, self).__init__(test_name)
        self.stack_list = stack_list

    # help to create resources on a per-test basis   
    def setUp(self):
        self.stack_function = StackSizeFunctions(self.stack_list)
        
    def test_size_of_stack(self):
        Logger.info(f'\n TestCase size() \n Output =>>> {self.stack_function.size()}')