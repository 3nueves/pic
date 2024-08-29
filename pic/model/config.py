""" Module to load configurations """

from .install import Install

class Config():
    """ class config """

    def __init__(self) -> None:
        self.install = Install()

    def load_config(self):
        """ load """
        pass