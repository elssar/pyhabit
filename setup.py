from setuptools import setup, find_packages

setup(
    name = "pyhabit",
    description = "CLI and library to interact with HabitRPG",
    version = "0.3a",
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
            'habit = pyhabit.cli:main'
        ]
    },
    url = "http://github.com/xeross/pyhabit",
    download_url = "https://github.com/xeross/pyhabit/tarball/master"
)
