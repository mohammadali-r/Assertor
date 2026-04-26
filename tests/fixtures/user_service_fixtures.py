import pytest
from client.api_client import APIClient
from config.config import load_config
from services.user_service import UserService

@pytest.fixture
def user_service():
    config = load_config()
    client = APIClient(config.base_url)
    return UserService(client)