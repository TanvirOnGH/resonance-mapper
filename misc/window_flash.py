import numpy as np
from subprocess import run as exec
from sound.classifier import classify_sound
from audio.stream import initialize_stream
from audio.manager import AudioManager
from config import CHUNK_SIZE, FORMAT, CHANNELS, RATE, THRESHOLD

# TODO: Remove reliance on flashfocus
FLASH_WINDOW_COMMAND = "flash_window"  # Requires: flashfocus

'''
Flashes the window when a bass is detected using the flashfocus 'focus_window' command.
Intended for Eye-Candy Purposes.
'''

# TODO: Daemonize
def flash_window_on_bass():
    try:
        with AudioManager() as audio_manager:
            stream = initialize_stream(
                audio_manager,
                FORMAT,
                CHANNELS,
                RATE,
                CHUNK_SIZE)

            previous_classification = None

            try:
                while True:
                    audio_data = np.frombuffer(
                        stream.read(CHUNK_SIZE), dtype=np.int16)
                    max_amplitude = np.max(np.abs(audio_data))

                    if max_amplitude > THRESHOLD:
                        sound_class = classify_sound(audio_data, RATE)

                        if sound_class != previous_classification:
                            previous_classification = sound_class

                            # TODO: Add handling for additional sound classes
                            if sound_class == "bass":
                                exec(FLASH_WINDOW_COMMAND, text=False)
                    else:
                        pass
            except KeyboardInterrupt:
                pass
            finally:
                stream.stop_stream()
                stream.close()
    except Exception as e:
        print("An unexpected error occurred:", e)
        return []


def main():
    flash_window_on_bass()


if __name__ == "__main__":
    main()
