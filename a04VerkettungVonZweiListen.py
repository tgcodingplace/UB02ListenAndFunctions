# Aufgabe 4: Listen und Functions
#
# Erstelle eine Function f4, die zwei Listen zusammenhängt. Die Adresse auf die
# zusammengefügte Liste wird zurückgeliefert.

# Beachte, dass der beide Parameter für eine Liste stehen

def f4(e, f):

    # l ist die Liste, die die beiden Listen e und f aufnimmt.
    l = []

    for i in e:

        l.append(i) # füge zunächst e an l an

    for i in f:

        l.append(i) # füge dann f an l an

    # ... und kopiere die Adresse von l an das Hauptprogramm zurück
    return l


########################################################################
#                                                                      #
# Hier beginnt das Hauptprogramm                                       #
#                                                                      #
########################################################################

a = [2,4,6,8,10]
b = [12,14,16,18,20]

# c übernimmt die Adresse der Liste
c = f4(a,b)

print(c)


