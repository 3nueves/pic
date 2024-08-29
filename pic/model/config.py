""" Module to load configurations """

from .install import Install

class Config():
    """ class config """

    def __init__(self) -> None:
        self.install = Install()
