import cv2 as cv
from image.image import Image
from terminal.log import Log


class AreaRelation():

    def __init__(self):
        super().__init__()
        self._log = Log(self.__class__.__name__)

    def resize(self, original_image: Image) -> Image:
        scaled_width: int = int(original_image.get_width() / 4)
        scaled_height: int = int(original_image.get_height() / 4)
        new_image = self._resize_cv(original_image, scaled_width, scaled_height)
        new_image = self.process_black_white(new_image)
        new_image.extend_filename(f"_shrink")
        return new_image

    def _resize_cv(self, original_image: Image, new_width: int, new_height: int) -> Image:
        res = cv.resize(original_image.get_img(), (new_width, new_height), interpolation=cv.INTER_AREA)
        new_image = Image()
        new_image.set_img(res)
        new_image.set_dir_path(original_image.get_dir_path())
        new_image.set_name(original_image.get_name())
        return new_image

    def process_black_white(self, original_image: Image) -> Image:
        img_grey = cv.cvtColor(original_image.get_img(), cv.COLOR_BGR2GRAY)
        original_image.set_img(img_grey)
        return original_image

