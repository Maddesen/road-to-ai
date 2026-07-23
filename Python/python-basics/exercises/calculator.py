# Aufgabe: Programmieren Sie einen einfachen Taschenrechner

# Ihr Taschenrechner soll folgnede Fu ktionen unterstützen:
# - Addition (+)
# - Subtraktion (-)
# - Multiplikation (*)
# - Division (/)

# Der Benutzer soll aufgefordert werden, zwei Zahlen einzugeben.
# Anschließend sollte der Benutzer die gewünschte Operation wählen können.

# Beispielablauf:
# 1. Benutzer gibt Zahlen ein
# 2. Bentuzer wählt Operation (+, -, *, /).
# Das Programm führt die Berechnung durch und gibt das Ergebnis aus

zahl1 = float(input("Bitte geben Sie die erste Zahl an:"))
zahl2 = float(input("Bitte geben Sie die zweite Zahl an:"))
oper = input("Bitte geben sie an, wie die Zahlen verrechnet werden sollen (+, -, *, /, **, %):")
if oper == "+":
    print("Ergebnis:", (zahl1 + zahl2)) # für jetzt ok. Später: if-elif eine eigene Variable erstellen lassen
elif oper == "-":                       # und diese Variable am Ende ausgeben (oder mit ihr zB weiter rechnen)
    print("Ergebnis:", (zahl1 - zahl2))
elif oper == "*":
    print("Ergebnis:", (zahl1 * zahl2))
elif oper == "/":
    print("Ergebnis:", (zahl1 / zahl2)) 
elif oper == "**":
    print("Ergebnis:", (zahl1 ** zahl2))
elif oper == "%":
    print("Ergebnis:", (zahl1 % zahl2))
