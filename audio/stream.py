def initialize_stream(p, audio_format, num_channels, sampling_rate, chunk_size):
    stream = p.open(
        format=audio_format,
        channels=num_channels,
        rate=sampling_rate,
        input=True,
        frames_per_buffer=chunk_size
    )
    return stream
