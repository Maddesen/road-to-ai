
## Variables store values.

name =  "Maddy" #String = Wörter/Buchstaben
print(name) # Werte ausgeben
alter = 40 #Integer = ganze Zahlen
print(alter) # Werte ausgeben
# Casting  = Umwandlung von einem Datentyp in einen anderen
alter_str = str(alter) #String = Wörter/Text
print("Alter als String:", alter_str) # Werte ausgeben

# Gleitkommazahlen zu Ganzzahlen casten
hoehe = 175.5 #Float = Kommazahlen zu Ganzenzahlen
hoehe_int = int(hoehe) # Float zu Integer

# Ergebnis ausgeben
print("Höhe als Ganzzahl:",hoehe_int)

# Listen sind eine Art Conatiner, in dem mehrere Werte gespeichert werden können.
meine_zahlen_liste = [1, 2, 3, 4, 5]
meine_buchstaben_liste = ["a", "b", "c", "d", "e"]
meine_gemischte_liste = [1, "a", 2, "b", 3, "c"]

print("Zahlenliste:", meine_zahlen_liste)
print("Buchstabenliste:", meine_buchstaben_liste)
print("Gemischte Liste:", meine_gemischte_liste)

# add new value to the list
meine_zahlen_liste. append(6)

print("Updated Zahlenliste:", meine_zahlen_liste)
print("1. Wert in der Liste meine_zahlen_liste:", meine_zahlen_liste[0]) #immer bei 0 anfangen zu zählen
print("2. Wert in der Liste meine_zahlen_liste:", meine_zahlen_liste[1])
print("3. Wert in der Liste meine_zahlen_liste:", meine_zahlen_liste[2])    

# change value
meine_zahlen_liste[0] = 0
print("Updated Zahlenliste:", meine_zahlen_liste)

# remove value
meine_zahlen_liste.remove(0)
print("Updated Zahlenliste nach dem Löschen:", meine_zahlen_liste)

#lenght of list
print("Länge der Zahlenliste:", len(meine_zahlen_liste))

mein_dictonary = {"name": "Maddy", "alter": 25}
print("Name:", mein_dictonary["name"])

# value change
mein_dictonary["name"] = "Nathalie"
print("Neuer Name:", mein_dictonary["name"])

# add new key-value
mein_dictonary["hobby"] = "schwimmen"
print("Hobby:", mein_dictonary["hobby"])

# delete key-value
print("mein_dictonary before delete:", mein_dictonary)
del mein_dictonary["hobby"]
print("mein_dictonary after delete:", mein_dictonary)
