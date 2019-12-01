# Empfehlung (auch zum Danebenlegen bei den Übungsaufgaben): Python Cheat Sheet
# https://www.dataquest.io/blog/python-cheat-sheet/

###=== Umgang mit Variablen allgemein ===###

# Python-Skripte werden einfach von oben nach unten ausgefuehrt, es ist keine explizite main notwendig (aber moeglich, sehen wir spaeter)
# Variablen kriegen keine Typendeklaration:
x = 5
x += 3
y = 2*x
print(y)

# Grundlegende Operatoren funktionieren wie erwartet:
# Modulo:
print(y%3)

# Ganzzahl-Division (floor):
print(y//3)

# Potenzierung:
print(y**4)

# Alle Operationen lassen sich mit Direktzuweisung kombinieren:
y %= 3
print(y)

# Vorsicht: strong typing -> Java-artige Verkettung geht nicht!
print("y="+y)

# Stattdessen muss man explizit konvertieren:
print("y="+str(y))

# Jede Variable in Python ist ein Objekt:
print(x.bit_length())

# Nützliche Funktion: dir() zeigt alle Methoden und Attribute eines Objektes an:
dir(x)
dir("   test")
print("   test".upper())
print("   test".strip())

# LÜCKENAUFGABEN zu dir()

# Methoden mit __ sind "magic"-Methoden, nicht für direkte Verwendung gedacht

# Neben den klassischen integer, float, string haben wir Listen:
x = [1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]
print(x)

# Vorsicht: Durch die dynamische Typisierung geht das x=[1,2,3] oben: x ist jetzt kein integer mehr, sondern eine Liste!
# Adressierung von Listen wie gewohnt:
print(x[0])

# Man kann mit Listen viele lustige Dinge tun, z.B.:
# slicen
print(x[2:5])
print(x[5:])
print(x[:5])

# von hinten adressieren
print(x[-3])

# Verketten, verschachteln und Datentypen darin mischen
print(x + ["a", 2, ["b", "blub"]])

# LÜCKENAUFGABE zu Listen

# Elemente entfernen
x.pop(3) # Das ist der Index
print(x)
x.remove(5) # Das ist der Wert des Elements (es wird das erste Vorkommen gelöscht)
print(x)

# Performance-Hinweis: Listen sind als voralloziierte pointer-Arrays implementiert, die bei Erreichen
# der Kapazität wachsen (-> volle Kopie).
# pop last, get sind O(1), append ist amortisiert O(1), aber pop nach Index, remove sind O(n)!

# Als abgespeckte Version existieren noch Tupel:
tup = (1, 3, 4)
print(tup)

# Viel mehr als Zugriff geht damit nicht, tuples sind immutable (erlauben
# aber Optimierungen, sollten also wenn möglich statt Listen eingesetzt werden)

# Dann gibt es noch Dictionaries (aus Java bekannt z.B. als HashMap):
mydict = {"key": "value", "a": 5, "Zeugs": "sehr sinnvoll", 7: "sieben"}
print(mydict)
print(mydict["Zeugs"])
mydict["Zeugs"] = "weniger sinnvoll"
print(mydict["Zeugs"])

# Ueberpruefung, ob ein key drin ist:
print("Zeugs" in mydict)
print("neuerkey" in mydict)
mydict["neuerkey"] = "neuerwert"
print("neuerkey" in mydict)
print(mydict["neuerkey"])

# Übrigens auch aus einem Tupel von Tupeln initialisierbar:
mydict2 = dict((("7", "sieben"), ("acht", 8)))
print(mydict2)

# LÜCKENAUFGABEN zu Dictionaries

# Ein set ist eine Menge und kann jedes Element nur ein Mal enthalten:

myset = set()
myset.add(15)
myset.add("blub")
print(myset)
myset.add(14)
myset.add(15)
print(myset)

###=== Umgang mit Strings ===###
# Python wird häufig zur Stringverarbeitung (Tabellenkonversion etc.) verwendet,
# daher ein paar mehr Details zu Strings.

# String-delimiter können ", ', oder (für multiline) """ sein:
print('Das ist z.B. nuetzlich um " nicht escapen zu muessen')

dat="""Oder um
mehrere Zeilen Text
einfach einzugeben"""
print(dat)

# Es existieren viele convenience-Funktionen für strings, z.B.:

dat2 = dat.replace("\n", " ")
print(dat2)
print(dat2.split(" "))

# (das geht alles auch mit regexp, Modul re, aber das führt zu weit)

# Strings haben eine häufig verwendete, nette Methode, um Tupel und Arrays zu verketten:

toprint = ["Das", "sind", "Woerter"]
print(" ".join(toprint))
print("--!--".join(toprint))

# LÜCKENAUFGABEN zu Strings

# Zum Formatieren von strings existiert eine Spezifikationssprache:
# {} sind placeholder für Variablen
print("Der Wert von y: {} minus den Wert von x: {} ist: {}".format(x, y, x-y))

# Mit {} können auch Positionen in der Argumentenliste angegeben werden:
print("y: {1}, x: {0}".format(x, y))

# Positionen können wiederholt werden:
print("{0}{1}{0}".format("abra", "cad"))

# Zahlenformate können definiert werden:
print("723 in binary: {0:b} and hex: {0:X}".format(723))

# Damit kann man übrigens schön die Ergebnisse binärer Operationen anschauen:
print("1: {:b}, 1<<2: {:b}, 60: {:b}, ~60: {:b} (dezimal: {}), 13: {:b}, 60&13: {:b}, 60|13: {:b} etc...".format(1, 1<<2, 60, ~60, ~60, 13, 60&13, 60|13))
# Frage: Kann jemand erklären, wieso ~60==-61

# Man kann links, rechts oder mittig alignen und sich das Fuellzeichen aussuchen:
print("y 10-stellig rechtsbündig: {0:>10}, linksbündig: {0:<10}, zentriert: {0:^10} und rechtsbündig mit 0: {0:0>10}".format(y))


###=== Kontrollstrukturen ===###

# Kontrollstrukturen verhalten sich wie gewohnt.
# Ungewohnt:
#  * Beginn eines Blocks wird mit : am Ende der Kontrollstuktur gekennzeichnet
#  * Einrückung muss stimmen (und in gesamten Code konsistent sein, mal 3 Leerzeichen und mal 4 geht nicht).
y = 12
if y > 10:
    y -= 3
elif y <= 10:
    y += 10
else:
    print("Geht nicht.")
print(y)

# Funktioniert nicht wegen fehlender Einrückung:
if y > 10:
    print("y immer noch groesser 10")
print("Das ist auch toll")

# While tut das, was while halt so tut:
y=10
while y > 5:
    print(y)
    y -= 1

# LÜCKENAUFGABEN zu while, if, else

# for ist zum iterieren da:
letters = ["a", "b", "c"]
for letter in letters:
    if letter == "a":
        print("AAAAAAAAA")
    print(letter)

# Man kann über alles iterieren, was iterable ist (auch strings sind z.B. iterable):
print(range(2,7))
for x in range(2,7):
    print(x)

for x in range(0,10,3):
    print(x)

for key in mydict:
    print(str(key) + ": " + str(mydict[key]))

for item in mydict.items():
    print(item)

# LÜCKENAUFGABEN zu for

# AUFGABEN:
# 1.1) Finden Sie 2 Methoden, um von einem String alle Zeichen
#   zeilenweise auszugeben. Z.B. word = "test", Ergebnis:
# t
# e
# s
# t
# 1.2) Geben Sie von den Buchstaben des Wortes jeden nur ein Mal aus. Z.B.
#   word = "test". Tips: Sie können eine dafür besonders geeigtene Datenstruktur verwenden, oder die .count()-Methode
#   von String. Ergebnis:
# t
# e
# s
# 1.3) Drehen Sie die Zeichen in einem String um, z.B. word = "Zeichenkette", nach
#   Ausführung ist word == "etteknehcieZ"
# 1.4*) Bauen Sie aus einem String (z.B. "test") ein Array aller Rotationen
#   dieses String (-> ["test", "estt", "stte", "estt"])
# 1.5*) Erweitern Sie 1.4 indem aus einem Array von Strings eine dictionary
#   generiert wird, die zu jedem der Strings (key) die Liste aller Rotationen
#   wie in 1.4* beschrieben ablegt (values).
# 1.6*) Erweitern Sie 1.4*, indem Sie eine um den ersten Buchstaben zentrierte
#   Ausgabe erstellen. Z.B. word = "Test", Ausgabe:
#     Test
#    tTes
#   stTe
#  estT

# Direktes Entpacken der Tupel:
for key, value in mydict.items():
    print(str(key) + ": " + str(value))

# Geht übrigens mit >2 Elementen und überall wo Tupel/Listen zurückkommen:
a, b, c = (1, 2, 5)
print("{}, {}, {}".format(a, b, c))

# Eine Python-spezifische Form von Schleifen ist die list comprehension. Sie
# definiert Operationen, die auf definierte Elemente einer iterable angewendet werden
values = range(0, 20)
even = []
for x in values:
    if x % 2 == 0:
        even += [x]
print(even)
even = [x for x in values]
even = [[y for y in range(0, x)] for x in range(0, 20)]
print(even)

stringdict = dict([(str(x), x) for x in values])
print(stringdict["12"])

# LÜCKENAUFGABEN List Comprehensions
