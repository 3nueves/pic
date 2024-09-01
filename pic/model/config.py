""" Module to load configurations """
import yaml

from pathlib import Path

from .install import Install

class Config():
    """ class config """

    PATH_CONFIG_FILE_PIC = 'pic/config.yaml'
    NAME_CONFIG_FILE_KITS = 'pic.yaml'


    def __init__(self) -> None:
        self.yml = yaml
        self.install = Install()
        self.path_home = Path.home()
        self.pic_config = self.path_home.joinpath(self.PATH_CONFIG_FILE_PIC)
        self.config = self.load_config_pic()


    def load_config_pic(self):
        """ load pic config """
        return self.__read_yaml(self.pic_config)


    def load_config_kits(self):
        """ load kits config """

        try:
            path_kits = self.config['contexts'][self.config['context']]['path_kits']
            return self.__read_yaml(path_kits + '/' + self.NAME_CONFIG_FILE_KITS)

        except (ValueError, KeyError) as error:
            print(f'\n keyError: {error} has a mistake\n')
            exit()


    def load_config_servers(self):
        """ load servers config  """
        pass


    def load_config_secrets(self):
        """ load secrets config  """
        pass


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