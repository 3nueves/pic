""" Testing Config """
from pic.model.config import Config


class TestConfig:
    """ pytest """

    def test_load_config(self):
        """ Test to check if config return is ok """
        config = Config()

        # check pic config
        assert isinstance(config.load_config_pic(), dict)

        # check kits, servers and sercrets config
        assert isinstance(config.load_configs(), dict)
