import json
from pathlib import Path
from .utils.logger import logger

class SegmentationBuilder:
 def build_segments(self, customers):
 logger.info("Building segments...")

 segments = {
 "engaged": [c for c in customers if c.get("last_order_id")],
 "unengaged": [c for c in customers if not c.get("last_order_id")],
 "new_subscribers": [c for c in customers if c.get("state") == "enabled"],
 }

 Path("output").mkdir(exist_ok=True)
 with open("output/segments.json", "w") as f:
 json.dump(segments, f, indent=2)

 logger.info("Segments saved.")
 return segments