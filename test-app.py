"""
Test cases for the Flask application
"""
import json
import pytest
from crucible import create_app

@pytest.fixture
def app():
    """Create and configure a Flask app for testing"""
    app = create_app("testing")
    return app

@pytest.fixture
def client(app):
    """A test client for the app"""
    return app.test_client()

def test_index_route(client):
    """Test the index route"""
    response = client.get('/')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['status'] == 'success'
    assert data['message'] == 'Crucible API running'

def test_health_route(client):
    """Test the health check route"""
    response = client.get('/health')
    data = json.loads(response.data)
    
    assert response.status_code == 200
    assert data['status'] == 'healthy'