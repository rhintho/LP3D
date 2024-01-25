from terminal.log import Log
from terminal.main_menu import MainMenu
from image.image import Image

if __name__ == '__main__':
    log = Log('Main')
    log.info("Program starting")

    cm = MainMenu()

    img = Image('images/hs_1.jpg')
    log.info(img)
