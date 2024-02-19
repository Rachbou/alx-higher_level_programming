#!/usr/bin/python3
# 100-my_int.py
# Rachid BOULMANI
"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """
    a class MyInt that inherits from int
    MyInt is a rebel. MyInt has == and != operators inverted
    """

    def __eq__(self, OtherInt):
        """
        defining == as !=
        """
        
        if self.real == OtherInt:
            return (False)
        return (True)

    def __ne__(self, OtherInt):
        """
        defining != as ==
        """
        
        if self.real == OtherInt:
            return (True)
        return (False)
