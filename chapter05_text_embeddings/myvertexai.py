from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials

api_key_path = "/Users/danniel.kil/Downloads/khlee-demo-8af60a965548.json"

credentials = Credentials.from_service_account_file(
    api_key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"]
)

PROJECT_ID = "khlee-demo"
REGION = "us-central1"
# REGION = "global"

import vertexai

vertexai.init(project=PROJECT_ID, location=REGION, credentials=credentials)