# methods.py
class Methods:
    def __init__(self):
        self.apiKeys = self.ApiKeys(self)
        self.tasks = self.Tasks(self)

    class ApiKeys:
        def __init__(self, client):
            self.client = client

        def list(self):
            return self.client.api_call("GET", "apikeys")

        def create(self, note=None):
            return self.client.api_call("POST", "apikeys/create", {"note": note})

        def delete(self, apiKey):
            return self.client.api_call("POST", "apikeys/delete", {"apiKey": apiKey})

    class Tasks:
        def __init__(self, client):
            self.client = client

        def create(
            self,
            generator_name,
            version_id=None,
            config={},
            metadata=None,
            webhooks=None,
        ):
            return self.client.api_call(
                "POST",
                "tasks/create",
                {
                    "generatorName": generator_name,
                    "versionId": version_id,
                    "config": config,
                    "metadata": metadata,
                    "webhooks": webhooks,
                },
            )

        def cost(
            self,
            generator_name,
            version_id=None,
            config={},
            metadata=None,
            webhooks=None,
        ):
            return self.client.api_call(
                "POST",
                "tasks/cost",
                {
                    "generatorName": generator_name,
                    "versionId": version_id,
                    "config": config,
                    "metadata": metadata,
                    "webhooks": webhooks,
                },
            )

        def get(self, task_id):
            return self.client.api_call("GET", f"tasks/{task_id}")

        def list(self, status=None, task_id=None, type=None):
            return self.client.api_call(
                "GET", "tasks", {"status": status, "taskId": task_id, "type": type}
            )


class ApiKey:
    def __init__(self, apiKey, apiSecret, note, createdAt):
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.note = note
        self.createdAt = createdAt
