import sqlite3
from datetime import date
from card import Card

class CardRepository:
    def __init__(self, db_path: str): 
        self.db_path = db_path
        self._create_table()

    def _create_table(self) -> None: 
        conn=sqlite3.connect(self.db_path)
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cards (
            id INTEGER PRIMARY KEY,
            recto TEXT NOT NULL,
            verso TEXT NOT NULL,
            box INTEGER NOT NULL,
            next_review TEXT NOT NULL 
            )
        """)
        conn.commit()
        conn.close()
   
    def add(self, card: Card) -> None: 
        conn=sqlite3.connect(self.db_path)
        cursor =conn.execute("""
            INSERT INTO cards (recto, verso, box, next_review)
            VALUES (?, ?, ?, ?)
        """, (card.recto, card.verso, card.box, card.next_review.isoformat()))
        card.id = cursor.lastrowid
        conn.commit()
        conn.close()

    def add_many(self, cards: list[Card]) -> None:
        conn=sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        for card in cards:
            cursor.execute("""
                INSERT INTO cards (recto, verso, box, next_review)
                VALUES (?, ?, ?, ?)
            """, (card.recto, card.verso, card.box, card.next_review.isoformat()))
        conn.commit()
        conn.close()

    def update(self, card: Card) -> None: 
        conn=sqlite3.connect(self.db_path)
        conn.execute("""
            UPDATE cards
            SET recto = ?, verso = ?, box = ?, next_review = ?
            WHERE id = ?
        """, (card.recto, card.verso, card.box, card.next_review.isoformat(), card.id))
        conn.commit()
        conn.close()

    
    def get_due(self, today: date) -> list[Card]:
        conn=sqlite3.connect(self.db_path)
        cursor = conn.execute("""
            SELECT id, recto, verso, box, next_review
            FROM cards
            WHERE next_review <= ?
        """, (today.isoformat(),))
    
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_card(row) for row in rows]
           
        
    def get_all(self) -> list[Card]:
        conn=sqlite3.connect(self.db_path)
        cursor = conn.execute("""
            SELECT id, recto, verso, box, next_review
            FROM cards
        """)
        
        rows = cursor.fetchall()
        conn.close()
        return [self._row_to_card(row) for row in rows]


    def get_by_id(self, card_id: int) -> Card | None:
        conn=sqlite3.connect(self.db_path)
        cursor = conn.execute("""
            SELECT id, recto, verso, box, next_review
            FROM cards
            WHERE id = ?
        """, (card_id,))
        row = cursor.fetchone()
        conn.close()
        return self._row_to_card(row) if row else None

    def _row_to_card(self, row: tuple) -> Card:
        return Card(
            id=row[0],
            recto=row[1],
            verso=row[2],
            box=row[3],
            next_review=date.fromisoformat(row[4])
        )