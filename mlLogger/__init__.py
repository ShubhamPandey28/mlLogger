from mlLogger.cli import *
from mlLogger.db import *


if not config_present:
    config_path = '/home/mlLogger-config.json'
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)


if __name__ == "__main__":
    base()