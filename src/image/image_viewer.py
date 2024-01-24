import cv2
from terminal.log import Log


class ImageViewer:
    def __init__(self, img):
        self._log = Log(self.__class__.__name__)
        self._img = img
        print(type(self._img))

    def get_img(self):
        return self._img

    def set_img(self, img):
        self._img = img

    def show_image(self):
        if self.img is not None:
            cv2.imshow('LP3D Image Viewer', self._img)
            self._log.info(f"Showing image window and waiting for user key input to close the window.")
            cv2.waitKey(0)  # TODO how can I manage the input?
            cv2.destroyAllWindows()
            self._log.info("Window closed.")
        else:
            self._log.error("Image not found!")

    img = property(get_img, set_img)
