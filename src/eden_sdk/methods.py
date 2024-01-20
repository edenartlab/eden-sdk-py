class Methods:
    def __init__(self):
        self.apiKeys = self.ApiKeys(self)
        self.characters = self.Characters(self)
        self.creations = self.Creations(self)
        self.concepts = self.Concepts(self)
        self.generators = self.Generators(self)
        self.manna = self.Manna(self)
        self.tasks = self.Tasks(self)

    class ApiKeys:
        def __init__(self, client):
            self.client = client

        def list(self, page=None, limit=None, sort=None):
            return self.client.api_call(
                "GET", "apikeys", {"page": page, "limit": limit, "sort": sort}
            )

        def create(self, note=None):
            return self.client.api_call("POST", "apikeys/create", {"note": note})

        def delete(self, apiKey):
            return self.client.api_call("POST", "apikeys/delete", {"apiKey": apiKey})

    class Characters:
        def __init__(self, client):
            self.client = client

        def list(self, user_id=None, page=None, limit=None, sort=None):
            return self.client.api_call(
                "GET",
                "characters",
                {
                    "userId": user_id,
                    "page": page,
                    "limit": limit,
                    "sort": sort,
                },
            )

        def get(self, character_id):
            return self.client.api_call("GET", f"characters/{character_id}")

        def create(
            self,
            name,
            image=None,
            voice=None,
            greeting=None,
            dialogue=None,
            logos_data=None,
            is_private=None,
        ):
            return self.client.api_call(
                "POST",
                "characters",
                {
                    "name": name,
                    "image": image,
                    "voice": voice,
                    "greeting": greeting,
                    "dialogue": dialogue,
                    "logosData": logos_data,
                    "isPrivate": is_private,
                },
            )

        def update(
            self,
            character_id,
            name=None,
            image=None,
            voice=None,
            greeting=None,
            dialogue=None,
            logos_data=None,
            is_private=None,
        ):
            return self.client.api_call(
                "PATCH",
                f"characters/{character_id}",
                {
                    "name": name,
                    "image": image,
                    "voice": voice,
                    "greeting": greeting,
                    "dialogue": dialogue,
                    "logosData": logos_data,
                    "isPrivate": is_private,
                },
            )

        def delete(self, character_id):
            return self.client.api_call(
                "POST", "characters/delete", {"characterId": character_id}
            )

        def test(
            self,
            name,
            identity,
            message,
            knowledge=None,
            knowledge_summary=None,
            attachments=None,
        ):
            return self.client.api_call(
                "POST",
                "characters/test",
                {
                    "name": name,
                    "identity": identity,
                    "message": message,
                    "knowledge": knowledge,
                    "knowledge_summary": knowledge_summary,
                    "attachments": attachments,
                },
            )

        def interact(self, session_id, character_id, message, attachments=None):
            return self.client.api_call(
                "POST",
                "characters/interact",
                {
                    "sessionId": session_id,
                    "characterId": character_id,
                    "message": message,
                    "attachments": attachments,
                },
            )

    class Generators:
        def __init__(self, client):
            self.client = client

        def list(self, page=None, limit=None, sort=None):
            return self.client.api_call(
                "GET", "generators", {"page": page, "limit": limit, "sort": sort}
            )

        def get(self, generator_name):
            return self.client.api_call("GET", f"generators/{generator_name}")

    class Manna:
        def __init__(self, client):
            self.client = client
            self.vouchers = self.Vouchers(client)

        def balance(self):
            return self.client.api_call("GET", "manna/balance")

        class Vouchers:
            def __init__(self, client):
                self.client = client

        def redeem(self, code):
            return self.client.api_call("POST", "manna/vouchers/redeem", {"code": code})

    class Creations:
        def __init__(self, client):
            self.client = client
            self.reactions = self.Reactions(client)

        def list(self, user_id=None, name=None, page=None, limit=None, sort=None):
            return self.client.api_call(
                "GET",
                "creations",
                {
                    "userId": user_id,
                    "name": name,
                    "page": page,
                    "limit": limit,
                    "sort": sort,
                },
            )

        def get(self, creation_id):
            return self.client.api_call("GET", f"creations/{creation_id}")

        def update(self, creation_id, is_private):
            return self.client.api_call(
                "PATCH", f"creations/{creation_id}", {"isPrivate": is_private}
            )

        def delete(self, creation_id):
            return self.client.api_call("DELETE", f"creations/{creation_id}")

        class Reactions:
            def __init__(self, client):
                self.client = client

            def add(self, creation_id, reaction):
                return self.client.api_call(
                    "POST",
                    "creations/reactions/add",
                    {"creationId": creation_id, "reaction": reaction},
                )

            def remove(self, creation_id, reaction):
                return self.client.api_call(
                    "POST",
                    "creations/reactions/remove",
                    {"creationId": creation_id, "reaction": reaction},
                )

    class Concepts:
        def __init__(self, client):
            self.client = client
            self.reactions = self.Reactions(client)

        def list(self, user_id=None, name=None, page=None, limit=None, sort=None):
            return self.client.api_call(
                "GET",
                "concepts",
                {
                    "userId": user_id,
                    "name": name,
                    "page": page,
                    "limit": limit,
                    "sort": sort,
                },
            )

        def get(self, concept_id):
            return self.client.api_call("GET", f"concepts/{concept_id}")

        def update(self, concept_id, is_private):
            return self.client.api_call(
                "PATCH", f"concepts/{concept_id}", {"isPrivate": is_private}
            )

        def delete(self, concept_id):
            return self.client.api_call("DELETE", f"concepts/{concept_id}")

        class Reactions:
            def __init__(self, client):
                self.client = client

            def add(self, concept_id, reaction):
                return self.client.api_call(
                    "POST",
                    "concepts/reactions/add",
                    {"conceptId": concept_id, "reaction": reaction},
                )

            def remove(self, concept_id, reaction):
                return self.client.api_call(
                    "POST",
                    "concepts/reactions/remove",
                    {"conceptId": concept_id, "reaction": reaction},
                )

    class Tasks:
        def __init__(self, client):
            self.client = client

        def create(
            self,
            generator_name,
            version_id=None,
            config={},
            metadata=None,
        ):
            return self.client.api_call(
                "POST",
                "tasks/create",
                {
                    "generatorName": generator_name,
                    "versionId": version_id,
                    "config": config,
                    "metadata": metadata,
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

        def list(
            self, status=None, task_id=None, type=None, page=None, limit=None, sort=None
        ):
            return self.client.api_call(
                "GET",
                "tasks",
                {
                    "status": status,
                    "taskId": task_id,
                    "type": type,
                    "page": page,
                    "limit": limit,
                    "sort": sort,
                },
            )


class ApiKey:
    def __init__(self, apiKey, apiSecret, note, createdAt):
        self.apiKey = apiKey
        self.apiSecret = apiSecret
        self.note = note
        self.createdAt = createdAt
