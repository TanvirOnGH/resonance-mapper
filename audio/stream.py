import pyaudio


def initialize_stream(p, format, channels, rate, chunk_size):
    stream = p.open(
        format=format,
        channels=channels,
        rate=rate,
        input=True,
        frames_per_buffer=chunk_size
    )
    return stream
