from cli import *
from db import *

if not config_present:
    print(os.path.dirname(__file__))
    config_path = os.path.join(os.path.dirname(__file__),'db/config.json')
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)


if __name__ == "__main__":
    base()