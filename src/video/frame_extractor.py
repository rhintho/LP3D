import subprocess
from pathlib import Path

from terminal.log import Log


class FrameExtractor:

    def __init__(self, dir_path: str, fps: int = 10):
        self._log = Log(self.__class__.__name__)
        self._fps = fps
        self._dir_path = Path(dir_path)
        self._dir_name = self._dir_path.name
        self._target_path = self._dir_path.parent.joinpath(self._dir_name + '_' + str(fps) + "_fps")
        self._target_path.mkdir(exist_ok=True)

    def process_frame_extraction(self):
        # Get items of source folder
        items = []
        for item in self._dir_path.iterdir():
            if not item.is_dir() and not item.name.startswith("."):
                items.append(item)

        # Running ffmpeg for every item
        for item in items:
            file_name, file_extension = item.stem, item.suffix
            target = self._dir_path.joinpath(file_name + "_%04d.png")
            args = ["ffmpeg", "-i", item, "-vf", "fps={}".format(self._fps), target]  # TODO make ffmpeg accessible
            self._log.debug(f'Processing frame extraction: {args}')
            subprocess.run(args)
