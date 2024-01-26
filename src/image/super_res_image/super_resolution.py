from abc import abstractmethod


class SuperResolution:

    def __init__(self):
        pass

    @abstractmethod
    def resize(self, image, scale_factor):
        pass
