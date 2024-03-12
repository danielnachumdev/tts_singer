from typing import Optional
import pyttsx3
from pyttsx3 import Engine
from danielutils import atomic
from ...consts import WPM_VALUES


class Speaker:
    @staticmethod
    def _create_engine() -> Engine:
        return pyttsx3.init()

    def __init__(self, engine: Optional[Engine] = None) -> None:
        self.engine = engine if engine is not None else Speaker._create_engine()

    @atomic
    def say(self, sentence: str) -> "Speaker":
        self.engine.say(sentence)
        self.engine.runAndWait()
        return self

    @atomic
    def save(self, sentence: str, path: str) -> None:
        self.engine.save_to_file(sentence, path)
        self.engine.runAndWait()

    def __del__(self) -> None:
        self.engine.stop()

    @property
    def wpm(self) -> int:
        return self.engine.getProperty('rate')

    @wpm.setter
    def wpm(self, v: int | WPM_VALUES) -> None:
        if isinstance(v, WPM_VALUES):
            v = v.value
        self.engine.setProperty('rate', v)

    @property
    def volume(self) -> float:
        return self.engine.getProperty('volume')

    @volume.setter
    def volume(self, v: float) -> None:
        if not (0 <= v <= 1):
            raise ValueError("volume can only be a number between 0 and 1")
        self.engine.setProperty('volume', v)


__all__ = [
    "Speaker"
]
