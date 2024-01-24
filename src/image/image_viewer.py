import cv2
from terminal.log import Log


class ImageViewer:
    def __init__(self, img_path):
        self._img_path: str = img_path
        self._img = cv2.imread(self._img_path, cv2.IMREAD_COLOR)
        self._log = Log(self.__class__.__name__)

    def get_img_path(self) -> str:
        return self._img_path

    def set_img_path(self, img_path: str) -> None:
        self._img_path = img_path
        self._img = cv2.imread(self._img_path, cv2.IMREAD_COLOR)

    def get_img(self):
        return self._img

    def set_img(self, img_path: str) -> None:
        self.set_img_path(img_path)

    def show_image(self):
        if self.img is not None:
            cv2.imshow('Open CV Image Viewer', self._img)
            self._log.info(f"Showing image {self._img_path} and waiting for user key input.")
            cv2.waitKey(0)  # TODO how can I manage the input?
            cv2.destroyAllWindows()
            self._log.info("Window closed.")
        else:
            self._log.error("Image not found!")

    img_path = property(get_img_path, set_img_path)
    img = property(get_img, set_img)
