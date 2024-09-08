from pic.model.config import Config
from pic.manage.context import Context
from pic.manage.servers import Servers
from pic.manage.git import Git

config = Config()
# context = Context()
# server = Servers()
# server = Git()

p = config.load_configs()
d = config.load_config_pic()

# context.change_context("git")


# context = p['context']

# contexts = p['contexts'][context]

# print(contexts['path_kits'])

# for c in d['contexts'].items():
#     for a in c:
#         print(a)

# print()

for a in p['kits']['kits']:
    print(a)

for pic in p['servers']['servers']:
    print(pic['hosts'])

