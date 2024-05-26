import json

import requests
from eden_sdk.methods import Methods


class EdenClient:
    def __init__(self, api_url="https://api.eden.art", api_key=None, api_secret=None):
        super().__init__()
        self.api_url = api_url
        self.api_key = api_key
        self.api_secret = api_secret
        self.session = requests.Session()
        self.session.headers.update(
            {"X-Api-Key": self.api_key, "X-Api-Secret": self.api_secret},
        )

        self.api_keys = Methods.ApiKeys(self)
        self.characters = Methods.Characters(self)
        self.creations = Methods.Creations(self)
        self.concepts = Methods.Concepts(self)
        self.generators = Methods.Generators(self)
        self.manna = Methods.Manna(self)
        self.tasks = Methods.Tasks(self)
        self.media = Methods.Media(self)

    def api_call(self, method, url, data=None):
        response = self.session.request(method, f"{self.api_url}/{url}", json=data)
        response.raise_for_status()
        return response.json()

    def create(self, generator_name, version_id=None, config={}):
        # Submit the task and get the ID
        task = self.tasks.create(
            generator_name=generator_name,
            version_id=version_id,
            config=config,
        )
        taskId = task["taskId"]

        # Subscribe to task updates
        for event in self.subscribe(taskId):
            if event["status"] == "completed":
                return event["result"]

            if event["status"] == "failed":
                raise Exception("Error occurred while processing task")

    def subscribe(self, taskId):
        headers = {"X-Api-Key": self.api_key, "X-Api-Secret": self.api_secret}
        url = f"{self.api_url}/tasks/events?taskId={taskId}"
        response = requests.get(url, headers=headers, stream=True)
        event_data = None
        for line in response.iter_lines():
            if line:  # filter out keep-alive new lines
                line = line.decode("utf-8")
                if line.startswith("event:"):
                    event_data = line[6:].strip()  # cache the event data, strip off "event:" prefix
                elif line.startswith("data:") and event_data == 'task-update':
                    json_data = line[6:]  # strip off "data:" prefix
                    yield json.loads(json_data)
