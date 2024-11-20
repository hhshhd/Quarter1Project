import os
import openai
from nemoguardrails import RailsConfig, LLMRails
from typing import Optional

openai_api_key = "OpenAI-API-key"
os.environ["OPENAI_API_KEY"] = openai_api_key

class TranslationGuardrails:
    def __init__(self):
        self.config = RailsConfig.from_path("config.yml")
        self.rails = LLMRails(self.config)

    def translate_text(self, text: str, target_language: str, source_language: Optional[str] = None) -> str:
        if source_language:
            prompt = f"Translate the following text from {source_language} to {target_language}: {text}"
        else:
            prompt = f"Translate the following text to {target_language}: {text}"
        
        response = self.rails.generate(messages=[{
            "role": "user",
            "content": prompt
        }])
        return response["content"]

    def generate_response(self, prompt: str) -> str:
        response = self.rails.generate(messages=[{
            "role": "user",
            "content": prompt
        }])
        return response["content"]

    def explain(self) -> dict:
        info = self.rails.explain()
        return info.colang_history
