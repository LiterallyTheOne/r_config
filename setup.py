from setuptools import setup

setup(
    name='r_config_loader',
    version="0.2.0",
    packages=['r_config_loader'],
    author="Ramin Zarebidoky",
    author_email="mystery.ramin@gmail.com",
    description="using easydict and Yaml to make loading and using config easier",
    url="https://github.com/literallynomana/r_config_loader",
    long_description="using easydict and PyYaml to make loading config easier",
    install_requires=['pyyaml', 'easydict']
)
