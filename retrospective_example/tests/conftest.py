import sys
sys.path.append("..")
import pytest
from flask import Flask, jsonify, request
from retrospective_example.app import app

@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def runner():
    return app.test_cli_runner()