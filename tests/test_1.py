import pytest

from r_config_loader.r_config_loader import RConfig


@pytest.fixture()
def r_config():
    # type: () -> RConfig
    return RConfig()


@pytest.fixture()
def yaml_str():
    # type: () -> str

    return """
    yek:
      ramin: 2
      mehran: 'salam'
    # comment to test
    dow:
      se:
        p1: 2.2
      f1: 'khodafez'
    """


def test_update_the_main_config(r_config, yaml_str):
    r_config.update_from_str(yaml_str)

    assert hasattr(r_config, 'yek')
