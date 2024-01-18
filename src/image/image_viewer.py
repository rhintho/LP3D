import cv2


class ImageViewer:
    def __init__(self, img_path):
        self._img_path = img_path
        self._img = cv2.imread(self._img_path, cv2.IMREAD_COLOR)

    def get_img_path(self):
        return self._img_path

    def set_img_path(self, img_path):
        self._img_path = img_path
        self._img = cv2.imread(self._img_path, cv2.IMREAD_COLOR)

    def get_img(self):
        return self._img

    def set_img(self, img_path):
        self.set_img_path(img_path)

    def show_image(self):
        cv2.imshow('Image Viewer', self._img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    img_path = property(get_img_path, set_img_path)
    img = property(get_img, set_img)


if __name__ == '__main__':
    iv = ImageViewer('../../images/red_octo.jpg')
    iv.show_image()
