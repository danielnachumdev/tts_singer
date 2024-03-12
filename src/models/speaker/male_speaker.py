from .speaker import Speaker


class MaleSpeaker(Speaker):
    def __init__(self) -> None:
        super().__init__(Speaker._create_engine())


__all__ = [
    "MaleSpeaker"
]
