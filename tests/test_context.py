""" Testing Context """
from pic.manage.context import Context
from pic.model.config import Config

class TestContext:
    """ pytest """

    def test_change_context(self):
        """ Test to check if change context """

        # check if context change
        context = Context()
        context.change_context('remote')

        config = Config()
        assert config.config['context'] == 'remote'