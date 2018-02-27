#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

import .from .hasValue import HasValue

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


class IntValue(HasValue):  # Subclass int to get handy functions
    """

    """

#    def __new__(cls, integer):
#        return super().__new__(int(integer))

    def __init__(self, integer):
        #if integer is not None:
        super().__init__(int(integer))
        #else:
        #    super().__init__(None)
        self._name = "IntValue"
        self._value_type = "int_value"

    #def __repr__(self):
    #    return json
    #    return """[{{'int_value': {:d}}}]""".format(super().__repr__())

    #def __str__(self):
    #    return """[{{'int_value': {:d}}}]""".format(super().__int__())

    def json(self):
        """

        :return:
        """
        if self._value or self._value == 0:
            return [{self._value_type: self._value}]