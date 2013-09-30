from setuptools import setup, find_packages
from orc import PACKAGE_NAME, VERSION


if __name__ == '__main__':
    setup(
        name=PACKAGE_NAME,
        version=VERSION,
        license='MIT',

        packages=find_packages(),

        install_requires=['tornado==3.1.1']
    )
