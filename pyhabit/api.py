import requests
import json

class HabitAPI(object):
    DIRECTION_UP = "up"
    DIRECTION_DOWN = "down"

    TYPE_HABIT = "habit"
    TYPE_DAILY = "daily"
    TYPE_TODO = "todo"
    TYPE_REWARD = "reward"

    def __init__(self, user_id, api_key, base_url = "https://habitrpg.com/"):
        self.user_id = user_id
        self.api_key = api_key
        self.base_url = base_url

    def auth_headers(self):
        return {
            'x-api-user': self.user_id,
            'x-api-key': self.api_key
        }

    def request(self, method, path, *args, **kwargs):
        path = "%s/%s" % ("api/v2", path) if not path.startswith("/") else path[1:]

        if not "headers" in kwargs:
            kwargs["headers"] = self.auth_headers()

        return getattr(requests, method)(self.base_url + path, *args, **kwargs)

    def user(self):
        return self.request("get", "user").json()

    def tasks(self):
        return self.request("get", "user/tasks").json()

    def task(self, task_id):
        return self.request("get", "user/tasks/%s" % task_id).json()

    def create_task(self, task_type, text, completed = False, value = 0, note = ""):
        data = {
            'type': task_type,
            'text': text,
            'completed': "true" if completed else "false",
            'value': value,
            'note': note
        }

        return self.request("post", "user/tasks/", data=data).json()

    def update_task(self, task_id, text):
        return self.request("put", "user/tasks/%s" % task_id, data=text).json()

    def perform_task(self, task_id, direction):
        return self.request("post", "user/tasks/%s/%s" % (task_id, direction)).json()
