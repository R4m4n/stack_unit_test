import unittest
import os, sys
import getopt, json
from custom_logging import Logger
from stack_tests import * # All the tests from the module are imported.


if __name__ == '__main__':

    """
    Code starts from getting and analysing the arguments passed in the terminal 
    while running this file.
    Valid arguments are: unit_test.py -s <stack> -t <test> -e <element>
    """

    # Assigning default values in case no value is passed in the command.
    arg_test = "size"
    arg_value = "[1,2,3,4,5]"
    arg_element = 1
    arg_help = "{0} -s <stack> -t <test> -e <element>".format(sys.argv[0])
    
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hi:t:s:e:", ["help", "test=", "stack=", "element="])
    except:
        Logger.error(arg_help)
        sys.exit(2)
    
    # Analysing and assigning the values for each argument passed.
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            Logger.error(arg_help)
            sys.exit(2)
        elif opt in ("-t", "--test"):
            arg_test = arg
        elif opt in ("-s", "--stack"):
            arg_value = arg
        elif opt in ("-e", "--element"):
            arg_element = int(arg)

    # Entered value in the terminal will be received as string so it is dumped into list.
    stack_list = json.loads(arg_value)
    suite = unittest.TestSuite() # Object of TestSuite class is created. 
    
    """
    For each test name passed in terminal, test is added to the TestSuite class object
    and the required arguments like stack_list and element is passed.
    """
    if arg_test == 'size':
        test_name = 'test_size_of_stack'
        suite.addTest(StackSizeTest(test_name, stack_list = stack_list))
    elif arg_test == 'pop':
        test_name = 'test_pop_from_stack'
        suite.addTest(StackPopTest(test_name, stack_list = stack_list))
    elif arg_test == 'peek':
        test_name = 'test_peek_from_stack'
        suite.addTest(StackPeekTest(test_name, stack_list = stack_list))
    elif arg_test == 'empty':
        test_name = 'test_empty_from_stack'
        suite.addTest(StackEmptyTest(test_name, stack_list = stack_list))
    elif arg_test == 'push':
        test_name = 'test_push_from_stack'
        suite.addTest(StackPushTest(test_name, stack_list = stack_list, element = arg_element))
    else:
        Logger.error('Please enter the correct test name: ["size", "pop", "peek", "empty", "push"]')
        sys.exit(2)
    
    # Unit tests added in the TestSuite are called.
    unittest.TextTestRunner().run(suite) 