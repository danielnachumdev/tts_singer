from danielutils import create_directory, clear_directory, WorkerPool
from ..speaker import Speaker
from ..melody import Melody
from .singer_worker import SingerWorker


class Singer:
    def __init__(self, speaker: Speaker) -> None:
        self.speaker = speaker

    def sing(self, melody: Melody) -> None:
        create_directory("./tmp")
        clear_directory("./tmp")

        pool = WorkerPool(1, SingerWorker, {}, {})
        for i, info in enumerate(melody):
            pool.submit((i, info, self.speaker))
            break
        pool.start()

    def save(self, melody: Melody, path: str) -> None:
        pass
