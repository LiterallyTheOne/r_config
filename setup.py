from setuptools import setup

setup(
    name='r_config_loader',
    version="0.2.0",
    packages=['r_config_loader'],
    author="Ramin Zarebidoky",
    author_email="ramin.zarebidoky@gmail.com",
    description="Standard way that I am using to use config",
    url="https://github.com/literallynomana/r_config_loader",
    long_description="using easydict and PyYaml to make loading config easier",
    install_requires=['pyyaml', 'easydict']
)
