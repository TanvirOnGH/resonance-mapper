def initialize_stream(p, audio_format, num_channels, sampling_rate, chunk_size):
    """
    Initialize an audio stream for recording.

    This function creates and configures an audio stream for recording audio
    using the provided audio format, number of channels, sampling rate, and
    chunk size.

    Args:
        p (audio_manager): An audio manager or audio processing library instance
            responsible for managing audio streams.
        audio_format (int): The audio format (e.g., pyaudio.paInt16) for the
            recorded audio.
        num_channels (int): The number of audio channels (e.g., 1 for mono, 2 for stereo).
        sampling_rate (int): The sampling rate in Hz for the audio stream.
        chunk_size (int): The size of audio data chunks to be read at a time.

    Returns:
        audio_stream: An initialized audio stream for recording.

    Example:
        # Import necessary libraries and modules
        import pyaudio

        # Define audio stream parameters
        audio_format = pyaudio.paInt16
        num_channels = 1
        sampling_rate = 44100
        chunk_size = 1024

        # Initialize an audio stream
        stream = initialize_stream(pyaudio.PyAudio(), audio_format, num_channels, sampling_rate, chunk_size)
    """
    stream = p.open(
        format=audio_format,
        channels=num_channels,
        rate=sampling_rate,
        input=True,
        frames_per_buffer=chunk_size
    )
    return stream
