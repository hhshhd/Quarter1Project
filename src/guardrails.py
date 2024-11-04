import os
import openai
from nemoguardrails import RailsConfig, LLMRails

openai_api_key = "OpenAI-API-key"
os.environ["OPENAI_API_KEY"] = openai_api_key

class CustomGuardrails:
    def __init__(self):
        # Initialize NeMo Guardrails with the configuration
        self.config = RailsConfig.from_path("config.yml")
        self.rails = LLMRails(self.config)

    def generate_response(self, prompt):
        # Use guardrails to process and generate a response
        response = self.rails.generate(messages=[{
            "role": "user",
            "content": prompt
        }])
        return response["content"]

    def explain(self):
        # Return the detailed guardrail application history
        info = self.rails.explain()
        return info.colang_history
