from ascii_barchart.analysis import average_value1_by_type
from ascii_barchart.io import load_rows
from ascii_barchart.plotting import print_bar_chart


def main():
    rows = load_rows("data/points.csv")
    averages = average_value1_by_type(rows)
    print_bar_chart(averages)


if __name__ == "__main__":
    main()