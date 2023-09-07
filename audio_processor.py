import numpy as np
from audio.stream import initialize_stream
from audio.manager import AudioManager
from config import CHUNK_SIZE, FORMAT, CHANNELS, RATE, THRESHOLD
from audio.classifier import classify_audio


def process_audio(process_callback):
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
                        sound_class = classify_audio(audio_data, RATE)

                        if sound_class != previous_classification:
                            previous_classification = sound_class

                            # Call the provided process_callback function
                            process_callback(sound_class)
                    else:
                        pass
            except KeyboardInterrupt:
                pass
            finally:
                stream.stop_stream()
                stream.close()
    except Exception as e:
        print("An unexpected error occurred:", e)
