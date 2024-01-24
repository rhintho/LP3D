from terminal.log import Log
from terminal.main_menu import MainMenu
from image.image_viewer import ImageViewer

if __name__ == '__main__':

    log = Log('Main')
    log.info("Program starting")

    cm = MainMenu()

    iv = ImageViewer('images/hs_1.jpg')
    iv.show_image()


