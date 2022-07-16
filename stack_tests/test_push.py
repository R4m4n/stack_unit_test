import unittest
from custom_exceptions import EmptyStackException
from custom_logging import Logger

class StackPushFunctions():

    def __init__(self, stack_list, element):
        self.stack_data = stack_list
        self.element = element

    def push(self):
        if self.element == None:
            raise(EmptyStackException('Entered element cannot be null.'))
        self.stack_data.append(self.element)
        return self.stack_data


class StackPushTest(unittest.TestCase):

    def __init__(self, test_name, stack_list = [1,2,3,4,5], element = 3):
        super(StackPushTest, self).__init__(test_name)
        self.stack_list = stack_list
        self.element = element

    # help to create resources on a per-test basis
    def setUp(self):
        self.stack_function = StackPushFunctions(self.stack_list, self.element)
        
    def test_push_from_stack(self):
        Logger.info(f'\n TestCase push() \n Output =>>> {self.stack_function.push()}')