""" Module to install app """
import pathlib
import yaml
from os import path


# These files are used to install pic.

home = pathlib.Path.home()

pic = {
    'contexts': {
        'local': {
            'kits':f'{home}/pic/kits', 
            'servers':f'{home}/pic/servers', 
            'secrets':f'{home}/pic/secrets',
            'mode': 'local'
        },
        'remote': {
            'kits':f'{home}/pic/kits', 
            'servers':f'{home}/pic/servers', 
            'secrets':f'{home}/pic/secrets',
            'mode': 'remote'
        },
        'git': {
            'kits':'https://github.com/3nueves/kits.git', 
            'servers':f'{home}/pic/servers', 
            'secrets':f'{home}/pic/secrets',
            'mode': 'remote'
        }
    },
    'context': 'local',
}

servers = {
    'servers': [
        {
        'name':'mariadb',
        'user': 'root',
        'hosts': ['192.168.1.55', '10.0.0.234'],
        'port':'22',
        'password':'$PASSWORD',
        'pkey': "/home/dml/.ssh/id_rsa"
        }
    ]
}

secrets = {
    'worker-1': ['secret'],
    'worker-2': ['secret']
}

kits = {
    'kits': ['cmd']
}

# Name of the kit
cmd = {
    'kits': {
        'uploads': 
        {
        'allways': [
            'cmd.sh'
        ],
        'once': [
            'name-file.txt'
        ],
        },
        'pipeline': [ 'cmd.sh' ]
    }
}

kit = """#!/bin/bash

exec "$@"
"""

kit_name = 'cmd'

# We save the path on dictionary where going to go config file
path_configs = {
    'pic': 'pic/config.yaml',
    'pic/kits': 'pic/kits/pic.yaml',
    f'pic/kits/{kit_name}': f'pic/kits/{kit_name}/pic.yaml',
    'pic/servers': 'pic/servers/servers.yaml',
    'pic/secrets': 'pic/secrets/secrets.yaml'
}

class Install():
    """
    Creating Folder and Config File 
    """

    configs = {
                'pic': pic, 
                'servers': servers,
                'secrets': secrets, 
                'kits': kits, 
                'cmd': cmd
            }

    def __init__(self) -> None:
        self.home = pathlib.Path.home()
        if not path.exists(self.home.joinpath('pic/.installed')):
            self.create_folders_and_files()
            self.create_kit()
            self.installed()


    def __create_file(self, route_file, config) -> None:
        """ Add config into the files """

        try:
            with open(str(route_file), "a+", encoding="utf-8") as file:
                file.seek(0)
                try:
                    file.writelines(config)
                except ValueError:
                    print("Error Creating File")
        except FileNotFoundError as error:
            print(error)


    def create_folders_and_files(self) -> None:
        """Create Folder if not exist"""

        for paths, file in path_configs.items():

            route_folder = self.home.joinpath(paths)
            route_file = self.home.joinpath(file)

            if not path.exists(route_folder) or not path.exists(route_file):
                
                print(f'route: {route_folder} file: {route_file}')

                # Creamos el directorio en la home
                pathlib.Path.mkdir(route_folder)
                
                # Cojemos la primera palabra de las key que tenemos en el diccionario path_configs
                folder = path.basename(route_folder)

                # recorremos configs y preguntamos si la primera palabra de de la key del diccionario path_configs 
                # coincide con la key del diccionario configs si es afirmativo guardamos el valor 
                # del diccionario configs en "config_file"
                config_file = [config[1] for config in self.configs.items() if config[0] == folder]

                # convertimos a yaml el diccionario
                config = yaml.dump(config_file[0], default_flow_style=False)

                # creamos el fichoro con los datos del diccionario
                self.__create_file(route_file, config)


    def create_kit(self) -> None:
        """ Only create kit """
        if not path.exists(self.home.joinpath(f'pic/kits/{kit_name}/{kit_name}.sh')):
            self.__create_file(self.home.joinpath(f'pic/kits/{kit_name}/{kit_name}.sh'), kit)


    def installed(self) -> None:
        """ Only create sign """
        if not path.exists(self.home.joinpath('pic/.installed')):
            self.__create_file(self.home.joinpath('pic/.installed'), 'installed')
