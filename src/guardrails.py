import os
import openai
import pandas as pd
from dotenv import load_dotenv
from nemoguardrails import RailsConfig, LLMRails

# Load environment variables from .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class CustomGuardrails:
    def __init__(self):
        # Load the configuration for guardrails
        self.config = RailsConfig.from_path("config/config.yml")
        self.rails = LLMRails(self.config)

    def generate_response(self, prompt):
        response = self.rails.generate(messages=[{
            "role": "user",
            "content": prompt
        }])
        return response["content"]

    def explain(self):
        info = self.rails.explain()
        return info.colang_history

