import streamlit as st
from utils import render_step_progress




st.set_page_config("LLM Output", layout="wide")
st.title("2️⃣ LLM Selection and Output Display")
render_step_progress(current_step=2)
st.info("This page will be used to select a Large Language Model and display generated course content or analytics.")
