# import streamlit as st
# from typing import Literal

# def render_step_progress(current_step: int):
#     steps = [
#         "Home",
#         "Course Configuration",
#         "LLM Output"
#     ]

#     progress_bar = ""
#     for i, step in enumerate(steps):
#         if i < current_step:
#             progress_bar += f"✅ {step} &nbsp;→&nbsp; "
#         elif i == current_step:
#             progress_bar += f"🟦 {step} &nbsp;→&nbsp; "
#         else:
#             progress_bar += f"⬜ {step} &nbsp;→&nbsp; "

#     # Remove trailing arrow
#     if progress_bar.endswith("&nbsp;→&nbsp; "):
#         progress_bar = progress_bar[:-18]

#     st.markdown(f"""
# <div style="padding: 1rem; background-color: #999999; border-radius: 0.5rem; font-size: 1.1rem;">
#     {progress_bar}
# </div>
# """, unsafe_allow_html=True)

import streamlit as st

def render_step_progress(current_step: int):
    steps = [
        ("Home", "/"),
        ("Course Configuration", "/Course_Config"),
        ("LLM Output", "/LLM_Output")
    ]

    progress_bar = ""
    for i, (label, link) in enumerate(steps):
        if i < current_step:
            progress_bar += f"<a href='{link}' target='_self'  style='text-decoration: none;'>✅ {label}</a> &nbsp;→&nbsp; "
        elif i == current_step:
            progress_bar += f"<a href='{link}' target='_self'  style='text-decoration: none;'><strong>🟦 {label}</strong></a> &nbsp;→&nbsp; "
        else:
            progress_bar += f"<a href='{link}' target='_self'  style='text-decoration: none;'>⬜ {label}</a> &nbsp;→&nbsp; "

    # Remove trailing arrow
    if progress_bar.endswith("&nbsp;→&nbsp; "):
        progress_bar = progress_bar[:-18]

    st.markdown(f"""
<div style="padding: 1rem; background-color: #666666; border-radius: 0.5rem; font-size: 1.1rem;">
    {progress_bar}
</div>
""", unsafe_allow_html=True)
