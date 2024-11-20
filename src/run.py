import streamlit as st
from guardrails import TranslationGuardrails

# Initialize the guardrails setup
guardrails = TranslationGuardrails()

# Streamlit UI for the application
st.title("AI Translation Service")

# Create tabs for different functionalities
tab1, tab2 = st.tabs(["Translation", "General Chat"])

with tab1:
    st.header("Text Translation")
    
    # Input text area
    input_text = st.text_area("Enter text to translate:", height=150)
    
    # Language selection
    col1, col2 = st.columns(2)
    with col1:
        source_lang = st.text_input("Source Language (optional)", "")
    with col2:
        target_lang = st.text_input("Target Language (required)", "")
    
    # Translation button
    if st.button("Translate"):
        if not target_lang:
            st.error("Please specify a target language")
        elif not input_text:
            st.error("Please enter text to translate")
        else:
            with st.spinner("Translating..."):
                result = guardrails.translate_text(
                    text=input_text,
                    target_language=target_lang,
                    source_language=source_lang if source_lang else None
                )
                st.write("Translation:", result)
                
                # Display guardrail explanations in an expander
                with st.expander("View Process Details"):
                    st.write(guardrails.explain())

with tab2:
    st.header("General Chat")
    
    user_input = st.text_area("Enter your message:", height=150)
    
    if st.button("Send Message"):
        result = guardrails.generate_response(user_input)
        st.write("Response:", result)
        
        with st.expander("View Process Details"):
            st.write(guardrails.explain())
