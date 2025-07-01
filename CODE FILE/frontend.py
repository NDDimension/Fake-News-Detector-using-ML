import streamlit as st
import joblib
from PIL import Image
import os

# Set page configuration
st.set_page_config(page_title="📰 Fake News Detector", layout="centered")

# Load model and vectorizer
vectorizer = joblib.load("../Models/tfidf_vectorizer.jb")
model = joblib.load("../Models/fake_news_detector.jb")

# Custom CSS styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f4f6f7;
        font-family: 'Segoe UI', sans-serif;
    }
    .stTextArea textarea {
        font-size: 16px !important;
    }
    .footer {
        text-align: center;
        padding-top: 30px;
        font-size: 14px;
        color: #888;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 10em;
        font-size: 16px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Optional: Add a header image
image = Image.open("../Img/image.png")
st.image(image, use_container_width=True)

# Title and subtitle
st.title("📰 Fake News Detector")
st.markdown("### 🔍 Instantly verify the authenticity of a news article.")
st.info(
    "Enter a news article below and click **Check News** to detect if it's Real or Fake."
)

# Input
news_input = st.text_area(
    "📝 Paste the News Article Here",
    height=200,
    placeholder="Type or paste your news article here...",
)

# Button
if st.button("Check News"):
    if news_input.strip():
        with st.spinner("Analyzing..."):
            transform_input = vectorizer.transform([news_input])
            prediction = model.predict(transform_input)

        if prediction[0] == 1:
            st.success("✅ This news appears to be **Real**.")
        else:
            st.error("⚠️ This news appears to be **Fake**.")
    else:
        st.warning("⚠️ Please enter a news article to analyze.")

# Footer
st.markdown("---")
st.markdown(
    "<div class='footer'>Made with ❤️ by <strong>DHANRAJ SHARMA</strong></div>",
    unsafe_allow_html=True,
)
