import subprocess
import cv2 as cv
from pathlib import Path

from terminal.log import Log


class FrameExtractor:

    def __init__(self, dir_path: str, frame_count: int = 10):
        self._log = Log(self.__class__.__name__)
        self._frame_count = frame_count
        self._dir_path = Path(dir_path)

    def process_frame_extraction(self):
        # Get items of source folder
        items = []
        for item in self._dir_path.iterdir():
            if not item.is_dir() and not item.name.startswith("."):
                items.append(item)
        # Create target folder with name frame_#
        target_dir = Path(str(self._dir_path) + f"/frame_{self._frame_count}")
        target_dir.mkdir(parents=True, exist_ok=True)

        # Running ffmpeg for every item
        for item in items:
            self._log.info(f"Processing video file {item}.")
            video = cv.VideoCapture(str(item))
            if video.isOpened():
                i = 1
                while True:
                    ret, frame = video.read()
                    if not ret:
                        break
                    cv.imwrite(f'{target_dir}/{i}.jpg', frame)
                    i += 1
            video.release()
