from rich.console import Console
from rich.text import Text

console = Console()

def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)

STYLES = {
    "A": "bold cyan",
    "B": "bold magenta",
    "C": "bold green",
    "D": "bold yellow",
}

def render_bar_chart(values, width=40):
    if not values:
        return

    # Falls ein Dictionary übergeben wird, in Key-Value-Paare umwandeln[cite: 1, 2]
    if isinstance(values, dict):
        values = values.items()

    maximum = max(val for _, val in values)

    for label, value in values:
        bar_len = scale_bar(value, maximum, width)
        style = STYLES.get(label, "bold white")

        line = Text(f"{label} | ")
        line.append("█" * bar_len, style=style)
        line.append(f" {value}")
        
        console.print(line)