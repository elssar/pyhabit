#!/usr/bin/env python

from pprint import pprint

import os
import sys

from api import HabitAPI

USER_ID=os.environ["HABIT_USER_ID"]
API_KEY=os.environ["HABIT_API_KEY"]

def main():
    habitAPI = HabitAPI(USER_ID, API_KEY)
    func = getattr(habitAPI, sys.argv[1])
    if callable( func ):
        pprint(func(*sys.argv[2:]))
    else:
        print "Not a HabitRPG API method"
