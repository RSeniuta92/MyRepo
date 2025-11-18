import json
from ascii_table import Table

# --- 1. Wczytaj JSON z pliku ---
with open("asciitable.json", "r") as f:
    rows = json.load(f)

# --- 2. Konwersja wierszy -> kolumny (i wszystkie wartości na stringi) ---
data = [
    {
        "Header": key,
        "Contents": [str(row[key]) for row in rows]
    }
    for key in rows[0].keys()
]

# --- 3. Generowanie tabeli ---
table = Table(data)
print(table)