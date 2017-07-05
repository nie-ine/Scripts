#!/usr/bin/python3
# -*- encoding: UTF-8 -*-
#

import knora
import pClasses
import log

""" demo.py

Required: Python 3.0 or later
Recommended: Python 3.4 or later
"""

__version__ = "0.0.1 (20170319)"
__author__ = "Sascha Kaufmann <sascha.kaufmann@unibas.ch>"
__appname__ = "test.py"



def main():
    """
    
    :return:
    """

    log.footnote("###1. Insert LogIn and Server information:",True)
    ##
    knora_auth = ('<usr name>', '<password>');     
    server = "http://test-02.salsah.org"   

    
    ## instanziere Knora Objekt
    knora_api = knora.Knora(server=server, auth=knora_auth)
    
    
    log.footnote("###2. Specify new input content (in this example it's a string) \n Wenn man automatisiert einliest, solte man das Log dann ausstellen.")
    ##
    person_obj = pClasses.JPerson('Testperson fuer den Wiki - Eintrag')
    
    
    ## Ausgabe zur Veranschaulichung
    print("Objekt als Dictionary:\n")
    print(person_obj.get_export_data)
    print("--------\n\n")
    
    
    ## Speicher das Objekt
    resource_id = knora.store_object(knora_api, person_obj)
    print("Neues Objekt mit resource_id={} generiert".format(resource_id))
    
    
    return


if __name__ == '__main__':
    main()

