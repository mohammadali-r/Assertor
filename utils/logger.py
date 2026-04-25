# from client.api_client import APIClient
from loguru import logger

logger.add("logs/test.log", rotation="1 MB")
# logger.info(f"GET {APIClient.url}")
# logger.info(f"Response: {response.status_code}")