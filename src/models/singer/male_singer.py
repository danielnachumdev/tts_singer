from .singer import Singer
from ..speaker import MaleSpeaker


class MaleSinger(Singer):
    def __init__(self) -> None:
        super().__init__(MaleSpeaker())


__all__ = [
    "MaleSinger"
]
