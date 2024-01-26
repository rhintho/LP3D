from app_manager import AppManager
from terminal.argument_handler import ArgumentHandler
from terminal.log import Log
from image.image import Image
from image.super_res_image.nearest_neighbor import NearestNeighbor

if __name__ == '__main__':
    log = Log('Main')
    log.info("LP3D program starting")

    ah = ArgumentHandler()
    ah.parse_args()
    ah.log_arguments()
    args = ah.get_args()

    app = AppManager()
    app.start_processing(args)


    log.info(f"LP3D terminated.")

