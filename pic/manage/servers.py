""" Module to manage servers """

from pic.model.config import Config

class Servers:
    """ class Manage Servers """

    def __init__(self) -> None:
        config = Config()
        server_config = config.load_configs()
        print(server_config['servers'])
