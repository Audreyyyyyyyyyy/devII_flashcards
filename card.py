from dataclasses import dataclass, field
from datetime import date


@dataclass
class Card:
    id: int | None
    recto: str
    verso: str
    box: int = 1
    next_review: date = field(default_factory=date.today)   # date du jour par défaut

    def is_due(self, today: date) -> bool: 
        return self.next_review <= today 
        "fait par Brian : jsp comment faire il faut faire en sorte que si next_review c'est ajd on la fait pop"
    def promote(self) -> None:
        if self.box <5:
            self.box +=1    # box + 1 (max 5)
    def demote(self) -> None: 
        self.box =1      # retour à 1