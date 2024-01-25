import cv2 as cv
from terminal.log import Log


class ImageViewer:
    WINDOW_NAME = "LP3D Image Viewer"

    def __init__(self, img):
        self._log = Log(self.__class__.__name__)
        self._img = img

    def get_img(self):
        return self._img

    def set_img(self, img):
        self._img = img

    def show_image(self):
        if self._img is not None:
            cv.imshow(self.WINDOW_NAME, self._img)
            self._log.info(f"Showing image window and waiting for user key input to close the window.")
            cv.waitKey(0)  # TODO how can I manage the input?
            cv.destroyWindow(self.WINDOW_NAME)
            self._log.info("Window closed.")
        else:
            self._log.error("Image not found!")

    img = property(get_img, set_img)
