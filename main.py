from dataclasses import dataclass
from datetime import date 
import datetime

@dataclass
class Card:
    id: int | None
    recto: str
    verso: str
    box: int = 1
    next_review: date = datetime.today()   # date du jour par défaut

    def is_due(self, today: date) -> bool: 
        return today <= date
    def promote(self) -> None:
        if box <5
            box +=1
             # box + 1 (max 5)
    def demote(self) -> None: 
        box =1      # retour à 1