# bad_style.py - Example file with PEP8 violations

import os, sys  # E401: multiple imports on one line
import random


def calculate_sum(x,y):  # E231: missing whitespace after ','
    result=x+y  # E225: missing whitespace around operator
    return  result  # E272: multiple spaces before keyword


class myClass:  # N801: class name should use CapWords convention
    
    def __init__(self):
        self.value = 10
        self.really_long_variable_name_that_exceeds_seventy_nine_characters_limit = 100  # E501: line too long

    def badMethod(self):  # N802: function name should be lowercase
        x=5
        if x==5:  # E225: missing whitespace around operator
            print( "x is 5" )  # E201, E202: whitespace after/before parenthesis
        return x 


# E303: too many blank lines (3)
print("End of file") 
