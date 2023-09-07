from subprocess import run as execute
from audio_processor import process_audio

# TODO: Remove reliance on flashfocus
FLASH_WINDOW_COMMAND = "flash_window"  # Requires: flashfocus


def main():
    """
    Main entry point of the audio processing program with window flashing.

    This function serves as the main entry point for the program. It processes
    audio data and flashes the window when a "bass" sound is detected.

    Example:
        # Run the program to process audio data and flash the window for bass
        python main.py
    """
    def process_callback(sound_class):
        """
        Callback function to handle sound classifications and flash the window.

        This function is called when a sound classification is made. It checks
        if the detected sound class is "bass" and triggers window flashing.

        Args:
            sound_class (str): The detected sound class.

        Example:
            # Define a callback function to process sound classifications
            def callback(sound_class):
                if sound_class == "bass":
                    print("Bass Detected!")
        """
        if sound_class == "bass":
            execute(FLASH_WINDOW_COMMAND, text=False, check=True)

    process_audio(process_callback)


if __name__ == "__main__":
    main()
