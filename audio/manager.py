from pyaudio import PyAudio


class AudioManager:
    def __enter__(self):
        self.p = PyAudio()
        return self.p

    def __exit__(self, exc_type, exc_value, traceback):
        if self.p:
            self.p.terminate()
