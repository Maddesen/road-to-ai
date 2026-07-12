
## Variables store values.

name =  "Maddy" #String = Wörter/Buchstaben
print(name) # Werte ausgeben
alter = 40 #Integer = ganze Zahlen
print(alter) # Werte ausgeben
# Casting
alter_str = str(alter) #Casting = Umwandlung von einem Datentyp in einen anderen

# Gleitkommazahlen zu Ganzzahlen casten
hoehe = 175.5 #Float = Kommazahlen
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
