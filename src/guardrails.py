from nemo_toolkit import Guardrails

def setup_guardrails(config):
    """Setup guardrails using the provided configuration."""
    rails = Guardrails(config=config)
    rails.initialize()
    return rails

def apply_guardrails(input_text, guardrails):
    """Apply guardrails to input text."""
    return guardrails.process(input_text)
