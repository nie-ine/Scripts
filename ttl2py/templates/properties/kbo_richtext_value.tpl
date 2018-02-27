#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


"""
RichtextValue: definition of a datatype to handle Knora Base Ontology (KBO) text
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class RichtextValue(str):  # Subclass string to get handy functions
    """

    """

    def __new__(cls, string):
        if string is not None:
            return super(RichtextValue, cls).__new__(cls, string)
        return None

    def __init__(self, string):
        super(RichtextValue, self).__init__()

    def __repr__(self):
        return """[{{'richtext_value': {{'utf8str': "{:s}"}}}]""".format(super().__repr__())

    def __str__(self):
        return """[{{'richtext_value': {{'utf8str': "{:s}"}}}]""".format(super().__str__())

    def json(self):
        return [{'richtext_value': {'utf8str': super().__str__()}}]
