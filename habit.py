#!/usr/bin/env python

from pprint import pprint

import requests
import json
import os
import sys

DIRECTION_UP = "up"
DIRECTION_DOWN = "down"

TYPE_HABIT = "habit"
TYPE_DAILY = "daily"
TYPE_TODO = "todo"
TYPE_REWARD = "reward"

USER_ID=os.environ["HABIT_USER_ID"]
API_KEY=os.environ["HABIT_API_KEY"]
API_URL="https://habitrpg.com/api/v1/"

AUTH_HEADERS = {
    'x-api-user': USER_ID,
    'x-api-key': API_KEY
}

def user():
    r = requests.get(API_URL + "user", headers=AUTH_HEADERS)
    return r.json()

def tasks():
    r = requests.get(API_URL + "user/tasks", headers=AUTH_HEADERS)
    return r.json()

def task(task_id):
    r = requests.get(API_URL + "user/task/%s" % task_id, headers=AUTH_HEADERS)
    return r.json()

def create_task(task_type, text, completed = False, value = 0, note = ""):
    data = {
        'type': task_type,
        'text': text,
        'completed': completed,
        'value': value,
        'note': note
    }

    r = requests.post(API_URL + "user/task/%s" % task_id, data=data, headers=AUTH_HEADERS)
    return r.json()

def update_task(task_id, text):
    r = requests.put(API_URL + "user/task/%s" % task_id, data=text, headers=AUTH_HEADERS)
    return r.json()

def perform_task(task_id, direction):
    print API_URL[:-7] + "v1/users/%s/tasks/%s/%s" % (USER_ID, task_id, direction)
    r = requests.post(API_URL[:-7] + "v1/users/%s/tasks/%s/%s" % (USER_ID, task_id, direction), data=json.dumps({'apiToken': API_KEY}), headers={'Content-Type': 'application/json'})
    return r.text

if __name__ == "__main__":
    func = locals()[sys.argv[1]]
    if callable( func ):
        pprint(func(*sys.argv[2:]))
