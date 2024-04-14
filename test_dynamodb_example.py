import boto3
from moto import mock_dynamodb2
from src.boto3_example import DynamodBExample
import pytest


@mock_dynamodb2
def test_create_dynamo_table():
    """
    Implement the test logic here for testing create_dynamo_table method
    """
    dynamodb_example = DynamodBExample()
    dynamodb_example.create_movies_table()

    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table("Movies")

    assert table.name == "Movies"
    assert "year" in table.key.schema[0].values()
    assert "title" in table.key.schema[1].values()


@mock_dynamodb2
def test_add_dynamo_record_table():
    """
    Implement the test logic here for testing add_dynamo_record_table method
    """
    dynamo_example = DynamodBExample()
    dynamo_example.create_movies_table()

    item = {
        "year": 2023,
        "title": "Test Movie",
        "info": {"plot": "Test Plot", "rating": 5},
    }

    dynamo_example.add_dynamo_record("Movies", item)
    dynamodb = boto3.resource("dynamodb", region_name="us-east-1")
    table = dynamodb.Table("Movies")

    response = table.get_item(Key={"year": 2023, "title": "Test Movie"})
    assert "Item" in response
    assert response["Item"] == item


@mock_dynamodb2
def test_add_dynamo_record_table_failure():
    """
    Implement the test logic here test_add_dynamo_record_table method for failures
    """
    dynamodb_example = DynamodBExample()
    dynamodb_example.create_movies_table()

    item = {
        "year": "Invalid Year",
        "title": "Test Movie",
        "info": {"plot": "Test Plot", "rating": 5},
    }

    try:
        dynamodb_example.add_dynamo_record("Movies", item)
        assert False
    except Exception as e:
        assert "Invalid year type" in str(e)
