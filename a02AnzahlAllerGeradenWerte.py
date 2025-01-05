# Aufgabe 2: Listen und Functions
#
# Erstelle eine Function, die die Anzahl aller geraden Zahlenwerte in der Liste
# zurückliefert.

# Die Function f2 nimmt als Parameter die Adresse der im Hauptprogramm
# angelegte Liste entgegen. Über die Information, die in a abgelegt ist
# kann man auf die Speicheradresse der Liste zugreifen.
# Daher nennt man den Bezeichner einer Liste Referenz oder Adresse.
# Du kannst es Dir so vorstellen: In a steckt der Anfang der Liste.

def f2(a):

    # in der lokalen Variable anzahl zählen wir alle geraden Zahlenwerte.
    anzahl = 0

    # Durchlaufe die Liste - Starte bei Index Null und erhöhe i solange
    # i kleiner als die Länge der Liste ist.
    # Remember: Höchster Index ist hier 7, Länder dier Liste ist 8
    # passt!
    for i in range(0, len(a)):

        # Sollte der Wert in der Liste am Index i bei einer ganzzahligen
        # Division durch 2 keinen Divisionsrest besitzen (remember modulo)
        # handelt es sich um eine gerade Zahl und anzahl wird um 1 erhöht
        if a[i]%2==0:
            
            anzahl = anzahl + 1

    # kopiere den Inhalt von anzahl zurück an den Aufrufer.
    return anzahl


########################################################################
#                                                                      #
# Hier beginnt das Hauptprogramm                                       #
#                                                                      #
########################################################################

liste = [37,24,56,19,3,84,47,29]

print(f2(liste))






