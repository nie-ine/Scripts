## Get Knora, Salsah, Sipi and GraphDB up and running with Docker

###Attention: Ontologies in GraphDB are not stored in a persistent way yet.  This will be the next step and will come soon.

### Prerequisites:
 - Install Docker
 - Increase Memory and CPUs that Docker is allowed to use. It works with 10 GB, maybe less as well.
	 - 	Mac: Go to Docker > Preferences > Advanced
	 - If images stop running without an explanation, you might need to increase the memory a little bit more.

### Deployment alternatives
You can find two alternatives here to perform the deployment.

1. Fast and recommended alternative: Go to the KnoSaSi-PrebuiltImages - Folder and follow the instructions below. This alternative will pull all images from Dockerhub and get them up and running.
2. Slow alternative: To be sure to get the latest version of all parts of the software, you can built all images "from scratch" on your machine as well. Stay in the current directory and follow the instructions below.

After you have chosen your alternative, only perform the instructions that are necessary as indicated below for the alternative that you have chosen.

|   | Instructions   | Alternative 1| Alternative 2  |
|--:| ------------- |:-------------:| :-----:        |
| 1 | Git clone NIE-INE Scripts | x | x |
| 2 | Git clone Knora into Scripts/KnoSaSi-Dockerfiles/Knora, so that there is a folder Scripts/KnoSaSi-Dockerfiles/Knora/Knora  | x | x |
| 3 | Knora/webapi/src/main/resources/application.conf - change hostname for graphdb to "graphdb" and sipi to "sipi", both are localhost before this change.|  | x |

To finalise the setup...

|   | Instructions   | Alternative 1| Alternative 2  |
|--:| ------------- |:-------------:| :-----:        |
| 4 | Map the name sipi to the ip address of localhost your in /etc/hosts file. e.g. next to localhost the name sipi should be mapped to the same ip adress as localhost. | x | x |
| 5 | Start the containers: docker-compose up | x | x |
| 6 | After GraphDB is running: cd to Knora/webapi/scripts and execute the script ./graphdb-free-init-knora-test.sh | x | x |
| 7 | Restart Knora: docker restart "container id of Knora". You find the container id of the knora container by typing "docker ps". | x | x |
| 8 | Execute the import Script in ImportPictureTest with python3. Before, change the label in the python script on line 10 to an individual name. If you get a json with the resource back from knora after executing the code and if you can find the resource and the picture in Salsah using the full text search searching for the given label, your setup is working. | x | x |

The services are available at:

 - Sipi: localhost:1024
 - Knora: localhost:3333
 - GraphDB: localhost:7200
 - Salsah: localhost:4200

 
If you would like to stop the containers:

 - If you press ctrl+c twice, docker will force containers to stop, the containers wont be deleted though. Since the imported data for the triple store is not saved persistently yet, this option saves the data in the container as well.
 - docker-compose down stops and deletes all containers.