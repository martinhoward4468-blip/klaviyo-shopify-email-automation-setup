import requests
from .logger import logger

def make_request(method, url, headers=None, data=None):
 try:
 response = requests.request(method, url, headers=headers, json=data, timeout=10)
 response.raise_for_status()
 return response.json()
 except Exception as e:
 logger.error(f"API request failed: {e}")
 raise