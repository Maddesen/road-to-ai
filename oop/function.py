# functions in python

# function for adding two numbers

def addiere(zahl1: int, zahl2: int) -> int:
    return zahl1 + zahl2

# function to greet a user
def greet(name: str) -> str:
    return f"Hallo, {name}!"

# Funktion zu Berechnung des Flächeninhaltes eines Rechteckes mit typehints
def berechne_flaeche(laenge: float, breite: float) -> float:
    """ 
    Berechnet die Fläche eines Rechteckes
    Parameter:
    Länge: die Länge des Rechteckes
    Breite: die breite eines Rechteckes
    Return:
    float: die Fläche des Rechteckes
    """
    return laenge * breite

# Aufruf der funtkion:
summe = addiere(5, 8)
print("Die Summe ist:", summe)

gruß = greet("Nathalie")
print(gruß)

flaeche = berechne_flaeche(10.5, 4.4)
print("Die Fläche des Rechteckes ist:", flaeche)

