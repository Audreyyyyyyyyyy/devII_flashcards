from openpyxl import load_workbook


def importer_cartes(chemin):
    """Lit un fichier Excel et renvoie la liste des cartes valides."""
    classeur = load_workbook(chemin)
    feuille = classeur.active
    cartes = []

    for ligne in feuille.iter_rows(min_row=2, max_col=2, values_only=True):
        recto = ligne[0]
        verso = ligne[1]

        # on ignore les lignes avec une case vide
        if recto is None or verso is None:
            continue

        carte = {
            "recto": str(recto).strip(),
            "verso": str(verso).strip(),
        }
        cartes.append(carte)

    return cartes


if __name__ == "__main__":
    cartes = importer_cartes("mots.xlsx")
    for carte in cartes:
        print(carte["recto"], "->", carte["verso"])
    print(len(cartes), "cartes importées")

