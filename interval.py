from datetime import date, timedelta
from card import Card

class LeitnerScheduler:
    INTERVALS = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16}   # jours

    def apply_answer(self, card: Card, correct: bool, today: date) -> None: ...
    def next_review_date(self, box: int, today: date) -> date: 
        INTERVALS[box]
        "il faut rajouter interval a la date de ajd pour la prochaine revision"