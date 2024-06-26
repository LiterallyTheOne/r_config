RConfig
=======

A customized way to use config

`Documentation <https://r-config.readthedocs.io/en/latest/>`_

`PyPi <https://pypi.org/project/r-config/>`_

Usage
-----

From string
^^^^^^^^^^^

.. code-block:: python

    from r_config import RConfig

    rc = RConfig()

    str_yaml = """
        example1:
          id: 2
          name: 'Ramin'
        # comment to test
        example2:
          sub1:
            p1: 2.2
          sub2: 'test_1'
     """

    rc.update_from_str(str_yaml)



From file
^^^^^^^^^

.. code-block:: python

    from r_config import RConfig
    from pathlib import Path

    rc = RConfig()

    path = Path('/path/to/config.yaml')

    rc.update_from_file(path)


From dict
^^^^^^^^^

.. code-block:: python

    from r_config import RConfig

    r_dict = {'a': 10, 'b': 'salam', 'f': {'p': 2, 'q': 3}}

    rc = RConfig(r_dict)
