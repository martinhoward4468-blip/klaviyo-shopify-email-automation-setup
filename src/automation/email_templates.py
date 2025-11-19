from pathlib import Path
from jinja2 import Environment, BaseLoader
from .utils.logger import logger

class EmailTemplateBuilder:
 def generate_template(self):
 logger.info("Generating email template...")

 template = """

 Welcome to {{ brand }}

 We're excited to have you with us.

 """

 env = Environment(loader=BaseLoader())
 compiled = env.from_string(template).render(brand="Your Brand")

 Path("output").mkdir(exist_ok=True)
 with open("output/template_preview.html", "w") as f:
 f.write(compiled)

 logger.info("Template generated successfully.")