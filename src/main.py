from terminal.log import Log
from image.image import Image
from image.super_res_image.nearest_neighbor import NearestNeighbor

if __name__ == '__main__':
    log = Log('Main')
    log.info("Program starting")

    log.info("Create image instance.")
    img = Image('images/hs_1.jpg')
    log.info(img)

    nn_tech = NearestNeighbor()
    new_img = nn_tech.resize(img)
    new_img.show_image()
