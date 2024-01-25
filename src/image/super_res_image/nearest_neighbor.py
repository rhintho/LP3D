import cv2 as cv
from image.super_res_image.super_resolution import SuperResolution
from terminal.log import Log


class NearestNeighbor(SuperResolution):

    def __init__(self):
        super().__init__()
        self._log = Log(self.__class__.__name__)

    def resize(self, image):
        old_img = image
        res = cv.resize(image, (int(old_img.shape[1]) * 2, int(old_img.shape[0]) * 2), interpolation=cv.INTER_NEAREST)

        cv.imshow('result', res)
        cv.waitKey(0)
        cv.destroyWindow('result')
