import numpy as np
from scipy.io import wavfile as wav


class AudioSample:
    @staticmethod
    def load(path: str) -> "AudioSample":
        sr, data = wav.read(path)
        return AudioSample(data, sr)

    def __init__(self, data: np.ndarray, sr: int) -> None:
        self.data = data
        self.sr = sr

    def set_pitch(self, hz: int) -> "AudioSample":
        return self

    def set_speed(self, wpm: int) -> "AudioSample":
        return self

    def save(self, path: str) -> None:
        wav.write(path, self.sr, self.data)

    def _histogram(self) -> None:
        pass

    def _spectogram(self) -> None:
        pass


__all__ = [
    "AudioSample"
]
