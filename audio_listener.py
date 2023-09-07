from sys import argv
from audio_processor import process_audio
from utils.frequency import frequency_ranges

# TODO: Implement argument validation and handling for unexpected inputs
# TODO: Help menu


def main():
    if len(argv) > 1 and argv[1] == "--frequency-range":
        frequency_ranges()
    else:
        def process_callback(sound_class):
            if sound_class != "silence":
                print(sound_class)
            else:
                print("silence")

        process_audio(process_callback)


if __name__ == "__main__":
    main()
