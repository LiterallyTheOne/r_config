import pytest

from r_config import RConfig
from typing import Any


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


@pytest.fixture()
def r_dic():
    # type: () -> dict[str,Any]

    return {'a': 10, 'b': 'salam', 'f': {'p': 2, 'q': 3}}


def test_update_the_main_config(r_config, yaml_str):
    r_config.update_from_str(yaml_str)

    assert hasattr(r_config, 'yek')


def test_from_dic(r_dic):
    r = RConfig(r_dic)
    assert hasattr(r, 'a')


def test_inner_dictionaries(r_dic):
    r = RConfig(r_dic)
    assert isinstance(r.f, RConfig)
