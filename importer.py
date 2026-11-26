from openpyxl import load_workbook

from card import Card
from repository import CardRepository


def lire_excel(chemin: str) -> tuple[list[Card], list[str]]:
    """Lit un fichier Excel (colonne A = recto, colonne B = verso, ligne 1 = en-têtes).

    Renvoie (cartes valides, messages d'erreur). N'écrit rien en base.
    """
    classeur = load_workbook(chemin, data_only=True)
    feuille = classeur.active
    cartes: list[Card] = []
    erreurs: list[str] = []

    for numero, ligne in enumerate(feuille.iter_rows(min_row=2, max_col=2, values_only=True), start=2):
        recto = "" if ligne[0] is None else str(ligne[0]).strip()
        verso = "" if ligne[1] is None else str(ligne[1]).strip()

        if not recto and not verso:
            continue  # ligne complètement vide : on l'ignore sans erreur
        if not recto or not verso:
            erreurs.append(f"Ligne {numero} : recto ou verso vide")
            continue

        cartes.append(Card(None, recto, verso))

    classeur.close()
    return cartes, erreurs


def importer_dans_repo(chemin: str, repo: CardRepository) -> dict:
    """Lit l'Excel puis ajoute à la base les cartes qui n'y sont pas déjà."""
    cartes, erreurs = lire_excel(chemin)

    # (recto, verso) déjà connus : évite de doubler les cartes si on réimporte le même fichier
    deja_la = {(c.recto.lower(), c.verso.lower()) for c in repo.get_all()}
    nouvelles: list[Card] = []
    doublons = 0

    for carte in cartes:
        cle = (carte.recto.lower(), carte.verso.lower())
        if cle in deja_la:
            doublons += 1
        else:
            nouvelles.append(carte)
            deja_la.add(cle)

    repo.add_many(nouvelles)
    return {"ajoutees": len(nouvelles), "doublons": doublons, "erreurs": erreurs}


if __name__ == "__main__":
    import sys

    chemin = sys.argv[1] if len(sys.argv) > 1 else "mots.xlsx"
    resultat = importer_dans_repo(chemin, CardRepository("test.db"))

    print(resultat["ajoutees"], "carte(s) ajoutée(s)")
    print(resultat["doublons"], "doublon(s) ignoré(s)")
    for erreur in resultat["erreurs"]:
        print("Erreur :", erreur)
