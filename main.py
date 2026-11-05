# main.py
# F-07 : réviser les cartes du jour
from donnees import cartes
import random

MAX_NOUVELLES = 20


def choisir_cartes():
    a_revoir = []
    nouvelles = []

    for carte in cartes:
        if carte["boite"] == 0:
            nouvelles.append(carte)
        elif carte["maitrisee"] == False:
            a_revoir.append(carte)

    # on mélange pour que l ordre change
    random.shuffle(a_revoir)
    random.shuffle(nouvelles)

    # d abord les cartes à revoir ensuite les nouvelles (20 max)
    liste = a_revoir
    compteur = 0
    for carte in nouvelles:
        if compteur < MAX_NOUVELLES:
            liste.append(carte)
            compteur = compteur + 1

    return liste


def reviser():
    liste = choisir_cartes()
    print("Il y a", len(liste), "cartes à réviser")

    numero = 1
    for carte in liste:
        print()
        print("Carte", numero, "sur", len(liste), ":", carte["recto"])
        input("Appuie sur Entrée pour retourner la carte")
        print("Réponse :", carte["verso"])

        reponse = input("1 = je savais, 2 = j'ai hésité, 3 = je ne savais pas : ")
        while reponse != "1" and reponse != "2" and reponse != "3":
            reponse = input("Choisis 1, 2 ou 3 : ")

        # une nouvelle carte arrive en boite 1
        if carte["boite"] == 0:
            carte["boite"] = 1

        if reponse == "1":
            if carte["boite"] == 5:
                carte["maitrisee"] = True
            else:
                carte["boite"] = carte["boite"] + 1
        elif reponse == "3":
            carte["boite"] = 1
            carte["maitrisee"] = False
        # si reponse == "2" on ne change rien

        numero = numero + 1

    print()
    print("Fin de la session")
    for carte in cartes:
        print(carte["recto"], "-> boite", carte["boite"], "maitrisee :", carte["maitrisee"])


# programme principal
while True:
    reviser()

