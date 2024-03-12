from .speaker import Speaker


class FemaleSpeaker(Speaker):
    def __init__(self) -> None:
        engine = Speaker._create_engine()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
        super().__init__(engine)


__all__ = [
    "FemaleSpeaker"
]
