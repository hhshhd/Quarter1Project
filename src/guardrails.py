# guardrails.py
from nemoguardrails import Rails, Validator
import openai
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

openai.api_key = os.getenv("OPENAI_API_KEY")

class CustomGuardrails:
    """Class to set up and apply guardrails for API calls and responses."""
    
    def __init__(self):
        self.rails = Rails()

    def validate_input(self, user_input):
        """Validate user input using custom rules."""
        # Define custom validation logic
        if len(user_input) < 5:
            return False, "Input too short."
        return True, "Input validated."

    def apply_guardrails(self, input_text):
        """Apply guardrails and make OpenAI API call if validated."""
        is_valid, message = self.validate_input(input_text)
        if not is_valid:
            return message

        # Use OpenAI's API with guardrails
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=input_text,
            max_tokens=50
        )
        return response.choices[0].text.strip()

