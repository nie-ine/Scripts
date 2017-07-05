##Knora.py
Hier wird eine Klasse "Knora" definiert, der du beim Initialisieren nur den Server und ein Tupel mit (<Username>, <Password>) uerbergeben musst.


Danach kannst Du mit mit Knora.post() Daten in Knora speichern, bzw. mit Knora.get() Daten aus Knora herauslesen (get() muss ich noch anpassen, damit es funktioniert). Die post-Methode verlangt die Daten als Dictionary.
Diese Methoden sind low-level. Daher gibt es die Funktion "store_object(<storage_object>). Wenn Du Ihr ein zu speicherndes Objekt uebergibst, kuemmert sie sich um den Rest und gibt Dir, falls erfolgreich, die ResourceID der neu angelegten Resource zurueck.


##pClasses.py
In pClasses.py findest Du hierzu die Klassen Person und JPerson als Beispiel. Letztere sollte Deine Testresource abbilden.

##test.py
test.py ist ein Beispiel. Um es laufen zu lassen, musst Du noch Deinen Usernamen und Password im Tupel knora_auth setzen (Zeile 26). Es sollte Dir eine neue Resource anlegen.