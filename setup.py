from setuptools import setup, find_packages

setup(
    name = "python-habitrpg",
    description = "CLI and library to interact with HabitRPG",
    version = "0.1a",
    install_requires=[
        'distribute',
        'requests'
    ],
    packages = find_packages(),
    author = "Xeross",
    author_email = "contact@xeross.me",
    license = "MIT",
    entry_points = {
        'console_scripts': [
            'habit = habitrpg.cli:main'
        ]
    },
    url = "http://github.com/xeross/python-habitrpg",
    download_url = "https://github.com/xeross/python-habitrpg/tarball/master"
)
