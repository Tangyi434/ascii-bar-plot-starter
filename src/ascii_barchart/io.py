import csv


def load_rows(path):
    rows = []
    with open(path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)
        next(reader, None)  # Header überspringen

        for row in reader:
            if not row:
                continue
            point_type = row[0].strip()
            value1 = float(row[1])
            value2 = float(row[2])
            rows.append((point_type, value1, value2))

    return rows