import streamlit as st
from generation.answer_questions import answer_questions
import base64
import os
import html

st.set_page_config(page_title="AI Ethics Research Assistant", layout="centered")

def get_base64(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return ""

def set_background(image_file):
    encoded = get_base64(image_file)
    if encoded:
        st.markdown(f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """, unsafe_allow_html=True)

set_background("background.png")

st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: "Times New Roman", Times, serif !important;
    color: black !important;
}
h1 {
    text-align: center;
    font-weight: bold;
    font-size: 42px;
    font-family: "Times New Roman", Times, serif !important;
    color: black !important;
}
.block-container {
    background: transparent !important;
    padding-top: 2rem;
}
.stTextInput input {
    border-radius: 8px;
    padding: 10px;
    border: 1px solid #333;
    background-color: black;
    color: white;
    font-family: "Times New Roman", Times, serif !important;
}
.stButton button {
    border-radius: 8px;
    background-color: #2A2F45;
    color: white;
    border: none;
    padding: 10px 16px;
    font-family: "Times New Roman", Times, serif !important;
}
[data-testid="stCaptionContainer"] p {
    color: black !important;
    font-family: "Times New Roman", Times, serif !important;
    text-align: center !important;
}
label[data-testid="stWidgetLabel"] p {
    color: black !important;
    font-family: "Times New Roman", Times, serif !important;
    text-align: center !important;
}
.stTextInput {
    max-width: 500px;
    margin: 0 auto !important;
}
.stButton {
    display: flex !important;
    justify-content: center !important;
}
.stButton button:hover {
    background-color: #4a5568 !important;
    color: white !important;
}          
[data-testid="stAlert"] {
    background-color: #2A2F45 !important;
    color: white !important;
    font-family: "Times New Roman", Times, serif !important;
    border: none !important;
    border-radius: 8px !important;
    text-align: center !important;
    max-width: 500px !important;
}
[data-testid="stAlert"] p {
    color: white !important;
    font-family: "Times New Roman", Times, serif !important;
}          
</style>
""", unsafe_allow_html=True)

st.title("AI Ethics Research Assistant")
st.markdown("""
<p style="
    text-align: center;
    font-family: 'Times New Roman', serif;
    color: black;
    font-size: 18px;
    margin-top: -15px;
">Retrieval-Augmented System for AI Ethics Research with Citations</p>
""", unsafe_allow_html=True)

query = st.text_input("Enter your question-")

if st.button("Seek knowledge"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Processing..."):
            answer, docs = answer_questions(query)

        # DO NOT escape answer — render HTML as-is
        scroll_base64 = get_base64("scroll.png")

        sources_html = ""
        for i, doc in enumerate(docs):
            meta = doc.metadata
            author = meta.get('author', 'Unknown')
            year = meta.get('year', 'N.A.')
            title = meta.get('title', 'Unknown')
            domain = meta.get('domain', 'N.A.')
            sources_html += "[{}] {} ({}). <em>{}</em>. {}.<br>".format(i+1, author, year, title, domain)

        st.markdown(f"""
        <div style="position: relative; width: 700px; margin: 0 auto;">
            <img src="data:image/png;base64,{scroll_base64}"
                 style="width: 100%; display: block;" />
            <div style="
                position: absolute;
                top: 16%;
                left: 21%;
                width: 61%;
                height: 70%;
                overflow-y: auto;
                font-family: 'Times New Roman', serif;
                color: black;
                font-size: 15px;
                line-height: 1.6;
            ">
                {answer}
            </div>
        </div>
        <div style="
            margin-top: 30px;
            font-family: 'Times New Roman', serif;
            color: black;
            font-size: 15px;
            line-height: 2;
        ">
            <b style="font-size: 18px;">Sources</b><br>
            {sources_html}
        </div>
        """, unsafe_allow_html=True)
