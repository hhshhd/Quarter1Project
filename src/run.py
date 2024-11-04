import streamlit as st
from guardrails import CustomGuardrails

# Initialize the guardrails setup
guardrails = CustomGuardrails()

# Streamlit UI for the application
st.title("LLM Guardrails Demo")

# Text area for user to input prompt
user_input = st.text_area("Enter your prompt here:")

# Button to trigger response generation
if st.button("Generate Response"):
    # Generate a response with guardrails
    result = guardrails.generate_response(user_input)
    st.write("Response:", result)

    # Display guardrail explanations if needed
    st.write("Guardrail Explanations:")
    st.write(guardrails.explain())

