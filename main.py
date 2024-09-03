from pic.model.config import Config

config = Config()

p = config.load_configs()

# context = p['context']

# contexts = p['contexts'][context]

# print(contexts['path_kits'])


for a in p['path_servers'].items():
    for b in a:
        print(b)

# for pic in p.items():
#     print(pic['contexts'])

