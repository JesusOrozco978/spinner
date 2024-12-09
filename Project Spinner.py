import streamlit as st
import random
import math
import matplotlib.pyplot as plt

# Data for the spinner
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


# Spinner function
def create_spinner(selected_index=None):
    plt.figure(figsize=(6, 6))
    ax = plt.subplot(111, polar=True)
    num_sections = len(categories)
    angles = [2 * math.pi * i / num_sections for i in range(num_sections + 1)]
    colors = ["#FF5733", "#33FF57", "#3357FF", "#FF33A1", "#FFD733"] * (num_sections // 5 + 1)

    # Draw spinner sections
    for i in range(num_sections):
        ax.fill_between(angles[i:i + 2], 0, 1, color=colors[i], edgecolor="black")

    # Add text for each section
    for i in range(num_sections):
        angle = (angles[i] + angles[i + 1]) / 2
        ax.text(
            angle, 0.6, categories[i],
            horizontalalignment="center",
            verticalalignment="center",
            fontsize=10,
            rotation=math.degrees(angle),
            rotation_mode="anchor"
        )

    # Highlight the selected section
    if selected_index is not None:
        ax.fill_between(
            angles[selected_index:selected_index + 2], 0, 1, color="yellow", edgecolor="black"
        )

    ax.set_yticklabels([])
    ax.set_xticks([])
    ax.set_theta_zero_location("N")
    plt.title("Interactive Spinner", va="bottom", fontsize=16)
    st.pyplot(plt)


# Streamlit app
st.title("Interactive Spinner")

if st.button("Spin"):
    selected_index = random.randint(0, len(categories) - 1)
    create_spinner(selected_index)
    st.write(f"**Selected:** {categories[selected_index]}")
else:
    create_spinner()
