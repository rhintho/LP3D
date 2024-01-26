import cv2 as cv
from image.super_res_image.super_resolution import SuperResolution
from image.image import Image
from image.image_viewer import ImageViewer
from terminal.log import Log


class NearestNeighbor(SuperResolution):

    def __init__(self):
        super().__init__()
        self._log = Log(self.__class__.__name__)

    def resize(self, original_image: Image, scale_factor: int):
        scaled_width = int(original_image.get_width()) * scale_factor
        scaled_height = int(original_image.get_height()) * scale_factor
        self._log.debug(f"Scaled width: {scaled_width}, height: {scaled_height}")
        res = cv.resize(original_image.get_img(), (scaled_width, scaled_height),
                        interpolation=cv.INTER_NEAREST)
        new_img = original_image
        new_img.set_img(res)
        return new_img
