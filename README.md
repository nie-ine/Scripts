# Scripts
In the [NIE-INE](http://www.fee.unibas.ch/nie_ine.html) project an infrastructure is developed to ensure long-term storage of data of scientific edition projects in the Humanities at the University of Basel.  
For this purpose the existing platform [Knora-SALSAH](https://github.com/dhlab-basel/Knora) of the [Digital Humanities Lab](https://github.com/dhlab-basel) is used.  
The essence of the infrastructure is that data, stored in e.g. a MySQL relational database, are converted to a different machine-readable format, i.e. one that makes the semantics of the data explicit.  
In the development stage (see figure 1) a series of vocabularies or ontologies is created that will be used to express the data. These semantic models adhere to the [model theory of W3C RDF, RDFS](https://www.w3.org/TR/2002/WD-rdf-mt-20020429/), and [OWL Full](https://www.w3.org/TR/owl-semantics/).  
Further a comma-separated values (CSV)-file is created to enable the mapping between the old (e.g. MySQL) and the new (RDF/S-OWL) data format.  
A script written in Python will use at runtime the CSV-mapping file to convert the original data to a JSON (JavaScript Object Notation) format, which in turn will pass via a REST (Representational state transfer) Web service the Knora API, and finally be stored in an RDF graph database (triple store).  
![figure](https://github.com/nie-ine/Scripts/blob/master/MySQL-migration.png)
