import streamlit as st
import random

# Data for spinner
categories = [
    "Conflict of Interest in Hiring",
    "Falsifying Work Hours",
    "Withholding Credit for Ideas",
    "Exaggerating Sales Numbers",
    "Skipping Safety Rules",
    "Handling Burnout",
    "Overhearing Layoffs",
    "Conflict Between Team Members",
    "Handling Performance Issues",
    "Ethical Discounts"
]

st.title("Interactive Spinner")
st.write("Click the button to spin the wheel!")

if st.button("Spin"):
    selected = random.choice(categories)
    st.write(f"🎉 Selected: **{selected}**")
else:
    st.write("Waiting for you to spin the wheel!")
