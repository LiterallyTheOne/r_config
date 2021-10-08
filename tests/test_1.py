import pytest

from r_config import RConfig
from typing import Any


@pytest.fixture()
def rc():
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


def test_update_the_main_config(rc, yaml_str):
    rc.update_from_str(yaml_str)

    assert hasattr(rc, 'yek')


def test_from_dic(r_dic):
    rc = RConfig(r_dic)
    assert hasattr(rc, 'a')


def test_inner_dictionaries(r_dic):
    rc = RConfig(r_dic)
    assert isinstance(rc.f, RConfig)


def test_update_with_dictionary(rc, r_dic):
    rc.update(r_dic)
    assert hasattr(rc, 'a')
