""" Module to change context """
import yaml

from ..model.config import Config

class Context():
    """ Manage Contexts """
    
    def __init__(self):
        self.conf = Config()
        self.config = self.conf.config
        self.file = self.conf.pic_config

    def check_context_exist(self, context):
        """Check if exist context"""

        # find if context exist
        for ctx in self.config['contexts']:
            if ctx == context:
                return True

        return False

    def change_context(self, context):
        """Change context"""

        # check if context exist
        if not self.check_context_exist(context):
            print('\n -- Context not exists --\n')
            exit()

        # Change context
        self.config['context'] = context

        # Convert to yaml
        config_file = yaml.dump(self.config, default_flow_style=False)

        # Save changes
        file = open(self.file, 'w', encoding="utf-8")
        file.writelines(config_file)
        file.close()

        print(f'\n\n-- Context "{context}" changed succefully --\n\n')
