""" Module to load configurations """

from .install import Install

class Config():
    """ class config """

    def __init__(self) -> None:
        self.install = Install()
        print("hola")

    def load_config(self):
        """ load """
        print("hola mundo")
