#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__author__ = 'Xiuhua Ke'
__email__ = "xiuhua.ke@mail.utoronto.ca"
__copyright__ = "2014 Xiuhua Ke"

# imports one per line

def checksum(upc):
    """
    Checks if the digits in a UPC is consistent with checksum

 :param upc: a 12-digit universal product code

    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a string
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise:
    # TypeError (if paramiter is not a string)
    if type(upc) is not str:
        raise(TypeError())

    # check length of string
    # raise ValueError if not 12
    if len(upc) != 12:
        raise(ValueError())

    # convert string to array
    # hint: use the list function

    # generate checksum using the first 11 digits provided
    upcList = list(upc)

    odd = int(upcList[0]) + int(upcList[2]) + int(upcList[4]) + int(upcList[6]) + int(upcList[8]) + int(upcList[10])
    even = int(upcList[1]) + int(upcList[3]) + int(upcList[5]) + int(upcList[7]) + int(upcList[9])
    result = even + odd * 3

    modulo = result % 10

    if modulo != 0:
        result = 10 - modulo

    # check against the the twelfth digit
    if result == int(upc[11]):
        return True

    # return True if they are equal, False otherwise

    return False

print(checksum("036000291452"))