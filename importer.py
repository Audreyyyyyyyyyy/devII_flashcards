from openpyxl import load_workbook
from card import Card

class ExcelImporter:
    def load(self, file_path: str) -> tuple[list[Card], list[str]]: ...   # cartes valides, erreurs
    def _validate_row(self, row: tuple, line_number: int) -> str | None: ...