import os
##import requests

from dotenv import load_dotenv

load_dotenv()

api=os.getenv("api_key")

print(api)