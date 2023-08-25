from constants import FREQUENCY_RANGES


def frequency_ranges():
    # Sort the dictionary based on lower bounds of frequency ranges
    sorted_ranges = dict(
        sorted(FREQUENCY_RANGES.items(), key=lambda item: item[1]))

    for name, (low, high) in sorted_ranges.items():
        print(f"{name}: {low} Hz - {high} Hz")
