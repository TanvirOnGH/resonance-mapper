from sys import argv
from audio_processor import process_audio
from utils.frequency import frequency_ranges


def main():
    """
    Main entry point of the audio classification program.

    This function serves as the main entry point for the program. It checks
    command-line arguments and either displays frequency ranges or processes
    audio data and prints the detected sound classes.

    Example:
        # Run the program to process audio data
        python main.py

        # Display frequency ranges
        python main.py --frequency-range
    """
    if len(argv) > 1 and argv[1] == "--frequency-range":
        frequency_ranges()
    else:
        def process_callback(sound_class):
            """
            Callback function to handle sound classifications.

            This function is called when a sound classification is made. It
            prints the detected sound class unless it's "silence."

            Args:
                sound_class (str): The detected sound class.

            Example:
                # Define a callback function to process sound classifications
                def callback(sound_class):
                    print("Detected Sound Class:", sound_class)
            """
            if sound_class != "silence":
                print(sound_class)
            else:
                print("silence")

        process_audio(process_callback)


if __name__ == "__main__":
    main()
