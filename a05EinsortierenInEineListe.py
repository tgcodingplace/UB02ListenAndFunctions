# Aufgabe 5: Listen und Functions
#
# Erstelle eine Function f5, die eine übergebene Zahl in eine existierende Liste
# aufsteigend einsortiert. Wir beginnen mit einer Liste der Länge 0.

def f5(liste, wert):

    # Bei negativem Wert geben wir die Liste unbearbeitet
    # zurück
    if wert < 0:
        return liste

    # Wenn die Liste leer ist schreiben wir wert und geben die Liste zurück    
    if len(liste)==0:
        liste.append(wert)
        return liste

    # Bei mindestens einem Wert lohnt es sich einzusortieren
    # Wir fügen zunächst einen weiteren Platz ein
    liste.append(0)
    index = 0

    for i in range(len(liste)-1,0,-1):

        if wert < liste[i-1]:
            liste[i] = liste[i-1]
        else:
            index = i
            break

    liste[index] = wert

    return liste


########################################################################
#                                                                      #
# Hier beginnt das Hauptprogramm                                       #
#                                                                      #
########################################################################

# Eine negative Eingabe beendet das Programm

a = []

x = int(input("Gib eine positive Zahl ein: "))

while(x >= 0):

    a = f5(a,x)
    print(a)

    x = int(input("Gib eine positive Zahl ein: "))