from pyaudio import PyAudio


class AudioManager:
    """
    Audio manager for handling PyAudio instances.

    This class provides a context manager for managing PyAudio instances for
    audio input and output. It creates a PyAudio instance when entering the
    context and terminates it when exiting the context.

    Example:
        # Import necessary libraries and modules
        from pyaudio import PyAudio

        # Create an audio manager instance using a context
        with AudioManager() as audio_manager:
            # Use the audio manager to work with PyAudio
            stream = audio_manager.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True)
            # Perform audio processing or recording here

        # PyAudio is terminated automatically when exiting the context
    """

    def __enter__(self):
        self.p = PyAudio()
        return self.p

    def __exit__(self, exc_type, exc_value, traceback):
        if self.p:
            self.p.terminate()
