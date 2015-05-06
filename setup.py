from setuptools import setup, find_packages

setup(
    name = "pyhabit",
    description = "CLI and library to interact with HabitRPG",
    version = "0.3.0-alpha",
    install_requires=[
        'distribute',
        'requests'
    ],
    packages = find_packages(),
    author = "elssar",
    author_email = "elssar@altrawcode.com",
    license = "MIT",
    entry_points = {
        'console_scripts': [
            'habit = pyhabit.cli:main'
        ]
    },
    url = "https://github.com/elssar/pyhabit",
    download_url = "https://github.com/elssar/pyhabit/tarball/master"
)
