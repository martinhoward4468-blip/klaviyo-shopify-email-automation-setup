import yaml
import os
from dotenv import load_dotenv

settings = {}
credentials = {}

def load_settings():
 global settings
 with open("config/settings.yaml") as f:
 settings = yaml.safe_load(f)
 return settings

def load_credentials():
 global credentials
 load_dotenv("config/credentials.env")
 credentials = {
 "KLAVIYO_API_KEY": os.getenv("KLAVIYO_API_KEY"),
 "SHOPIFY_STORE_URL": os.getenv("SHOPIFY_STORE_URL"),
 "SHOPIFY_API_KEY": os.getenv("SHOPIFY_API_KEY"),
 "SHOPIFY_PASSWORD": os.getenv("SHOPIFY_PASSWORD"),
 }
 return credentials