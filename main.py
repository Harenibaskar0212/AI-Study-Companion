import streamlit as st
from modules import planner, flashcards, dashboard, mood_motivation
from PIL import Image
import os

st.set_page_config(page_title="AI Study Companion", layout="centered")

# Load CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/style.css")

# Display logo in sidebar
logo_path = os.path.join("assets", "logo.jpg")
if os.path.exists(logo_path):
    logo = Image.open(logo_path)
    st.sidebar.image(logo, width=150)

# Styled title (you can remove st.title below if you want header only in sidebar)
st.markdown('<h1 style="color:#0d6efd; font-family:\'Segoe UI\', Tahoma, Geneva, Verdana, sans-serif;">📚 AI Study Companion</h1>', unsafe_allow_html=True)
st.sidebar.markdown(
    '<h2 style="color:#0d6efd; font-family:\'Segoe UI\', Tahoma, Geneva, Verdana, sans-serif;">Menu</h2>', unsafe_allow_html=True)

# Sidebar Menu
menu = st.sidebar.radio(
    "Navigate to",
    ["📅 Study Planner", "🧠 Notes to Flashcards", "📊 Performance Dashboard", "😊 Mood & Motivation", "ℹ️ About / Help"]
)

# Routing tabs to respective modules
if menu == "📅 Study Planner":
    planner.show()

elif menu == "🧠 Notes to Flashcards":
    flashcards.show()

elif menu == "📊 Performance Dashboard":
    dashboard.show()

elif menu == "😊 Mood & Motivation":
    mood_motivation.show()

elif menu == "ℹ️ About / Help":
    import modules.about_help as about_help
    about_help.show()
