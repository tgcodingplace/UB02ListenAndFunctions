# Aufgabe 1: Listen und Functions
#
# Erstelle eine Function summe, die 
# --> die Adresse einer gegebenen Liste als Referenz übernimmt,
# --> die Summe über alle Elemente berechnet und
# --> diese Summe an den Aufrufer zurück liefert.

# Die Function summe nimmt als Parameter die Adresse der im Hauptprogramm
# angelegte Liste entgegen. Über die Information, die in a abgelegt ist
# kann man auf die Speicheradresse der Liste zugreifen.
# Daher nennt man den Bezeichner einer Liste Referenz oder Adresse.
# Du kannst es Dir so vorstellen: In a steckt der Anfang der Liste.

def summe(a):

    # in der lokalen Variable summe addieren wie alle Werte auf.
    summe = 0

    # Durchlaufe die Liste - Starte bei Index Null und erhöhe i solange
    # i kleiner als die Länge der Liste ist.
    # Remember: Höchster Index ist hier 7, Länder dier Liste ist 8
    # passt!
    for i in range(0, len(a)):

        summe += a[i]

    # kopiere den Inhalt von summe zurück an den Aufrufer.
    return summe

########################################################################
#                                                                      #
# Hier beginnt das Hauptprogramm                                       #
#                                                                      #
########################################################################

liste = [37,24,56,19,3,84,47,29]

print(summe(liste))