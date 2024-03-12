from .melody_info import MelodyInfo


class Melody:
    @staticmethod
    def random_from_words(text: str) -> "Melody":
        n = len(text.split(" "))
        return Melody.from_words(text, [220 + i*20 for i in range(n)], [200 for _ in range(n)])

    @staticmethod
    def from_words(text: str, pitches: list[int], wpms: list[int]) -> "Melody":
        if not (len(words := text.split(" ")) == len(pitches) == len(wpms)):
            raise ValueError("lengths must be the same")
        return Melody([MelodyInfo(w, p, s) for w, p, s in zip(words, pitches, wpms)])

    def __init__(self, infos: list[MelodyInfo]) -> None:
        self.infos = infos

    def __iter__(self):
        return iter(self.infos)


__all__ = [
    "Melody"
]
