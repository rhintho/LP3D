import os

from image.image import Image
from image.super_res_image.bicubic import Bicubic
from image.super_res_image.bilinear import Bilinear
from image.super_res_image.lanczos import Lanczos
from image.super_res_image.lap_srn import LapSRN
from image.super_res_image.nearest_neighbor import NearestNeighbor
from terminal.log import Log
from video.frame_extractor import FrameExtractor


class AppManager:
    accepted_fileformat = ['.png', '.jpg', '.jpeg']

    def __init__(self):
        self._log = Log(self.__class__.__name__)

    def start_processing(self, args):
        if args.module == 'super-res':
            self.prepare_super_res_process(args)
        elif args.module == 'frame-ext':
            self.prepare_frame_extraction(args)
        else:
            self._log.error("Something went wrong with module argument.")

    def prepare_super_res_process(self, args):
        self._log.info("Starting super resolution process.")
        img_dir, img_list = self.get_file_information(args.path.replace("'", ""))
        self._log.debug(f"Dir path: {img_dir}, Image list: {img_list}")
        self.select_method(img_dir, img_list, args)

    def prepare_frame_extraction(self, args):
        self._log.info("Starting frame extraction process.")
        dir_path = args.path.replace("'", "")
        frame_count = args.factor
        self.processing_frame_extraction(dir_path, frame_count)

    def select_method(self, img_dir, img_list, args):
        if args.method == 'nearest-neighbor':
            nn = NearestNeighbor()
            self.processing_super_resolution(img_dir, img_list, args.factor, nn)
        elif args.method == 'bilinear':
            bilinear = Bilinear()
            self.processing_super_resolution(img_dir, img_list, args.factor, bilinear)
        elif args.method == 'bicubic':
            bicubic = Bicubic()
            self.processing_super_resolution(img_dir, img_list, args.factor, bicubic)
        elif args.method == 'lanczos':
            lanczos = Lanczos()
            self.processing_super_resolution(img_dir, img_list, args.factor, lanczos)
        elif args.method == 'lapsrn':
            lapsrn = LapSRN()
            self.processing_super_resolution(img_dir, img_list, args.factor, lapsrn)

    def processing_super_resolution(self, img_dir, img_list, scale_factor, method_obj):
        for img_filename in img_list:
            img = Image()
            img.load_image(self._get_image_path(img_dir, img_filename))
            self._log.debug(f"Loaded {img}")
            img = method_obj.resize(img, int(scale_factor))
            img.save()

    def _get_image_path(self, img_dir, img_filename):
        return str(os.path.join(img_dir, img_filename))

    def get_file_information(self, path):
        img_list = []
        dir_path = ""
        if os.path.isdir(path):
            dir_path = path
            for file in os.listdir(path):
                name, ext = os.path.splitext(file)
                if ext.lower() in self.accepted_fileformat:
                    img_list.append(file)
        else:
            dir_path, filename = os.path.split(path)
            img_list.append(filename)
        return dir_path, img_list

    def processing_frame_extraction(self, dir_path, frame_count):
        frame_ext = FrameExtractor(dir_path, frame_count)
        frame_ext.process_frame_extraction()
