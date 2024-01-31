import argparse
from terminal.log import Log


class ArgumentHandler:

    def __init__(self):
        self._log = Log(self.__class__.__name__)
        self._parser = argparse.ArgumentParser(prog='LP3D',
                                               description='Lost Places in 3D - Application for a three-dimensional '
                                                           'reconstruction of historic buildings.')
        self._args = None
        self.add_super_resolution_args()

    def get_parser(self):
        return self._parser

    def log_arguments(self):
        self._log.info(f'Called arguments: MODULE {self._args.module} :: METHOD {self._args.method} :: '
                        f'FACTOR {self._args.factor} :: PATH {self._args.path}')

    def get_args(self):
        return self._args

    def parse_args(self):
        self._args = self._parser.parse_args()
        return self._args

    def add_super_resolution_args(self):
        self._parser.add_argument('module', help='Choosed module for image processing.',
                                  choices=['super-res', 'feature-detection', 'frame-ext'])
        self._parser.add_argument('-p', '--path', help='Selected image file or folder for processing.')
        self._parser.add_argument('-fac', '--factor', help='Defined scaling factor for super resolution.')
        self._parser.add_argument('-m', '--method', help='Selected method for super resolution process.',
                                  choices=['nearest-neighbor', 'bilinear', 'bicubic', 'lanczos',
                                           'edsr', 'espcn', 'fsrcnn', 'lapsrn'])
        self._parser.add_argument('-t', '--target', help='Selected dir for saving processed images.')

    def check_arguments(self):
        pass  # TODO Error handling for arguments missing
