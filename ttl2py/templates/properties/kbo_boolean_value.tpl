#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


"""
IntValue: definition of a datatype to handle Knora Base Ontology (KBO) integers
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class BooleanValue:  # Subclass int to get handy functions
    """

    """

#    def __new__(cls):
#        return super(BooleanValue, cls).__new__(cls, bool)

    def __init__(self, boolean):
        self._value = boolean
#        return super(BooleanValue, self).__init__()

    def __repr__(self):
        return """[{{'boolean_value': {}}}]""".format(self._value)

    def __str__(self):
        return """[{{'boolean_value': {}}}]""".format(self._value)
