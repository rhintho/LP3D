import cv2 as cv
from terminal.log import Log
from image.image_viewer import ImageViewer


class Image:

    def __init__(self, img_path: str):
        self._log = Log(self.__class__.__name__)
        self._img = cv.imread(img_path)
        self._px = 0
        self._py = 0

    def show_image(self):
        iv = ImageViewer(self._img)
        iv.show_image()
