from pic.model.config import Config

from pic.manage.context import Context

config = Config()
context = Context()

p = config.load_configs()
d = config.load_config_pic()

context.change_context("gi")


# context = p['context']

# contexts = p['contexts'][context]

# print(contexts['path_kits'])

# for c in d['contexts'].items():
#     for a in c:
#         print(a)

# print()

# for a in p.items():
#     print(a)
    # for b in a:
    #     print(b)

# for pic in p.items():
#     print(pic['contexts'])

