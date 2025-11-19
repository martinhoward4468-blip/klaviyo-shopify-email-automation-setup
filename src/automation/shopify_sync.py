import requests
from .utils.logger import logger
from .utils.config_loader import credentials

class ShopifySync:
 def __init__(self):
 self.url = credentials.get("SHOPIFY_STORE_URL")
 self.api_key = credentials.get("SHOPIFY_API_KEY")
 self.password = credentials.get("SHOPIFY_PASSWORD")

 def sync_data(self):
 logger.info("Syncing Shopify data...")
 endpoint = f"https://{self.api_key}:{self.password}@{self.url}/admin/api/2023-07/customers.json"

 response = requests.get(endpoint)

 if response.status_code != 200:
 logger.error("Shopify sync failed.")
 raise ValueError("Failed to sync Shopify data.")

 clean = response.json().get("customers", [])
 logger.info(f"Synced {len(clean)} customers.")
 return clean