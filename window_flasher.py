from subprocess import run as exec
from audio_processor import process_audio

# TODO: Remove reliance on flashfocus
FLASH_WINDOW_COMMAND = "flash_window"  # Requires: flashfocus

'''
Flashes the window when a bass is detected using the flashfocus 'focus_window' command.
Intended for Eye-Candy Purposes.
'''

# TODO: Daemonize


def main():
    def process_callback(sound_class):
        if sound_class == "bass":
            exec(FLASH_WINDOW_COMMAND, text=False)

    process_audio(process_callback)


if __name__ == "__main__":
    main()
