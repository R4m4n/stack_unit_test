# Stack Unit Test

No external installation is required to tun this code.

To run the code you need to run the file `unit_test.py` in the root folder. There are certain arguments that you can pass to send the arguments while running this file from CLI.

For example:
`unit_test.py -s <stack> -t <test> -e <element>`

where,

-s is the stack which is required to be a list. e.g. [1,2,3,4]

-t is the test which runs the different test cases on the stack list passed. Test values are: `["size", "pop", "peak", "empty", "push"]`

-e is the value of element which is required in case of push. User can pass the value he needs to push to the stack.

Note: If no argument is passed then a size operation is ran on a default list `[1,2,3,4,5]`

File structure of the code:
```
.
./unit_test.py
./stack_tests
./stack_tests/__init__.py
./stack_tests/test_size.py
./stack_tests/test_peek.py
./stack_tests/test_pop.py
./stack_tests/test_push.py
./stack_tests/test_empty.py
./custom_exceptions.py
./custom_logging.py
./README.md
./.gitignore
```

Code starts from the `unit_test.py` file. 'stack_tests' directory is create as the test module containing all the test cases which are directly imported in the `unit_test.py`.

Two files `custom_exceptions.py` and `custom_logging.py` are being used as helper classes to provide the functionality whenever is needed.

Each file has a StackTest class inheriting `unittest.TestCase` for each test case and StackFunction class which is running all the required functionality in the task.

Every StackFunction has the Interface Struct methods like `size(), pop(), peak(), empty(), push()`, and returns the output to be logged in the terminal.

### I have added the comments in the code for better understanding :).