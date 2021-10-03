import yaml
from easydict import EasyDict
from pathlib import Path


def transfer_str_yaml_to_easydict(str_yaml):
    # type: (str) -> EasyDict
    """
    transfers yaml based string to EasyDict
    :param str_yaml: yaml based string
    :return: r_config
    """
    f_config = yaml.load(str_yaml, Loader=yaml.SafeLoader)

    return EasyDict(f_config)


def update_the_main_config(str_yaml, r_config=None):
    # type: (str, EasyDict) -> EasyDict
    """
    updates r_config a with given EasyDict
    :param str_yaml: yaml based string
    :param r_config: previous r_config
    :return: updated r_config
    """
    if r_config is None:
        r_config = EasyDict()

    cf = transfer_str_yaml_to_easydict(str_yaml)

    r_config.update(cf)
    return r_config


def load_config(config_path):
    # type: (str | Path) -> str
    """
    loads a yaml based config file as string
    :param config_path: path of config file
    :return: content of config file
    """
    with open(config_path) as config_file:
        result = config_file.read()
    return result


def update_the_main_config_with_path(config_path, r_config=None):
    # type: (str | Path, EasyDict) -> EasyDict
    """
    updates r_config with a given path
    :param config_path: path of config file
    :param r_config: previous r_config
    :return: updated r_config
    """
    str_yaml = load_config(config_path)

    r_config = update_the_main_config(str_yaml, r_config)

    return r_config
