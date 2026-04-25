from dataclasses import dataclass
from models.user_model import User
from client.api_client import APIClient


@dataclass
class UserService:
    client: APIClient

    # class UserService:
    #     def __init__(self, client):
    #         self.client = client

    def get_users(self):
        response = self.client.get(f"/users")
        data = response.json()

        # users = User(**data)  # validation happens here
        user_ids = []
        for item in data["users"]:
            user_ids.append(item["userId"])
            

        return user_ids, response.status_code
