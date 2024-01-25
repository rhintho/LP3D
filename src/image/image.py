import cv2 as cv
import numpy as np
from terminal.log import Log
from image.image_viewer import ImageViewer


class Image:

    def __init__(self, img_path: str):
        self._log = Log(self.__class__.__name__)
        self._img = cv.imread(img_path)
        self._px = 0
        self._py = 0
        self._width = self._img.shape[1]
        self._height = self._img.shape[0]
        self._rois = {}

    def show_image(self):
        iv = ImageViewer(self._img)
        iv.show_image()

    def get_shape(self):
        return self._img.shape

    def get_size(self):
        return self._img.size

    def get_channels(self):
        return self._img.shape[2]

    def get_height(self):
        return self._height

    def get_width(self):
        return self._width

    def get_blue_channel(self):
        b, g, r = cv.split(self._img)
        return b

    def get_green_channel(self):
        b, g, r = cv.split(self._img)
        return g

    def get_red_channel(self):
        b, g, r = cv.split(self._img)
        return r

    def get_pixel_color(self, x, y):
        return self._img[y, x]

    def set_pixel_color(self, x, y, ):
        pass

    def get_img(self):
        return self._img

    def set_img(self, img):
        self._img = img

    # def set_roi(self, x1: int, y1: int, x2: int, y2: int, name: str):
    #     roi = self._img[x1:y1, x2:y2]
    #     self._log.debug(roi)
    #     self._rois.update({name: roi})
    #     return roi
    #
    # def get_roi_list(self) -> [str]:
    #     return self._rois
    #
    # def get_roi(self, name: str):
    #     return self._rois[name]
    #
    # def save_roi(self, name: str):
    #     self._log.debug(self.get_roi(name))
    #     cv.imwrite(f"images/{name}.jpg", self._rois[name])

    def __str__(self):
        return (f"Image width {self._width} and height {self._height}, "
                f"Image size {self._img.size}, Image channels: {self.get_channels()}")

    def __repr__(self):
        return f"Image(width={self._width}, height={self._height}, size={self._img.size})"
