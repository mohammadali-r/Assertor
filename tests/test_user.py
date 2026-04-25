from client.api_client import APIClient
from config.config import load_config
from services.user_service import UserService

def test_get_users():
    config = load_config()

    client = APIClient(config.base_url)
    service = UserService(client)

    user_ids, status = service.get_users()

    assert status == 200
    assert len(user_ids) == 10