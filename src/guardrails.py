from nemo_toolkit import guardrails
from alt_profanity_check import predict
from openai import openai

# Profanity check function to use with NeMo guardrails
def check_profanity(text):
    """Check for profanity using the alt_profanity_check library."""
    return predict(text) == 1

def apply_guardrails(response_text):
    """Apply NeMo guardrails to the response text."""
    if check_profanity(response_text):
        return "Sorry, this response contains inappropriate language and cannot be displayed."
    return response_text

