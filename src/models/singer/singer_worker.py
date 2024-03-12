from danielutils import Worker
from ..melody_info import MelodyInfo
from ..speaker import Speaker
from ..audio_processing import AudioSample


class SingerWorker(Worker):
    def _work(self, obj: tuple[int, MelodyInfo, Speaker]) -> None:
        """execution of a single job
        """
        i, info, speaker = obj
        src_name = f"./tmp/{i}.wav"
        processed_name = f"./tmp/{i}p.wav"
        print(f"id = {self.id} index = {i}")
        speaker.save(info.phrase, src_name)
        AudioSample.load(src_name).set_pitch(info.pitch_hz).set_speed(info.wpm).save(processed_name)
