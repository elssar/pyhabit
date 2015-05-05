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

    def create_tag(self, name, tag_id=None):
        """
        Create new tag with optional unique id.
        It's generally best to leave the tag id blank and
        let it be automatically generated.

        :param name: name of new tag
        :type name: str or unicode
        :param tag_id: optional tag id
        :type tag_id: str or unicode

        usage: HabitAPI.create_tag('my awesome tag')
        """

        data = {
            'name': name,
        }
        if tag_id:
            data['id'] = tag_id

        results = self.request("post", "user/tags/", data=data)

        try:
            return results.json()
        except ValueError as e:
            return results

    def edit_tag(self, tag_id, name):
        """
        Edit tag name.

        :param name: new name of tag
        :type name: str or unicode
        :param tag_id: id of tag to edit
        :type tag_id: str or unicode

        usage:
        HabitAPI.edit_tag(
            '5632e96f-a086-4fc7-abc1-f88a878f68a7',
            'my better tag'
        )
        """

        data = {
            'name': name,
        }

        return self.request("put", "user/tags/%s" % tag_id, data=data).json()

    def delete_tag(self, tag_id):
        """
        Delete tag.

        :param tag_id: id of tag to delete
        :type tag_id: str or unicode

        usage: HabitAPI.delete_tag('5632e96f-a086-4fc7-abc1-f88a878f68a7')
        """

        return self.request("delete", "user/tags/%s" % tag_id).json()
