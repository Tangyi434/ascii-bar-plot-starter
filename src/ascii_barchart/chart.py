from rich import print

def scale_bar(value, maximum, width=40):
    if maximum <= 0:
        return 0
    return round(value / maximum * width)

def render_bar_chart(values, width=40):
    maximum = max(val for _, val in values)
    
    for label, value in values:
        bar = "█" * scale_bar(value, maximum, width)
        print(f"[bold]{label}[/bold]: [green]{bar}[/green] ({value})")