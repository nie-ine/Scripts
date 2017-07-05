import os

def footnote(contentToPrint, firstValue=False):
    
    switchOn = 1
    
    if switchOn == 1:
        
        fileName = "md/Documentation.md"
        if os.path.isfile(fileName):
        
            if firstValue == True:
                os.remove(fileName)
            
        
        print ('\n --- Log Info: %s --- \n' % contentToPrint)
        
        md_file = open(fileName, "a")
        md_file.write('%s\n' % contentToPrint)