import numpy as np
from constants import FREQUENCY_RANGES


def classify_audio(audio_data, rate):
    fft_result = np.fft.fft(audio_data)
    frequencies = np.fft.fftfreq(len(fft_result), d=1/rate)

    energy_levels = {}
    for label, (start_freq, end_freq) in FREQUENCY_RANGES.items():
        energy = np.sum(np.abs(fft_result[
            (frequencies >= start_freq) & (frequencies <= end_freq)]))
        energy_levels[label] = energy

    dominant_range = max(energy_levels, key=energy_levels.get)
    return dominant_range
