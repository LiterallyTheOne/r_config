import yaml
from easydict import EasyDict
from pathlib import Path


def load_config(config_path):
    # type: (str | Path) -> EasyDict
    """
    loads a yaml based config file
    """
    with open(config_path) as config_file:
        f_config = yaml.load(config_file, Loader=yaml.SafeLoader)
    return EasyDict(f_config)


def update_the_main_config(config_path, r_config):
    # type: (str | Path, EasyDict) -> None
    """
    updates r_config with the path given
    """
    cf = load_config(config_path)
    r_config.update(cf)
