# Aufgabe: 
# Schreiben Sie eine funktion die die Differenz zweier Zahlen errechnet und ausgibt
# verwenden sie typehints um sicherzustellen, dass beide argumente und die rückgabe int sind
# Was passiert wenn sie float zahlen eingeben?
# rufen sie die funktion auf und geben sie das ergebnis aus

def quotient(zahl1: int, zahl2: int) -> int:
    return zahl1 / zahl2

result = quotient (4, 2)
print("the result is:", result)

result2 = quotient (2.5, 1)
print("the result is:", result2)
