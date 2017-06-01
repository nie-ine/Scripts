import knora
import pClasses
import importlib
import csv

def sendToKnora(username, password, server, resourceName, propertyList, wholeValueList):
    
    knora_auth = (username, password)
    knora_api = knora.Knora(server=server, auth=knora_auth)
    
    path = "tablesCSV/" + resourceName + ".csv"
    with open(path, 'w') as f:
        writer = csv.writer(f, delimiter=',')
    
        #print("------")
        #extract Set from WholeValueList:
        #print("\nPropertyList in sendToKnora: {}\n".format(propertyList))
        
        i = 0
        for i in range (len(wholeValueList[i])):
            valueList = []
            for j in range (len(wholeValueList)):
                valueList.append(wholeValueList[j][i])
            person_obj = pClasses.GenericClass(resourceName, propertyList, valueList)
            print(person_obj.get_export_data)
            resource_id = knora.store_object(knora_api, person_obj)
            print("Neues Objekt mit resource_id={} generiert".format(resource_id))
            
            data = []
            data.append(resourceName)
            for i in range(len(propertyList)):
                data.append(propertyList[i])
                data.append(valueList[i])
            data.append(resource_id)
            
    
            writer.writerow(data)
        
    
        #print("------")
    
    
    
    return None