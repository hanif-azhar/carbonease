# pages/2_Input.py
import streamlit as st
import pandas as pd
from datetime import datetime
from utils.calculator import calculate_emission
from utils.lang import t

# --- LANGUAGE SETUP ---
lang = st.sidebar.selectbox("🌐 Language", ["en", "id", "jp"])

st.title(t("input_title", lang))

# Step 1: Select input
category = st.selectbox(t("category_label", lang), ["Electricity", "Fuel", "Transport", "Material"])

activity_map = {
    "Electricity": ["Grid Electricity"],
    "Fuel": ["Diesel", "Petrol"],
    "Transport": ["Car (average)", "Flight (short haul)", "Flight (long haul)"],
    "Material": ["Plastic", "Steel", "Aluminum"]
}

activity = st.selectbox(t("activity_label", lang), activity_map[category])
value = st.number_input(t("value_label", lang), min_value=0.0, step=0.1)
unit = st.text_input(t("unit_label", lang))
date = st.date_input(t("date_label", lang), value=datetime.today())
submit = st.button(t("submit_label", lang))

# Step 2: Calculate and show result
if submit:
    emission = calculate_emission(category, activity, value)

    if emission is not None:
        st.success(t("emission_result", lang).format(emission=emission))

        # Step 3: Save to log file
        new_data = {
            "Date": [date],
            "Category": [category],
            "Activity": [activity],
            "Value": [value],
            "Unit": [unit],
            "Emission (kg CO₂)": [emission]
        }

        df_new = pd.DataFrame(new_data)

        try:
            df_existing = pd.read_csv("data/emission_log.csv")
            df_combined = pd.concat([df_existing, df_new], ignore_index=True)
        except FileNotFoundError:
            df_combined = df_new

        df_combined.to_csv("data/emission_log.csv", index=False)
        st.info(t("saved_success", lang))

    else:
        st.error(t("emission_not_found", lang))
