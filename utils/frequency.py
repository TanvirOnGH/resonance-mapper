from constants import FREQUENCY_RANGES


def frequency_ranges():
    """
    Print and display predefined frequency ranges.

    This function retrieves and sorts the predefined frequency ranges from the
    'FREQUENCY_RANGES' dictionary and prints them to the console.

    Example:
        # Import necessary constants
        from constants import FREQUENCY_RANGES

        # Call the function to display frequency ranges
        frequency_ranges()
    """
    # Sort the dictionary based on lower bounds of frequency ranges
    sorted_ranges = dict(
        sorted(FREQUENCY_RANGES.items(), key=lambda item: item[1]))

    for name, (low, high) in sorted_ranges.items():
        print(f"{name}: {low} Hz - {high} Hz")
