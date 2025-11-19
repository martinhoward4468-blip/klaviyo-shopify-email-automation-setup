import requests
from .utils.logger import logger
from .utils.config_loader import credentials

class KlaviyoConnector:
 def __init__(self):
 self.api_key = credentials.get("KLAVIYO_API_KEY")
 self.base_url = "https://a.klaviyo.com/api"

 def validate_connection(self):
 logger.info("Validating Klaviyo connection...")
 headers = {"Authorization": f"Klaviyo-API-Key {self.api_key}"}
 url = f"{self.base_url}/accounts"
 response = requests.get(url, headers=headers)

 if response.status_code != 200:
 logger.error("Klaviyo validation failed.")
 raise ValueError("Failed to connect to Klaviyo API.")

 logger.info("Klaviyo connection validated successfully.")