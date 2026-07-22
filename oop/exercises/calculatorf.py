# Taschenrechner mit funktionen  und kommentaren

# funtionen 


def Abfrage1():
    """
    wiederholte abfrage der Zahl
    bis eine gültige eingabe kommt
    """
    while True:
        try:
            zahl1 = float(input("Bitte die Zahl an erste Position eineben:"))
            break
        except:
            print("Bitte geben sie ein gültige Zahl ein")
    
    return zahl1
      



def Abfrage2():
    while True:
        try:
            zahl2 = float(input("Bitte die Zahl an zweiter Position eineben:"))
            break
        except:
            print("Bitte geben sie ein gültige Zahl ein")
    
    return zahl2
      


zahl1 = Abfrage1()   # funtkion wird gestartet und die zahl gespeichert
zahl2 = Abfrage2()

oper = input("Wie soll gerechnet werden? Bitte geben sie + - * oder / ein:") # oper muss weiter definiert werden um eine funktion zu starten


def adition(zahl1: float, zahl2: float) -> float:
    """
    adiitions funtkion
    """
    return zahl1 + zahl2


def subtr(zahl1:float, zahl2: float) ->float:
    """
    subtraktions funktion
    """
    return zahl1 - zahl2


def multip(zahl1:float, zahl2:float) ->float:
    """
    multiplikations funktion
    """
    return zahl1 * zahl2

def divi(zahl1:float, zahl2:float) ->float:
    """
    divisions funktion
    """
    return zahl1 / zahl2
# Summe darf hier nicht als variable gespeichert werden
# da sie sonst städnig überschrieben und damit nicht korrekt weiter genutzt wird

if oper == "+":
    summe = adition(zahl1, zahl2)
    print("Ergebnis:", summe)
elif oper == "-":
    summe = subtr(zahl1, zahl2)
    print("Ergebnis:", summe)
elif oper == "*":
    summe = multip(zahl1, zahl2)
    print("Ergebnis ist:", summe)
elif oper == "/" and zahl2 == 0:
    print("Der eingegebene Opertor ist ungültig")
elif oper == "/":
    summe = divi(zahl1, zahl2)
    print("Ergebnis ist:", summe)


# es braucht kein else