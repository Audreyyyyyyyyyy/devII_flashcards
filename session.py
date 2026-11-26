from datetime import date
from card import Card
from interval import LeitnerScheduler
from repository import CardRepository

class ReviewSession:
    def __init__(self, repo: CardRepository, scheduler: LeitnerScheduler, today: date):
        self.repo = repo
        self.scheduler = scheduler
        self.today = today

    def current_card(self) -> Card | None:
        due_cards = self.repo.get_due(self.today)
        if due_cards == []:
            return None
        else:
            return due_cards[0]


    def answer(self, correct: bool) -> None:
        card=self.current_card()
        if card is not None:
            self.scheduler.apply_answer(card, correct, self.today)
            self.repo.update(card)
    
    def is_finished(self) -> bool:
        if self.current_card() is None:
            return True
        else:
            return False


