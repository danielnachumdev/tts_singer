import time

from danielutils import create_directory, clear_directory, WorkerPool
from ..speaker import Speaker
from ..melody import Melody
from .singer_worker import SingerWorker
import threading

class Singer:
    def __init__(self, speaker: Speaker) -> None:
        self.speaker = speaker

    def sing(self, melody: Melody) -> None:
        create_directory("./tmp")
        clear_directory("./tmp")
        pool = WorkerPool(2, SingerWorker, {}, {})
        for i, info in enumerate(melody):
            pool.submit((i, info, self.speaker))
        pool.start()
        pool.join()

    def save(self, melody: Melody, path: str) -> None:
        pass
