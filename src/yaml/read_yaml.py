import yaml
import pprint

with open("config.yml", 'r') as stream:
    try:
        # data = yaml.load(stream)  # single doc
        data = list(yaml.load_all(stream))
        pprint.pprint(data)
    except yaml.YAMLError as exc:
        print(exc)
