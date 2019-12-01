# LÜCKENAUFGABEN zu dir():
# Finden Sie eine String-Methode, die den ersten Buchstaben groß macht (z.B. "wort"->"Wort"), und eine, die
# die Groß- und Kleinschreibung vertauscht ("TestText"->"tESTtEXT"). Hinweise: "Großbuchstabe" heißt auf
# Englisch "capital letter" und die Bezeichnung dafür, ob ein Buchstabe groß oder klein geschrieben ist, heißt
# auf Englisch "case" ("upper case" = "groß geschrieben", "lower case" = "klein geschrieben")

text1 = "wort"
print(text1.%1%()) # Soll "Wort" ausgeben

text2 = "TestText"
print(text2.%2%()) # Soll tESTtEXT ausgeben

# LÜCKENAUFGABEN zu Listen:
# Erstellen Sie eine 3x3-Liste
myarray=[[%1%,%2%,%3%],[%4%],%5%]
print(myarray) # Soll ausgeben: [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Erstellen Sie eine 3x3-Liste, in der jede Zahl anders ist, geben Sie sie aus, und entfernen Sie
# das mittlere Element
myarray2=%6%
print(myarray2)
myarray2.%7%(%8%) # Whiteboard
print(myarray2)

# LÜCKENAUFGABEN zu Dictionaries:
# Erstellen Sie aus den Elementen von myarray2 eine Dictionary, in der die einzelnen Elemente Schlüsseln
# zugewiesen sind,
# die jeweils einzelne Buchstaben sind
mydict1 = dict()
mydict1[%1%] = %2%
%3%
print(mydict1.keys()) # Soll dict_keys(("a", "b")) ausgeben
print(mydict1["a"]) # Soll das Gleiche ausgeben, wie print(myarray2[0])


# LÜCKENAUFGABEN zu Sets:
# Erstellen Sie ein Array mit 4 Elementen, von denen 2 gleich sind. Erstellen Sie daraus ein neues Array,
# das jedes dieser Elemente nur ein Mal enthält.
myarray3 = [%1%, %2%, %3%, %4%]
unique = %5%() # unique als richtigen Datentyp initialisieren
unique.%6%(%7%) # Element hinzufügen
unique.%8% # ditto
unique.%9% # ditto
unique.%10% # ditto
myuniquearray = []
myuniquearray += [%11%.%12%()] # myuniquearray befüllen
myuniquearray += [%13%] # ditto
myuniquearray += [%14%] # ditto
print(myuniquearray) # Soll jedes Element aus myarray nur 1x ausgeben

# LÜCKENAUFGABEN zu Strings:

text = "Das hier ist ein Satz mit vielen Wörtern."

# Den 5ten Buchstaben aus dem Text ausgeben:
print(text[%1%])
print(text[4])

# Das dritte Wort aus dem Satz ausgeben:
words = text.split(" ")
print(words[2])
words = %1%.split(%2%)
print(%3%)

# Alle Wörter aus dem Satz mit "--" getrennt anstatt mit " " getrennt ausgeben:
# Variante 1:
print("--".join(words))
words = %1%
print("%2%".join(%3%))

# Variante 2:
print(text.replace(" ", "--"))
print(text.replace(%4%, %5%))


# LÜCKENAUFGABEN zu while, if, else
# Alle ungeraden Zahlen bis 10 ausgeben:
maxvalue = %1%
currentvalue = 0
while %2% <= %3%:
    if %4%: # Welche mathematische Operation kann genutzt werden, um die Teilbarkeit einer Zahl durch eine andere zu testen?
        print(%5%)
    %6% # Was muss man tun, damit die Schleife nicht unendlich weiterläuft?

# Die folgende Zahlenreihe ausgeben: 0, 1, 2, 3, 5, 7, 9, 12, 15, 18 (steigende Abstände):
currentvalue = %1%
cutoff1 = %2%
cutoff2 = %3%
%4%:
    print(%5%)
    if %6%:
        currentvalue += 3
    %7%:
        currentvalue %8%
    %9%:
        %10%

