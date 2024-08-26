""" Testing """
import pytest
import pathlib
import shutil

from os import path

from pic.model.install import Install

# const env
FOLDERS = {
    'pic': 'pic',
    'kits': 'pic/kits',
    'kits_sh': 'pic/kits/cmd',
    'servers': 'pic/servers',
    'secrets': 'pic/secrets'
}

FILES = {
    'pic': 'pic/config.yaml',
    'pic_install': 'pic/.installed',
    'kits': 'pic/kits/pic.yaml',
    'kits_sh': 'pic/kits/cmd/cmd.sh',
    'kits_pic': 'pic/kits/cmd/pic.yaml',
    'servers': 'pic/servers/servers.yaml',
    'secrets': 'pic/secrets/secrets.yaml'
}

class TestInstall:
    """ pytest """

    def test_check_class_install(self):
        """ Test to check if ok """
        install = Install()
        home = pathlib.Path.home()

        # Check if exiest Folders
        for folder in FOLDERS.values():
            assert path.exists(home.joinpath(folder))

       # Check if exiest Files
        for file in FILES.values():
            assert path.exists(home.joinpath(file))

        # Remove folder pic
        shutil.rmtree(home.joinpath(FOLDERS['pic']))
