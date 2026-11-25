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
    
    
    def add_many(self, cards: list[Card]) -> None: ...
        sqlite3.connect(self.db_path)
    def update(self, card: Card) -> None: ...
        sqlite3.connect(self.db_path)
    def get_due(self, today: date) -> list[Card]: ...
    def get_all(self) -> list[Card]: ...