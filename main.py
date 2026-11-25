from dataclasses import dataclass
from datetime import date
import datetime

@dataclass
class Card:
    id: int | None
    recto: str
    verso: str
    box: int = 1
    next_review: date = datetime.datetime.now()   # date du jour par défaut

    def is_due(self, today: date) -> bool: 
        if self.next_review 
    def promote(self) -> None:
        if box <5
            box +=1
        else box ===5     # box + 1 (max 5)
    def demote(self) -> None: 
        box ===1      # retour à 1