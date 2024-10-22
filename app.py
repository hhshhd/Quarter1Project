import streamlit as st

def main():
    st.title("Guardrails Implementation in LLMs")

    text_area = st.text_area("Enter your text that you want to translate!")

    if st.button("Translate"):
        if len(text_area) > 0:
            st.info(text_area)

if __name__ == "__main__":
    main()
