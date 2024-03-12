from dataclasses import dataclass


@dataclass
class MelodyInfo:
    phrase: str
    pitch_hz: int = 440
    wpm: int = 200
    delay_seconds: float = 0


__all__ = [
    "MelodyInfo"
]
