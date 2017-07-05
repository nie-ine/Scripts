#!/usr/bin/python
# -*- coding: utf-8 -*-

__version__ = "0.0.2 (20160319)"
__author__ = "Sascha Kaufmann <sascha.kaufmann@unibas.ch>"
__appname__ = "knora.py"


import collections
import json
import sys
import time
import traceback
from collections import namedtuple
import mimetypes

import requests
from requests.adapters import HTTPAdapter


_SERVER = "http://test-02.salsah.org/"
_GET_PATH = "/api/selections"
_POST_PATH = "/api/resources"
_SELECTION_PATH = "/api/selections/"
_MAX_RETRIES = 10                    # max. number of retries for a request
_TIMEOUT = 5                         # Session timeout in seconds
_AUTH = ("<USER>", "<PASSWORD>")     # as an example
KnoraAuth = namedtuple('Auth', 'User Password')


class Knora(object):
    ## Initialisierung der Objektattribute
    def __init__(self, server, auth=None):
        self._POST_HEADER = {'content-type': 'application/json'}
        self.post_url = "{}{}".format(server, _POST_PATH)
        self.get_url = "{}{}".format(server, _GET_PATH)
        self.session = requests.Session()
        self.session.auth = auth
        self.session.mount(server, HTTPAdapter(max_retries=_MAX_RETRIES))
        self.session.timeout = _TIMEOUT

    ## Hier bessert Sascha dann noch nach
    def get(self, url=None, *args):
        if url:
            try:
                result = self.session.get(url)
                result.raise_for_status()
                return result.json()
            except Exception as e:
                print(e)
        return None

    ## daten werde mit dieser methode hochgeladen, durch die Methode weiter unten store_object
    def post(self, data_dict, image=None):
        try:
            headers = None
            files = None
            data = json.dumps(data_dict)
            if image:
                data = {'json': data}
                filename = (image.get('filename').split('/'))[-1]
                files = {'file': (filename, open(image.get('filename'), 'rb'), image.get('mime'))}
            else:
                headers = self._POST_HEADER

            r = self.session.post(self.post_url, headers=headers, data=data, files=files)
            r.raise_for_status()
            result = r.json()
            return result.get('res_id') if result.get('status') == 0 else None
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
            time.sleep(1) # delays for 1 seconds
        return None

    def get_selection_properties(self, selection_id):
        try:
            KNORA_SELECTIONS_URL = ""
            r = self.session.get(KNORA_SELECTIONS_URL + selection_id)
            r.raise_for_status()
            result = r.json()
            return result.get('selection') if result.get('status') == 0 else None
        except Exception:
            exc_type, exc_value, exc_traceback = sys.exc_info()
            traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
        return None

## Diese Methode wird aufgerufen in test.py
def store_object(knora, storage_obj):

    resource_id = None
    try:
        if storage_obj.get_export_data:
            ## Schauen, ob das storage_obj ein _Image dabeihat.
            ## Bei dem Hochladen eines Bildes muss dass spezifiziert werden
            if getattr(storage_obj, '_IMAGE', None):
                mimetype = mimetypes.types_map[".{:s}".format(storage_obj._IMAGE.split('.')[-1])]
                image = {'filename': storage_obj._IMAGE, 'mime': mimetype}
            else:
                image = None
            for attempt in range(0, _MAX_RETRIES):
                resource_id = knora.post(storage_obj.get_export_data, image)
                if resource_id:
                    break
            else:
                print("Objekt konnten nicht gespeichert werden")
                print(obj.get_export_data)
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        traceback.print_exception(exc_type, exc_value, exc_traceback, limit=2)
        resource_id = None
    return resource_id

