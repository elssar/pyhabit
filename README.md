pyhabit
===============

HabitRPG python library (WIP)

Uses the env variables HABIT_USER_ID and HABIT_API_KEY for authentication

Installation
------------

Install using pip

    pip install git+git://github.com/elssar/pyhabit

Requires
--------

* requests

Usage
-----

Set your env vars for the API

call it from command line using 

    habit <method> <arg1> <arg2> <...>

OR

    from habitrpg import HabitAPI

    api = HabitAPI(<user_id>, <api_key>)
    api.user()
    ... # etc.

Todo
----

* Improve command line with proper help and commands
* Add command line init command and possible .habitrc
