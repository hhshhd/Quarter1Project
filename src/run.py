import streamlit as st
from guardrails import CustomGuardrails

# Initialize the guardrails setup
guardrails = CustomGuardrails()

st.title("LLM with Guardrails")

user_input = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    result = guardrails.generate_response(user_input)
    st.write("Response:", result)

    # Display guardrail explanations if needed
    st.write("Guardrail Explanations:")
    st.write(guardrails.explain())


