#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasValue import HasValue
"""
DateValue: definition of a datatype to handle Knora Base Ontology (KBO) dates
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class HasDate(HasValue):  # Subclass int to get handy functions
    """

    """

    def __init__(self, date_string):
        """

        :param string:
        """
        super(HasDate, self).__init__(date_string)

    def __repr__(self):
        """

        :return:
        """
        return """['date_value': 'GREGORIAN:{:s}']""".format(self._value)

    def __str__(self):
        """

        :return:
        """
        return """['date_value': 'GREGORIAN:{:s}']""".format(self._value)

    def json(self):
        """

        :return:
        """
        if self._value:
            return [{'date_value': 'GREGORIAN:{:s}'.format(self._value)}]
        return None
