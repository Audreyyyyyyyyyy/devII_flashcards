from datetime import date
from card import Card
from scheduler import LeitnerScheduler
from repository import CardRepository

class ReviewSession:
    def __init__(self, repo: CardRepository, scheduler: LeitnerScheduler, today: date): ...
    def current_card(self) -> Card | None: ...
    def answer(self, correct: bool) -> None: ...   # scheduler + repo.update + carte suivante
    def is_finished(self) -> bool: ...