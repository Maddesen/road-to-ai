# Eingabe über die Kommandozeile

# Einlesen eines Strings
name = input("Please enter your name:")
print("Hallo, " + name + "!")


# Einlesen eines Integers und Umwandlung
alter = input("Bitte geben Sie ihr alter ein: ")
alter= int(alter)
print("Sie sind", alter, "Jahre alt.")
print("Sie sind " + str(alter) + " Jahre alt.")

# Berechnung mit der Eingabe
jahre_bis_30 = 30 - alter
if jahre_bis_30 > 0:
    print("In " + str(jahre_bis_30) + " Jahren werden Sie 30.")
else:
    print("Sie sind bereits 30 Jahre alt oder älter.")

