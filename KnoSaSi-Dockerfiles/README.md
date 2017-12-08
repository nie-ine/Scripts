Presets:

- increase memory on your device. For Mac: Docker > Preference > Memory


Setup the latest version (slower alternative)

1. Create a folder for your deployment
2. Git clone NIE-INE scripts into this folder
2. Clone Knora into Scripts/KnoSaSi-Dockerfiles/Knora, so that there is a folder Scripts/KnoSaSi-Dockerfiles/Knora/Knora
3. Change in application.conf routes for graphdb to "graphdb" and sipi to "sipi"
4. Change path to Knora/webapi/src/main in Dockerfile according to where your local version is located
5. Run script
6. Restart Knora

Setup a working version, but not the latest version (faster alternative)
--> change the "build" parts to image, execute docker-compose

you have to create a folder with the folders as well.

add sipi to hostnames