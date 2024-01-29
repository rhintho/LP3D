import os

import cv2 as cv

from image.image_viewer import ImageViewer
from terminal.log import Log


class Image:

    def __init__(self):
        self._log = Log(self.__class__.__name__)
        self._filename = None
        self._img = None
        self._px = 0
        self._py = 0
        self._width = None
        self._height = None
        self._rois = {}
        self._dirpath = None

    def set_img(self, img):
        self._img = img
        self._width = img.shape[1]
        self._height = img.shape[0]

    def load_image(self, image_path):
        self._dirpath = os.path.dirname(image_path)
        loaded_image = cv.imread(image_path)
        self._filename = os.path.basename(image_path)
        self.set_img(loaded_image)

    def show_image(self):
        iv = ImageViewer(self)
        iv.show_image()

    def get_name(self):
        return self._filename

    def set_name(self, name):
        self._filename = name

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

    def get_dir_path(self):
        return self._dirpath

    def set_dir_path(self, dir_path):
        self._dirpath = dir_path

    def extend_filename(self, extension):
        filename, fformat = os.path.splitext(self._filename)
        filename = filename + extension + fformat
        self._log.debug(f"Extended filename: {filename}")
        self._filename = filename

    def save(self):
        self._log.debug(f"Saving image to {self._dirpath} + / + {self._filename}")
        cv.imwrite(str(os.path.join(self._dirpath, self._filename)), self._img)

    def __str__(self):
        return (f"Image \"{self._filename}\" with width {self._width} and height {self._height}, "
                f"Image size {self._img.size}, Image channels: {self.get_channels()}")

    def __repr__(self):
        return f"Image(width={self._width}, height={self._height}, size={self._img.size})"
