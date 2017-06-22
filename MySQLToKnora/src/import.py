#use python3

import mysql.connector
import os
import sys
import subprocess
import csv
import pClasses
import knora

from sendToKnora import sendToKnora



_ENCODING = 'utf-8'
_PROJ_PREFIX = "nie-ine"                      #Enter your project prefix
_KNORA_USR_NAME = "stoffregen"                    #Enter your credentials here
_KNORA_PASSWORD = "nie-stoffregen-ine"                 #Enter your credentials here
_KNORA_SERVER = 'http://test-02.salsah.org/'                 #Enter the URL of the Knora Instance here

def get_db_connection():
    try:
        cnx = mysql.connector.connect(user='root',
                                      password='',
                                      host='127.0.0.1',
                                      database='c9')
    except Exception:
        cnx = None

    return cnx


def read_csv(filename):
    data = None
    try:
        with open(filename, 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
    except Exception:
        data = None

    return data


def read_mapping(filename):
    mapping = read_csv(filename)
    try:
        del mapping[0]
    except Exception:
        mapping = None

    return mapping


def determine_property_column(data, property):
    """
    param data: table in form of a list of lists
    """
    
    column = -1
    try:
        for i in range(len(data)):
            column = -1
            for j in range(len(data[i])):
                if(str(data[i][j]) == property):
                    column = j
            if (column != -1): 
                break
    except:
        column = -1
    
    return column


def main():
    cnx = get_db_connection()
    if not cnx:
        print("Couldn't establish a database connection")
        return

    print ("1.0 Please rename your SQL dump file to dump.sql and upload it to this workspace.")
    
    if os.path.isfile('dump.sql'):
        print(" - File dump.sql found")     
    else: 
        print("File dump.sql not found")
        return
        
    #os.system('mysql-ctl start')
    os.system('mysql -u root c9 < dump.sql')
        
    mapping = read_mapping('mapping.csv')
    if not mapping:
        print("mapping file not found or empty!")
        return
    else:
        print ("\n 0. Mapping has been read successfully: \n{} ".format(mapping))


    currentTable = ""
    wholeListCheck = None
    propertyCheck = None
    resourceCheck = None
    
    print("\n 1. Import Data to Knora\n")
    
    for row in mapping:
        propertyList = []
        
        #print("----")
        if (row[0] != currentTable):
            #print("New Table found. Create CSV")
            currentTable = row[0]
            #csvFile = "> tablesCSV/" + currentTable + ".csv" 
            #rmCSV = "rm tablesCSV/" + currentTable + ".csv"
            #os.system(rmCSV)
            #os.system(csvFile)
            wholeList = []

        column = row[1]
        #print("Column in MySQL: {}".format(column))
        
        resourceName = row[2]
        #print("ResourceName in Knora: {}".format(resourceName))
        
        
        #find all properties for this resource
        for rowTwo in mapping:
            if(rowTwo[2]==resourceName):
                propertyList.append(rowTwo[3])
        #print("PropertyList for Knora: {}".format(propertyList))
        
        
        mySQLColumnList = []
        for rowTwo in mapping:
            if(rowTwo[2]==resourceName):
                mySQLColumnList.append(rowTwo[1])
        #print("mySQLColumnList for Knora: {}".format(mySQLColumnList))
        
        valueForKnoraList = []
        numberOfRows = 0
        
        mysqlStatement = "SELECT {:s} from {:s} ORDER BY id".format(row[1], currentTable)
        
        helpList = []
        
        cursor = cnx.cursor()
        cursor.execute(mysqlStatement)
        for value in cursor:
            helpList = ''.join(map(str, value))
            valueForKnoraList.append(helpList)
        
        wholeList.append(valueForKnoraList)            
        #print(wholeList)
        
        if(wholeList != wholeListCheck):
            if(wholeListCheck == None):
                wholeListCheck = wholeList
            else:
                #execute mySQL - Statement
                resourceId = sendToKnora(_KNORA_USR_NAME,
                                         _KNORA_PASSWORD,
                                         _KNORA_SERVER,
                                         resourceCheck,
                                         propertyCheck,
                                         wholeListCheck
                                        )
                #print(propertyCheck)
        propertyCheck = propertyList
        wholeListCheck = wholeList
        resourceCheck = resourceName
    
    #nicht schoen aber selten, dieser Aufruf fuer die letzte Resource des Mappings
    resourceId = sendToKnora(_KNORA_USR_NAME,
                             _KNORA_PASSWORD,
                             _KNORA_SERVER,
                             resourceName,
                             propertyCheck,
                             wholeListCheck
                            )

    cursor.close()
    cnx.close()
    
    
    #                       #
    #   Link Resources      #
    #                       #
    
    
    print("\n2. Link imported Data\n")
    
    for row in mapping:
        if(row[4] != ""):
            thisProperty = row[3]
            resourceName = row[2]
            linkedToProperty = row[5]
            linkedToResource = row[4]
            
            print("Die Property {} der Resource {} ist linked zur Resource {}".format(thisProperty, resourceName, linkedToResource))
            
            parentTableCSV = "tablesCSV/{:s}.csv".format(resourceName)
            childTableCSV = "tablesCSV/{:s}.csv".format(linkedToResource)
            
            parentList = read_csv(parentTableCSV)
            if not parentList:
                print("File '{:s}' doesn't exist or is empty!")
                return

            childList = read_csv(childTableCSV)
            if not childList:
                print("File '{:s}' doesn't exist or is empty!")
                return
           
            parent_column = determine_property_column(parentList, thisProperty)
            #TODO: the following block might be deleted in case the assert will pass
            for i in range(len(parentList)):
                parentColumn = -1
                for j in range(len(parentList[i])):
                    if(str(parentList[i][j]) == thisProperty):
                        parentColumn = j
                if (parentColumn != -1): 
                    break
            assert(parent_column == parentColumn)
          
            child_column = determine_property_column(childList, linkedToProperty)
            #TODO: the following block might be deleted in case the assert will pass
            for i in range(len(childList)):
                childColumn = -1
                for j in range(len(childList[i])):
                    if(str(childList[i][j]) == linkedToProperty):
                        childColumn = j
                if (childColumn != -1): 
                    break                 
            assert(child_column == childColumn)
                    
            #print("ParentColumn: {}".format(parentColumn))
            #print("ChildColumn: {}".format(childColumn))
            
            for parent in parentList:
                linkVariable = parent[parentColumn+1]
                #print("\nLinkvariable: {}".format(linkVariable))
                for child in childList:
                    #print("Childvariable: {}".format(child[childColumn+1]))
                    if (child[childColumn+1] == linkVariable):
                        childResourceID = child[len(child)-1]
                        parentResourceID = parent[len(parent)-1]
                        print("Parent {} with ResourceID {} has to be linked with Child {} with ResourceID {}".format( parent[len(parent)-2], parentResourceID , child[len(child)-2], childResourceID))
                        propertyName = _PROJ_PREFIX + ":" + thisProperty
                        #print (propertyName)
                        
                        knora_auth = (_KNORA_USR_NAME, _KNORA_PASSWORD)
                        knoraInstance = knora.Knora(server=_KNORA_SERVER, auth=knora_auth)
                        knoraInstance.update_resource_property(parentResourceID, propertyName, childResourceID)    
    
if __name__ == '__main__':
    sys.exit(main())