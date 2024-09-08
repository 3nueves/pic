""" Module to load configurations """
import yaml

from pathlib import Path
from git import Repo

from .install import Install
    
class Config():
    """ class config """

    CONFIG_FILE_PIC = 'pic/config.yaml'

    path = {
        'kits': 'pic.yaml',
        'servers': 'servers.yaml',
        'secrets':'secrets.yaml'
    }

    keep_config = {}

    def __init__(self) -> None:
        self.yml = yaml
        self.install = Install()
        self.path_home = Path.home()
        self.pic_config = self.path_home.joinpath(self.CONFIG_FILE_PIC)
        self.config = self.load_config_pic()


    def load_config_pic(self) -> str:
        """ load pic config """
        return self.read_config(self.pic_config)


    def read_config(self, route_file:str) -> dict:
        """ Read config file about pic"""
        try:
            with open(route_file, "r", encoding="utf-8") as file:
                try:
                    return self.yml.safe_load(file)

                except ValueError:
                    print("Error Reading File")

        except FileNotFoundError as error:
            print(error)


    def load_configs(self) -> dict:
        """ load config """
        for key, path in self.path.items():
            try:
                path_config = self.config['contexts'][self.config['context']][key]
                self.keep_config[key] = (self.read_config(path_config + '/' + path))

            except (ValueError, KeyError) as error:
                print(f'\n keyError: {error} has a mistake\n')
                exit()
        
        return self.keep_config
