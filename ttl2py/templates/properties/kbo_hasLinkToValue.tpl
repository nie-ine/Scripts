#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

from .hasValue import HasValue

"""
hasLinkToValue: definition to handle Knora Base Ontology (KBO)
"""

__author__ = "Sascha Kaufmann (sascha.kaufmann@unibas.ch)"
__copyright__ = "Copyright 2017, 2018; NIE-INE (nie-ine.ch)"
__credits__ = [""]
__license__ = "Apache License, Version 2 [https://www.apache.org/licenses/LICENSE-2.0.html]"
__version__ = "0.0.1"
__maintainer__ = "NIE-INE (nie-ine.ch)"
__email__ = "sascha.kaufmann@unibas.ch"
__status__ = "Prototype"


class HasLinkToValue(HasValue):  # Subclass int to get handy functions
    """

    """

    def __init__(self, link):
        """

        :param string:
        """
        super(HasLinkToValue, self).__init__(link)

    def __repr__(self):
        """

        :return:
        """
        try:
            return """['link_value': '{:s}']""".format(self._value)
        except TypeError:
            return

    def __str__(self):
        """

        :return:
        """
        try:
            return """['link_value': '{:s}']""".format(self._value)
        except TypeError:
            return

    def json(self):
        """

        :return:
        """
        try:
            return [{'link_value': '{:s}'.format(self._value)}]
        except TypeError:
            return