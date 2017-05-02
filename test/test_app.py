import pytest
from flask import url_for

class TestApp:

    def test_ping(self, client):
        res = client.get(url_for('ping'))
        assert res.status_code == 200
        assert res.json == {'ping': 'pong'}

    def test_home(self, client):
        res = client.get(url_for('index'))
        assert res.status_code == 200
