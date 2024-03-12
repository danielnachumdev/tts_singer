from danielutils import Worker
from ..melody_info import MelodyInfo
from ..speaker import Speaker


class SingerWorker(Worker):
    def _work(self, obj: tuple[int, MelodyInfo, Speaker]) -> None:
        """execution of a single job
        """
        i, info, speaker = obj
        speaker.save(info.phrase, f"./tmp/{i}.mp3")
