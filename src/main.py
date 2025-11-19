from fastapi import FastAPI, HTTPException
from automation.klaviyo_connector import KlaviyoConnector
from automation.shopify_sync import ShopifySync
from automation.segmentation_builder import SegmentationBuilder
from automation.email_templates import EmailTemplateBuilder
from automation.utils.logger import logger
from automation.utils.config_loader import load_settings, load_credentials

app = FastAPI(title="Klaviyo–Shopify Email Automation Setup")

@app.on_event("startup")
def startup_event():
 logger.info("Loading configuration...")
 load_settings()
 load_credentials()

@app.post("/run-setup")
def run_setup():
 try:
 logger.info("Starting automation setup...")

 klaviyo = KlaviyoConnector()
 shopify = ShopifySync()
 segmentation = SegmentationBuilder()
 templates = EmailTemplateBuilder()

 klaviyo.validate_connection()
 data = shopify.sync_data()
 segments = segmentation.build_segments(data)
 templates.generate_template()

 return {"status": "success", "segments_created": len(segments)}
 except Exception as e:
 logger.exception("Setup failed.")
 raise HTTPException(status_code=500, detail=str(e))