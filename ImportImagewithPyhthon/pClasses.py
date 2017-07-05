#!/usr/bin/python3
# -*- encoding: UTF-8 -*-
#

import log

"""pClasses.py

An example of how someone can use classes to store data in Knora

Required: Python 3.0 or later
Recommended: Python 3.4 or later
"""

__version__ = "0.0.2"
__author__ = "Sascha Kaufmann <sascha.kaufmann@unibas.ch>"
__appname__ = "pClasses.py"

import mimetypes
import re
import sys
import traceback
import os

from html.parser import HTMLParser

_ENCODING = 'utf-8'
_PROJ_PREFIX = "nie-ine"
_SEQNUM = 1
_MAX_STORE_ATTEMPTS = 7

_DEBUG = True

# Tools



# Classes

class PCBase(object):
    def __init__(self):
        self._PROJ_PREFIX = _PROJ_PREFIX
        self._RESOURCE_ID = None
        return

    @property
    def get_export_data(self):
        data = {}
        try:
            knora_properties = ["part_of", "seqnum"]
            code = self._PROJ_PREFIX
            properties = {}
            for key, value in iter(self.__dict__.items()):
                if key.startswith('_') or value is None:
                    continue
                prop = "salsah:{:s}".format(key) if key in knora_properties else "{:s}:{:s}".format(code, key)
                properties[prop] = [{'value': item} for item in value] if isinstance(value, list) else {'value': value}
            data = {'restype_id': "{:s}:{:s}".format(code, self._RESTYPE), 'properties': properties} if properties else {}
        except Exception as e:
            print(e)
        return data

    def set_resid(self, value):
        self._RESOURCE_ID = value

    def get_resid(self):
        return self._RESOURCE_ID


class Person(PCBase):
    def __init__(self, name, vorname, image=None):
        """
        image = path(name) to local image (e.g. //root/home/abc/image.jpg)
        """
        super(Person, self).__init__()
        global _SEQNUM
        self._PROJ_PREFIX = _PROJ_PREFIX
        self._RESTYPE = Person.__name__.lower()
        self._RESOURCE_ID = None
        self._IMAGE = image

        self.name = name
        self.vorname = vorname
        self.seqnum = _SEQNUM
        _SEQNUM += 1
        return


class JPerson(PCBase):
    def __init__(self, name):
        super(PCBase, self).__init__()
        global _SEQNUM
        
        log.footnote("###4. Specify project prefix in header")
        self._PROJ_PREFIX = _PROJ_PREFIX
        
        log.footnote("###5. Specify name of the resource")
        self._RESTYPE = "JansImageResource"
        self._RESOURCE_ID = None
        
        log.footnote("###6. Specify image path here if the resource has one.")
        
        image="/Users/system/Desktop/logo.jpg"
        
        """
        image = path(name) to local image (e.g. //root/home/abc/image.jpg)
        """
        self._IMAGE = image


        log.footnote("###7. Specify name of property (in this example it's hasName)")
        self.hasName = name
        self.seqnum = _SEQNUM
        _SEQNUM += 1
        return



