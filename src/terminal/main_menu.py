from terminal.log import Log


class MainMenu:

    def __init__(self):
        self._log = Log(self.__class__.__name__)
        self._log.debug('Console Menu started')
