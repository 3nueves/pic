""" Module to load configurations """
import yaml

from pathlib import Path

from .install import Install

class Config():
    """ class config """

    PATH_CONFIG_FILE_PIC = 'pic/config.yaml'

    path = {
        'path_kits': 'pic.yaml',
        'path_servers': 'servers.yaml',
        'path_secrets':'secrets.yaml'
    }

    keep_config = {}

    def __init__(self) -> None:
        self.yml = yaml
        self.install = Install()
        self.path_home = Path.home()
        self.pic_config = self.path_home.joinpath(self.PATH_CONFIG_FILE_PIC)
        self.config = self.load_config_pic()


    def load_config_pic(self):
        """ load pic config """
        return self.__read_yaml(self.pic_config)


    def __read_yaml(self, route_file):
        """ Read config file about pic"""

        try:
            with open(route_file, "r", encoding="utf-8") as file:
                try:
                    return self.yml.safe_load(file)

                except ValueError:
                    print("Error Reading File")

        except FileNotFoundError as error:
            print(error)


    def load_configs(self):
        """ load config """
        for key, path in self.path.items():
            try:
                path_config = self.config['contexts'][self.config['context']][key]
                self.keep_config[key] = (self.__read_yaml(path_config + '/' + path))

            except (ValueError, KeyError) as error:
                print(f'\n keyError: {error} has a mistake\n')
                exit()
        
        return self.keep_config
