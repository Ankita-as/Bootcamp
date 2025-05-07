from setuptools import setup, find_packages

setup(
    name="ankita_hello_cli",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "typer",
        "rich",
    ],
    entry_points={
        "console_scripts": [
            "ankita-hello = ankita_hello_cli.main:app",
        ],
    },
)
