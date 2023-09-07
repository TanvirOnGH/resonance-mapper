import numpy as np
from constants import FREQUENCY_RANGES


def classify_audio(audio_data, rate):
    """
    Classify the dominant frequency range of an audio signal.

    This function calculates the Fast Fourier Transform (FFT) of the input audio
    data and determines the dominant frequency range based on predefined
    frequency ranges.

    Args:
        audio_data (array-like): The audio signal data.
        rate (int): The sampling rate of the audio signal in Hz.

    Returns:
        str: The label of the dominant frequency range.

    Example:
        # Import necessary libraries and constants
        import numpy as np
        from constants import FREQUENCY_RANGES

        # Define sample audio data and sampling rate
        audio_data = np.array([...])  # Replace with actual audio data
        rate = 44100  # Replace with the actual sampling rate

        # Classify the audio data into a dominant frequency range
        result = classify_audio(audio_data, rate)
        print("Dominant Frequency Range:", result)
    """
    fft_result = np.fft.fft(audio_data)
    frequencies = np.fft.fftfreq(len(fft_result), d=1/rate)

    energy_levels = {}
    for label, (start_freq, end_freq) in FREQUENCY_RANGES.items():
        energy = np.sum(np.abs(fft_result[
            (frequencies >= start_freq) & (frequencies <= end_freq)]))
        energy_levels[label] = energy

    dominant_range = max(energy_levels, key=energy_levels.get)
    return dominant_range
