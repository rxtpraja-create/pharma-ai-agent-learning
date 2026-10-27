
import streamlit as st
from google import genai

st.set_page_config(
    page_title="Pharma AI Agent",
    page_icon="💊",
    layout="centered"
)

st.title("💊 Pharma AI Agent")
st.caption("Your pharmaceutical learning assistant")

st.info(
    "Learn about GMP, QA, QMS, CAPA, deviations "
    "and pharmaceutical data integrity."
)

api_key = None

try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    st.warning(
        "The app administrator must configure "
        "the Gemini API key before using the assistant."
    )

question = st.text_area(
    "Enter your pharmaceutical question",
    placeholder="Example: Explain CAPA in simple Hinglish."
)

if st.button("Ask Pharma AI", type="primary"):
    if not question.strip():
        st.warning("Please enter a question first.")
    elif not api_key:
        st.error("Gemini API key is not configured.")
    else:
        try:
            client = genai.Client(api_key=api_key)

            with st.spinner("Preparing your answer..."):
                response = client.models.generate_content(
                    model="gemini-3.5-flash",
                    contents=(
                        "You are a pharmaceutical learning assistant. "
                        "Explain concepts in simple Hinglish when useful. "
                        "Be accurate about GMP, QA, QMS, CAPA and data "
                        "integrity. Never invent regulations or claim "
                        "to replace approved SOPs. Verify important "
                        "compliance decisions with authoritative sources.\n\n"
                        + question
                    )
                )

            st.subheader("Pharma AI Answer")
            st.markdown(response.text or "No answer was returned.")

        except Exception as e:
            st.error("The request failed. Please check the API key, "
                     "model access and usage limits.")
            st.caption(type(e).__name__)
