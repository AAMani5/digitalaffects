import pytest
from flask import url_for
from digitalaffects.app import create_app
import capybara
import capybara.dsl
capybara.app = create_app()

class TestApp:

    def test_ping(self, client):
        res = client.get(url_for('ping'))
        assert res.status_code == 200
        assert res.json == {'ping': 'pong'}

    def test_home(self, client):
        res = client.get(url_for('index'))
        assert res.status_code == 200
    
    def test_search(self, client):
        capybara.dsl.page.visit('/')
        capybara.dsl.page.fill_in('userinput', value='brexit')
        capybara.dsl.page.find('[name=getmood]').click
        assert capybara.dsl.page.has_current_path('/')
        # current path should be /json
