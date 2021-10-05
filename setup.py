from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='r_config_loader',
    version="0.2.2",
    packages=['r_config_loader'],
    author="Ramin Zarebidoky",
    author_email="ramin.zarebidoky@gmail.com",
    description="Standard way that I am using to use config",
    url="https://github.com/literallynomana/r_config_loader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=['pyyaml', 'easydict']
)
