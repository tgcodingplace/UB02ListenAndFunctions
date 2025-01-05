# Aufgabe 3: Listen und Functions
#
# Erstelle eine Function f3, die eine existierende Liste nach einem ebenfalls
# übergebenen Zahlenwert durchsucht.
# --> Zurück gegeben wird der Index.
# --> Wird der Wert nicht gefunden wird -1 zurück geliefert.

# Beachte, dass der zweite Parameter x für den Suchwert steht.

def f3(a, x):

    # Fall sich der gesuchte Wert nicht in der Liste befindet behält index
    # entsprechend der Aufgabenstellung den Wert -1
    index = -1

    for i in range(0, len(a)):

        if a[i]==x:
            
            # Sobalb wir einen Treffer haben kopieren wir den Wert von i
            # in index und setzen i auf die Länge des Arrays. mit diesem
            # Trick provozieren wir einen vorzeitigen Schleifenabbruch.
            # OK, break hätte es auch getan .....
            index = i
            i = len(a)

    return index

########################################################################
#                                                                      #
# Hier beginnt das Hauptprogramm                                       #
#                                                                      #
########################################################################

liste = [37,24,56,19,3,84,47,29]

print(f3(liste,47))
print(f3(liste,48))

