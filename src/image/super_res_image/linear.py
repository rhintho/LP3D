from abc import ABC

import cv2 as cv
from image.super_res_image.super_resolution import SuperResolution
from image.image import Image
from terminal.log import Log


class Linear(SuperResolution, ABC):

    def __init__(self):
        super().__init__()
        self._log = Log(self.__class__.__name__)

    def resize(self, original_image: Image, scaling_factor: int) -> Image:
        scaled_width: int = self.calc_new_width(original_image.get_width(), scaling_factor)
        scaled_height: int = self.calc_new_height(original_image.get_height(), scaling_factor)
        new_image = self._resize_cv(original_image, scaled_width, scaled_height)
        new_image.extend_filename(f"_sr_linear_fac_{scaling_factor}")
        return new_image

    def _resize_cv(self, original_image: Image, new_width: int, new_height: int) -> Image:
        res = cv.resize(original_image.get_img(), (new_width, new_height), interpolation=cv.INTER_LINEAR)
        new_image = Image()
        new_image.set_img(res)
        new_image.set_dir_path(original_image.get_dir_path())
        new_image.set_name(original_image.get_name())
        return new_image
