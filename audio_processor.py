import numpy as np
from audio.stream import initialize_stream
from audio.manager import AudioManager
from audio.classifier import classify_audio
from config import CHUNK_SIZE, FORMAT, CHANNELS, RATE, THRESHOLD


def process_audio(process_callback):
    """
    Continuously process audio data from an input audio stream.

    This function initializes an audio stream, continuously reads audio chunks,
    classifies the audio data, and invokes a callback function with the
    classification result when a significant sound is detected based on a
    predefined threshold.

    Args:
        process_callback (callable): A callback function to handle the
            classification results.

    Example:
        # Import necessary libraries and modules
        import numpy as np
        from audio.stream import initialize_stream
        from audio.manager import AudioManager
        from audio.classifier import classify_audio
        from config import CHUNK_SIZE, FORMAT, CHANNELS, RATE, THRESHOLD

        # Define a callback function to process sound classifications
        def callback(sound_class):
            print("Detected Sound Class:", sound_class)

        # Process audio data and invoke the callback
        process_audio(callback)
    """
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
