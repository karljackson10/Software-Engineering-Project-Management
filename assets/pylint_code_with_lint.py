"""
Some Module
"""
# from math import pi
# from time import time

SOME_GLOBAL_VAR = 'GLOBAL VAR NAMES SHOULD BE IN ALL_CAPS_WITH_UNDERSCOES'

def multiply(x, y):
    """
    This returns the result of a multiplation of the inputs
    """
    # some_global_var = 'this is actually a local variable...'
    result = x* y


    if result == 777:
        print("jackpot!")

    return result

def is_sum_lucky(x, y):
    """This returns a string describing whether or not the sum of input is lucky
    This function first makes sure the inputs are valid and then calculates the
    sum. Then, it will determine a message to return based on whether or not
    that sum should be considered "lucky"
    """
    if x is not None:
        if y is not None:
            result = x+y
            if result == 7:
                return 'a lucky number!'
            #else:
            return 'an unlucky number!'

        return 'just a normal number'
    return 'x has no value'

class SomeClass:
    """
    Some Class
    """
    def __init__(self, some_arg,  some_other_arg # , verbose = False
                 ):
        self.some_other_arg  =  some_other_arg
        self.some_arg        =  some_arg
        # list_comprehension = [((100/value)*pi) for value in some_arg if value != 0]
        # time = time()
        # from datetime import datetime
        # date_and_time = datetime.now()
        # return
    def method_1 (self):
        """
        method 1
        """
        return

    def method_2 (self):
        """
        method 2
        """
        return
    