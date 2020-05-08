from mlLogger.cli import *
from mlLogger.db import *
import os

if not config_present:
    config_path = os.environ['HOME']+'/mlLogger-config.json'
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=4)


if __name__ == "__main__":
    base()