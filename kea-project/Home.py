# import streamlit as st
# from utils import render_step_progress


# # Define your pages
# page1 = st.Page("pages/1_Course_Config.py", title="1. Course Configuration & Instructor Input", icon=":material/double_arrow:")
# page2 = st.Page("pages/2_LLM_Output.py", title="2. LLM Selection and Output Display", icon=":material/double_arrow:")

# # Navigation
# pg = st.navigation([page1, page2])
# pg.run()











import streamlit as st
from utils import render_step_progress

st.set_page_config(page_title="Course Builder Home", layout="wide")
st.title("🏠 Welcome to the Hospitality Course Generator")

# Step 0 on the progress bar (Home Page)
render_step_progress(current_step=0)

st.markdown(
    """
    ### Welcome!
    Use the sidebar to navigate through each step of your course creation journey:
    
    **Step 1** – Course Configuration & Instructor Input  
    **Step 2** – Generate AI-Powered Course Content
    """
)




# import streamlit as st

# # --- Page Config ---
# st.set_page_config(page_title="Course Setup Wizard", layout="wide")

# # --- Stepper UI (Static View) ---
# st.markdown(
#     """
#     <div style='display: flex; justify-content: center; align-items: center; margin-bottom: 2rem;'>
#         <div style='padding: 12px 24px; border-radius: 25px; background-color: #4CAF50; color: white; margin-right: 10px; font-weight: bold;'>
#             1️⃣ Course Configuration
#         </div>
#         <div style='font-size: 28px; margin-right: 10px;'>➡️</div>
#         <div style='padding: 12px 24px; border-radius: 25px; background-color: #ddd; color: black; font-weight: bold;'>
#             2️⃣ LLM Output
#         </div>
#     </div>
#     """,
#     unsafe_allow_html=True,
# )

# # --- Welcome Message ---
# st.title("Welcome to the Course Setup Wizard")
# st.markdown("Use the left sidebar to begin by configuring your course. This two-step process helps you:")
# st.markdown("""
# - Set up course information and instructor input
# - Generate and view AI-assisted content using LLMs
# """)

# st.info("👉 Use the **sidebar** to select a page and begin.")

# # --- Define Pages ---
# page1 = st.Page("pages/1_Course_Config.py", title="1. Course Configuration & Instructor Input", icon=":material/double_arrow:")
# page2 = st.Page("pages/2_LLM_Output.py", title="2. LLM Selection and Output Display", icon=":material/double_arrow:")

# # --- Navigation ---
# pg = st.navigation([page1, page2])
# pg.run()