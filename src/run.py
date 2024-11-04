import os
import streamlit as st
import openai
from dotenv import load_dotenv
from guardrails import apply_guardrails  # Import the custom guardrails

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("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")

st.title("NeMo Guardrails Implementation in LLMs")

# Text area for user input
input_text = st.text_area("Enter text to translate:")

# Button to submit input
if st.button("Translate"):
    if input_text:
        # Send input text to OpenAI for translation
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"Translate the following text to English: {input_text}",
            max_tokens=100,
            temperature=0.2
        )
        
        # Get the response text
        translated_text = response.choices[0].text.strip()
        
        # Apply guardrails to the response
        moderated_text = apply_guardrails(translated_text)
        
        # Display results with and without guardrails
        st.subheader("Translation without Guardrails:")
        st.write(translated_text)

        st.subheader("Translation with NeMo Guardrails:")
        st.write(moderated_text)
    else:
        st.warning("Please enter text to translate.")

