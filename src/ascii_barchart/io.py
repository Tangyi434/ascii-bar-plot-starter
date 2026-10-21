import csv


def load_rows(file_path: str) -> list[dict]:
    """Liest die CSV-Datei ein und wandelt 'value1' in float um."""
    rows = []
    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            cleaned_row = {
                k.strip(): v.strip() for k, v in row.items() if k is not None
            }

            if "value1" in cleaned_row:
                cleaned_row["value1"] = float(cleaned_row["value1"])

            rows.append(cleaned_row)
    return rows