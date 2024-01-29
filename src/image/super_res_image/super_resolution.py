from abc import abstractmethod

from image.image import Image


class SuperResolution:

    def __init__(self):
        pass

    @abstractmethod
    def resize(self, image, scale_factor) -> Image:
        pass

    @abstractmethod
    def create_file_name(self) -> str:
        pass

    def calc_new_width(self, original_width: int, scaling_factor: int) -> int:
        return original_width * scaling_factor

    def calc_new_height(self, original_height: int, scaling_factor: int) -> int:
        return original_height * scaling_factor


