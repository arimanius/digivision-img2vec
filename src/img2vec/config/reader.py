from copy import deepcopy

import yaml

from img2vec.config.config import Config


def read(config: Config) -> Config:
    config = deepcopy(config)
    with open(config.config_file) as f:
        config.update(**yaml.safe_load(f))
    return config
