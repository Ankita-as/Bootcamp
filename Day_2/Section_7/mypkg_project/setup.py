from setuptools import setup, find_packages

from setuptools import setup, find_packages

setup(
    name='helloworld',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'typer',
    ],
    entry_points={
        'console_scripts': [
            'many-hellos=helloworld.main:app',
        ],
    },
)
