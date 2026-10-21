from collections import defaultdict


def average_value1_by_type(rows: list[dict]) -> dict:
    """Berechnet für jeden 'type' das arithmetische Mittel von 'value1'."""
    type_sums = defaultdict(float)
    type_counts = defaultdict(int)

    for row in rows:
        t = row["type"]
        val = row["value1"]
        type_sums[t] += val
        type_counts[t] += 1

    averages = {}
    for t in type_sums:
        averages[t] = type_sums[t] / type_counts[t]

    return averages