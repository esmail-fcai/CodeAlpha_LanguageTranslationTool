import streamlit as st
from deep_translator import GoogleTranslator

# Page Configuration
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Languages Dictionary
languages = {
    "English": "en",
    "Arabic": "ar",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Italian": "it",
    "Turkish": "tr",
    "Russian": "ru"
}

# Title
st.title("🌍 Language Translation Tool")
st.write("Translate text between multiple languages instantly.")

# Text Input
text = st.text_area(
    "Enter Text",
    placeholder="Type your text here...",
    height=150
)

# Word Counter
st.caption(f"📝 Word Count: {len(text.split())}")

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

# Translate Button
if st.button("🌐 Translate"):

    if not text.strip():
        st.warning("Please enter some text first.")
        st.stop()

    if source_lang == target_lang:
        st.error("Source and Target languages cannot be the same.")
        st.stop()

    try:
        translated = GoogleTranslator(
            source=languages[source_lang],
            target=languages[target_lang]
        ).translate(text)

        st.subheader("✅ Translated Text")

        st.success(translated)

        st.code(translated)

    except Exception as e:
        st.error(f"Translation Error: {e}")

# Footer
st.markdown("---")
st.caption("Developed by Esmail Sabry Elbeltagy for CodeAlpha AI Internship")