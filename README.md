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

Contributing
------------

This repository loosely uses standard `git-flow` branch management policy/strategy. If you want to learn more on `git-flow`, refer  to [tutorial from Atlassian](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) and more details at [http://nvie.com/posts/a-successful-git-branching-model/](http://nvie.com/posts/a-successful-git-branching-model/).

 - All feature and bug fix branches should be based off of the `develop` branch.
 - Please follow the naming convention for branches - `feature/*`, and `hotfix/*` for feature and bug/hot fix branches respectively.
 - Do not directly commit to `master` and `develop` branches.
