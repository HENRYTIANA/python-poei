import random

a = 200
b = 5
print(a + b)

# ceci est un commentaire sur une ligne

age = "je suis vieux"
print(age)

# permet d'afficher  de quel type est la variable (text, nombre)
text = "je suis du texte"
print(type(text))

nombre = 42
print(type(nombre))

# pour concatener

print(text * 3)

text = text + "en plus"

print(text)

# les positions des lettres dans un mot

text = "Hello world"
print(text[1])
print(text[0:5])
print("bonjour je m'apelle %s" % ("henry"))

# pour préciser que les élements entre les anti slash est du texte
text = "je suis du \"1233\""
print(text)

# une liste

maListe = []
print(type(maListe))
maListe = [1, 2, 3]
print(maListe)

# manipulation des listes
maListe = []
maListe.append(125)
print(maListe)
maListe.append("salut")
print(maListe)

# modifier le contenu d'une liste
maListe = ["pomme", "peche", "poire"]
print(maListe[1])
print(maListe[2])
maListe[1] = "nectarine"
print(maListe)

# suppression d'un élément
del maListe[1]
print(maListe)
maListe.remove("pomme")
print(maListe)

maListe = ["1er", "deuxieme", "troisieme"]
# Compter le nombre d’occurences d’une valeur
print(maListe.count("1er"))
# Trouver l’index d’une valeur
print(maListe.index("1er"))

maListe = ["1er", "deuxieme", "troisieme"]
print(maListe[-1])  # Cherche la dernière occurrence
print(maListe[-2:])  # Affiche les 2 dernières occurrences
print(maListe[:])  # Affiche toutes les occurrences
maListe[:] = []  # Vide la liste
print(maListe)

# les boucles
maListe = ["1er", "deuxieme", "troisieme"]
for item in maListe:
    print(item)

for item in enumerate(maListe):  # Avec l’index
    print(item)

# manipuler des listes
maListe = ["1er", "deuxieme", "troisieme"]
secondeList = maListe
maListe[0] = "toto"
print(secondeList)

maListe = ["1er", "deuxieme", "troisieme"]
print("1er" in maListe)
print("toto" in maListe)

maListe = list(range(15))
print(maListe)
liste = list(range(10))
liste.extend(maListe)
print(liste)

# les tuples
# monTuple = ()
# print(type(monTuple))
# monTuple = ("toto",)
# print(type(monTuple))
# monTuple[0] = "error"

# les dico
monDico = {}
monDico["name"] = "Mehdi"
monDico["height"] = "1m90"
print(monDico)

print(monDico.get("name"))
print("name" in monDico)
del monDico["name"]
for val in monDico.values():  # Affiche les valeurs
    print(val)

for key in monDico.keys():  # Affiche les index
    print(key)

a = "salut"
c = 5


def test():
    b = "test"
    print(c)


test()
print(a)
print(b)


def test():
    return "salut"


a = test()
print(a)


# valeur = input("Enter your value:")
# print(valeur)


def uneListe():
    list = [4, 8, 415, 1, 25, 75, 6]
    last = True
    limit = len(list)
    while last:
        for i in range(0, limit - 1):
            last = False
            if (list[i] > list[i + 1]):
                list[i + 1], list[i] = list[i], list[i + 1]
                last = True
        limit = limit - 1
    print(list)
