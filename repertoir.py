import sqlite3
from datetime import date
from card import Card

class CardRepository:
    def __init__(self, db_path: str): ...
        self.db_path = db_path
        self._create_table()

    def _create_table(self) -> None: ...
        sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY,
            recto TEXT NOT NULL,
            verso TEXT NOT NULL,
            box INTEGER NOTNULL,
            next_review TEXT NOT NULL 
            )
        """)
        conn.commit()
   
    def add(self, card: Card) -> None: ...
        sqlite3.connect(self.db_path)
        cursor =conn.execute("""
            INSERT INTO cards (recto, verso, box, next_review)
            VALUES ("""+card.recto+","+card.verso+","+card.box+","+card.next_review.isoformat()+")
        )
        id = cursor.lastrowid
        card.id = id
        conn.commit()
    
    def add_many(self, cards: list[Card]) -> None: ...
        sqlite3.connect(self.db_path)

    
    def update(self, card: Card) -> None: ...
        sqlite3.connect(self.db_path)

    
    def get_due(self, today: date) -> list[Card]:
        sqlite3.connect(self.db_path)
        conn.execute("""
            SELECT id, recto, verso, box, next_review
            FROM cards
            WHERE next_review <= ?
        """, (today.isoformat(),))
        
        
    def get_all(self) -> list[Card]: ...