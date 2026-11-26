from datetime import date, timedelta
from card import Card

class LeitnerScheduler:
    INTERVALS = {1: 1, 2: 2, 3: 4, 4: 8, 5: 16}   # jours

    def apply_answer(self, card: Card, correct: bool, today: date) -> None: 
        if correct:
            card.promote()
        else:
            card.demote()
        card.next_review = self.next_review_date(card.box, today)

    def next_review_date(self, box: int, today: date) -> date: 
        return today + timedelta(days= self.INTERVALS[box])
