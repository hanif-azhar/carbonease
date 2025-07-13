# pages/4_Monthly_Summary.py
import streamlit as st
import pandas as pd
import plotly.express as px
from utils.lang import t

# Language selector
lang = st.sidebar.selectbox("🌐 Language", ["en", "id", "jp"])

st.title(t("monthly_title", lang))

try:
    df = pd.read_csv("data/emission_log.csv")
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M").astype(str)

    monthly_summary = df.groupby("Month")["Emission (kg CO₂)"].sum().reset_index()

    st.metric(t("total_logged", lang), f"{df['Emission (kg CO₂)'].sum():.2f} kg")

    # Line chart
    fig_line = px.line(monthly_summary, x="Month", y="Emission (kg CO₂)", markers=True,
                       title=t("monthly_line_title", lang))
    st.plotly_chart(fig_line, use_container_width=True)

    # Bar chart
    fig_bar = px.bar(monthly_summary, x="Month", y="Emission (kg CO₂)", 
                     title=t("monthly_bar_title", lang))
    st.plotly_chart(fig_bar, use_container_width=True)

    # Raw table
    with st.expander(t("view_data_table", lang)):
        st.dataframe(monthly_summary)

except FileNotFoundError:
    st.warning(t("no_data_warning", lang))