# Die folgende Zahlenreihe ausgeben: 0, 1, 2, 3, 5, 7, 9, 12, 15, 18 (steigende Abstände):
currentvalue = 0
cutoff1 = 3
cutoff2 = 9
while currentvalue <= 18:
    print(currentvalue)
    if currentvalue < cutoff1:
        currentvalue += 1
    elif currentvalue >= cutoff1:
        currentvalue += 2
    else:
        currentvalue += 3

# LÜCKENAUFGABEN zu for

# Jeden zweiten Buchstaben aus dem Satz ausgeben:
# 2: a
# 4:
# 6: i
# ...
text = "Das hier ist ein Satz mit vielen Wörtern."
for index in range(%%, len(%%)):
    if %1%:
        print(%2%(index) + ": " + %3%)

# Einen Punkt ausgeben für jedes "i" im Text:
text = "Das hier ist ein Satz mit vielen Wörtern."
for letter in %1%:
    if %2%:
        print(".")

# Ein Array aufbauen mit allen Wörtern, die ein "i" enthalten:
text = "Das hier ist ein Satz mit vielen Wörtern."
wordswithi = []
allwords = text.split(" ")
for word in allwords:
    if "i" in word: # Der operator "in" funktioniert auch bei Strings!
        wordwithi += [word]
    print(wordswithi)

# EGI
# LÜCKENAUFGABEN zu List Comprehensions

# Erstellen Sie aus dem Array singulars ein Array multiples, in dem durch Anhängen von
# "s" die Mehrzahl jedes Wortes in
# singulars erstellt wird.
singular = ["house", "flower", "cat", "dog", "mountain"]
multiples = [%1% + %2% for word in %3%]

# Erstellen Sie aus dem Array stems ein 2-dimensionales Array singular_conjugations mit
# den Konjugationen für ich, du, er
# (z.B. "kauf" (Wortstamm von kaufen) -> ["kaufe", "kaufst", "kauft"])
stems = ["kauf", "lern", "mach", "sitz", "denk"]
singular_conjugations = [[%1%, %2%, %3%] for %4% in %5%]

# Bei Wortsämmen, die mit t enden muss bei der 2. und 3. Person noch ein "e" dazwischen.
# Bauen Sie aus t_stems
# ein Arrray singular_conjugations auf:
t_stems = ["arbeit", "antwort", "beobacht", "bitt", "heirat"]
singular_conjugations = [[%1%] for %2]

# In mixed_stems sind die beiden Wortstammtypen oben gemischt. Bauen Sie singular_conjugations nur aus den
# nicht mit "t" endenden Wortstämmen auf:
mixed_stems = ["kauf", "lern", "arbeit", "antwort", "mach", "beobacht", "sitz", "denk", "bitt", "heirat"]
singular_conjugations = [%1% for %2% if %3%]

## --- HOCHLADEN -- ## - AKGI

# Bauen Sie nun aus mixed_stems singular_conjugations so auf, dass die Konjugationen für alle Wörter korrekt
# erstellt werden
mixed_stems = ["kauf", "lern", "arbeit", "antwort", "mach", "beobacht", "sitz", "denk", "bitt", "heirat"]
singular_conjugations = [%1% if %2%]
singular_conjugations %3% [%4%]

# Kleine Wiederholung:

# Nur die Wörter, die i enthalten, aus dem Satz ausgeben:
text = "Das hier ist ein Satz mit vielen Wörtern."
only_i = [%1% in text.%2%(%3%) if %4%]

# Die Wörter mit i zählen
text = "Das hier ist ein Satz mit viiiielen Wörtern."
only_i = %1%
num_words = %2%(only_i)


# LÜCKENAUFGABEN zu Generator-Funktionen
# Schreiben Sie einen Generator, der ungerade Zahlen zurückgibt und geben Sie die ersten 2 aus:
def oddnumbers():
    number = 1
    %1%: # Wie lange wollen wir weitermachen?
        if %2%: # Wie prüft man, ob eine Zahl gerade ist?
            yield %3%
        number += 1

odd = %4%
print(%5%(odd))
print(%6%)

# Kann man das oben besser lösen? Braucht man die Schleife überhaupt?
# Modifizieren Sie die obige Aufgabe so, dass sie kein if benötigt
# (Hinweis: Nur eine Zeile ohne %% muss geändert werden)

