from datetime import date
from card import Card
from repository import CardRepository
from interval import LeitnerScheduler
from session import ReviewSession

repo = CardRepository("test.db")
for recto, verso in [("hola", "bonjour"), ("gracias", "merci"), ("adios", "au revoir")]:
    repo.add(Card(None, recto, verso))

session = ReviewSession(repo, LeitnerScheduler(), date.today())

while not session.is_finished():
    carte = session.random_card()
    print(carte.recto)
    reponse = input("Je savais ? (o/n) ")
    session.answer(carte.id, reponse == "o")

print("Terminé")