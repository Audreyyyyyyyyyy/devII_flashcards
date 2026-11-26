import random
from datetime import date
from card import Card
from interval import LeitnerScheduler
from repository import CardRepository


class ReviewSession:
    def __init__(self, repo: CardRepository, scheduler: LeitnerScheduler, today: date):
        self.repo = repo
        self.scheduler = scheduler
        self.today = today

    def random_card(self) -> Card | None:
        """Tire au hasard une carte parmi celles à réviser aujourd'hui."""
        due_cards = self.repo.get_due(self.today)
        if not due_cards:
            return None
        return random.choice(due_cards)

    def get_card(self, card_id: int) -> Card | None:
        """Renvoie la carte demandée si elle existe et si elle est à réviser aujourd'hui."""
        card = self.repo.get_by_id(card_id)
        if card is None or not card.is_due(self.today):
            return None
        return card

    def answer(self, card_id: int, correct: bool) -> None:
        card = self.get_card(card_id)
        if card is not None:
            self.scheduler.apply_answer(card, correct, self.today)
            self.repo.update(card)

    def is_finished(self) -> bool:
        return not self.repo.get_due(self.today)


class PracticeSession:
    """Entraînement libre : parcourt toutes les cartes dans un ordre aléatoire, sans modifier les boîtes."""

    def __init__(self, repo: CardRepository, seed: int):
        self.cards = sorted(repo.get_all(), key=lambda c: c.id)
        # même graine = même ordre : l'ordre reste stable d'une page à l'autre
        random.Random(seed).shuffle(self.cards)

    def total(self) -> int:
        return len(self.cards)

    def card_at(self, index: int) -> Card | None:
        if 0 <= index < len(self.cards):
            return self.cards[index]
        return None
