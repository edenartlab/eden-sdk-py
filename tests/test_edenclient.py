# test_edenclient.py
from typing import List

import pytest
from eden_sdk.EdenClient import EdenClient


@pytest.fixture
def eden():
    return EdenClient(
        api_url="http://localhost:5050",
        api_key="admin",
        api_secret="admin",
    )


def test_api_keys_list(eden):
    response = eden.api_keys.list()
    assert "docs" in response, "The response should contain 'docs'"
    docs = response["docs"]
    assert isinstance(docs, list), "The response should be a list"


def test_api_keys_create(eden):
    response = eden.api_keys.create(note="Test API Key")
    assert isinstance(response, dict), "The response should be a dict"
    assert "apiKey" in response, "The response should contain 'apiKey'"
    apiKey = response["apiKey"]
    assert "apiKey" in apiKey, "The response should contain 'apiKey'"
    assert "apiSecret" in apiKey, "The response should contain 'apiSecret'"


def test_api_keys_delete(eden):
    create_response = eden.api_keys.create(note="Test API Key")
    delete_response = eden.api_keys.delete(create_response["apiKey"]["apiKey"])
    assert delete_response == {}, "The response should be empty dict"


def test_tasks_create(eden):
    response = eden.tasks.create(generator_name="test")
    assert isinstance(response, dict), "The response should be a dict"
    assert "taskId" in response, "The response should contain 'taskId'"


def test_tasks_cost(eden):
    response = eden.tasks.cost(generator_name="test")
    assert isinstance(response, dict), "The response should be a dict"
    assert "cost" in response, "The response should contain 'cost'"


def test_tasks_get(eden):
    create_response = eden.tasks.create(generator_name="test")
    get_response = eden.tasks.get(create_response["taskId"])
    assert isinstance(get_response, dict), "The response should be a dict"
    assert "task" in get_response, "The response should contain 'task'"


def test_tasks_list(eden):
    response = eden.tasks.list()
    assert "docs" in response, "The response should contain 'docs'"
    docs = response["docs"]
    assert isinstance(docs, list), "The response should be a list"


def test_create(eden):
    response = eden.create(
        generator_name="test",
    )
    print(response)
    assert isinstance(response, List), "The response should be a list"
    assert isinstance(response[0], str), "The response should be a list of strings"
