import numpy as np
from sys import argv
from sound.classifier import classify_sound
from audio.stream import initialize_stream
from audio.manager import AudioManager
from utils.frequency import frequency_ranges
from config import CHUNK_SIZE, FORMAT, CHANNELS, RATE, THRESHOLD


def main():
    # TODO: Implement argument validation and handling for unexpected inputs
    # TODO: Help menu
    if len(argv) > 1 and argv[1] == "--frequency-range":
        frequency_ranges()
    else:
        try:
            with AudioManager() as audio_manager:
                stream = initialize_stream(
                    audio_manager,
                    FORMAT,
                    CHANNELS,
                    RATE,
                    CHUNK_SIZE)

                previous_classification = None
                print("Listening for sound...")

                try:
                    while True:
                        audio_data = np.frombuffer(
                            stream.read(CHUNK_SIZE), dtype=np.int16)
                        max_amplitude = np.max(np.abs(audio_data))

                        if max_amplitude > THRESHOLD:
                            sound_class = classify_sound(audio_data, RATE)

                            if sound_class != previous_classification:
                                previous_classification = sound_class
                                print(sound_class)
                        else:
                            if previous_classification != "silence":
                                previous_classification = "silence"
                                print("silence")
                except KeyboardInterrupt:
                    pass
                finally:
                    stream.stop_stream()
                    stream.close()

        except Exception as e:
            print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
