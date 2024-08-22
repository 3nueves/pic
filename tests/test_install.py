""" Testing """
import pytest
import pathlib
import shutil

from os import path

from pic.model.install import Install

# const env
FOLDER_PIC = '/Users/davidmoyalopez/pic'

class TestInstall:
    """ pytest """

    def test_install(self):
        """ Test to check if ok """
        install = Install()
        home = pathlib.Path.home()
        route = home.joinpath('pic')
        install.create_folders_and_files()
        shutil.rmtree(route)
        assert str(route) == FOLDER_PIC

        # self.install.create_kit()
        # self.install.installed()
        
        