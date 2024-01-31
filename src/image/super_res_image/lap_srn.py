from abc import ABC

import cv2 as cv
from image.super_res_image.super_resolution import SuperResolution
from image.image import Image
from terminal.log import Log


class LapSRN(SuperResolution, ABC):

    def __init__(self):
        super().__init__()
        self._log = Log(self.__class__.__name__)
        self._model_path = 'models/LapSRN_x8.pb'
        self._scaling_factor = 8

    def resize(self, original_image: Image, scaling_factor: int) -> Image:
        result_image = self._resize_cv(original_image, scaling_factor)
        result_image.extend_filename(f'_sr_dnn_lapsrn_fac_{self._scaling_factor}')
        return result_image

    def _resize_cv(self, original_image: Image, scaling_factor: int) -> Image:  # scaling factor not useful here
        superres = cv.dnn_superres.DnnSuperResImpl.create()
        superres.readModel(self._model_path)
        superres.setModel('lapsrn', self._scaling_factor)
        res = superres.upsample(original_image.get_img())

        result_image = Image()
        result_image.set_img(res)
        result_image.set_name(original_image.get_name())
        result_image.set_dir_path(original_image.get_dir_path())
        return result_image
