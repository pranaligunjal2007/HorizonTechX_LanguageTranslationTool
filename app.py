
import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="AI Language Translation Tool",
    page_icon="🌐",
    layout="centered"
)

# Title
st.title("🌐 AI Language Translation Tool")
st.write("Translate text between multiple languages using an NLP translation API.")

# Supported languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Kannada": "kn",
    "French": "fr",
    "German": "de",
    "Spanish": "es"
}

# Language selection
col1, col2 = st.columns(2)

with col1:
    source_language = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_language = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=2
    )

# Text input
text = st.text_area(
    "Enter text to translate:",
    height=150,
    placeholder="Type your text here..."
)

# Translation function
def translate_text(text, source, target):
    url = "https://api.mymemory.translated.net/get"

    params = {
        "q": text,
        "langpair": f"{source}|{target}"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()
    return data["responseData"]["translatedText"]


# Translate button
if st.button("🔄 Translate", use_container_width=True):

    if not text.strip():
        st.warning("⚠️ Please enter some text first.")

    elif source_language == target_language:
        st.info("Please select two different languages.")

    else:
        try:
            with st.spinner("Translating..."):
                translated = translate_text(
                    text,
                    languages[source_language],
                    languages[target_language]
                )

            st.success("Translation completed!")

            st.subheader("Translated Text")
            st.text_area(
                "Output",
                translated,
                height=150
            )

            st.caption("Translation powered by MyMemory Translation API.")

        except requests.exceptions.RequestException:
            st.error(
                "❌ Unable to connect to the translation service. "
                "Please try again."
            )

        except Exception:
            st.error(
                "❌ Something went wrong. Please check your input "
                "and try again."
            )

# Footer
st.divider()
st.caption("Horizon TechX | AI + NLP Language Translation Tool")
