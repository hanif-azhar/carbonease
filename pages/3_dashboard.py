import streamlit as st
import pandas as pd
import plotly.express as px
import os
import plotly.io as pio
from utils.export import generate_pdf
from fpdf import FPDF
from utils.lang import t

# Language selector
lang = st.sidebar.selectbox("🌐 Language", ["en", "id", "jp"])

st.title(t("dashboard_title", lang))

try:
    df = pd.read_csv("data/emission_log.csv")
    df["Date"] = pd.to_datetime(df["Date"])

    # --- FILTER SECTION ---
    st.sidebar.header(t("sidebar_filter", lang))
    start_date = st.sidebar.date_input("Start Date", value=df["Date"].min().date())
    end_date = st.sidebar.date_input("End Date", value=df["Date"].max().date())
    category_filter = st.sidebar.multiselect("Category", df["Category"].unique(), default=list(df["Category"].unique()))

    # Apply filters
    mask = (df["Date"].dt.date >= start_date) & (df["Date"].dt.date <= end_date) & (df["Category"].isin(category_filter))
    df_filtered = df[mask]

    # --- SUMMARY ---
    st.subheader(t("summary_title", lang))
    total_emission = df_filtered["Emission (kg CO₂)"].sum()
    st.metric(t("total_emission", lang), f"{total_emission:.2f} kg")

    # --- SMART SUGGESTION ---
    st.subheader(t("suggestion_title", lang))

    if not df_filtered.empty:
        top_category = df_filtered.groupby("Category")["Emission (kg CO₂)"].sum().idxmax()

        tips = {
            "Electricity": t("tip_electricity", lang),
            "Fuel": t("tip_fuel", lang),
            "Transport": t("tip_transport", lang),
            "Material": t("tip_material", lang)
        }

        suggestion = tips.get(top_category, t("tip_default", lang))
        st.info(f"{t('top_category_msg', lang)} **{top_category}**.\n\n{suggestion}")
    else:
        st.info(t("no_data_suggestion", lang))

    # --- BAR CHART ---
    bar_data = df_filtered.groupby("Category")["Emission (kg CO₂)"].sum().reset_index()
    fig_bar = px.bar(bar_data, x="Category", y="Emission (kg CO₂)", color="Category", title=t("bar_chart_title", lang))
    st.plotly_chart(fig_bar, use_container_width=True)

    # Save bar chart image
    bar_chart_path = "data/bar_chart.png"
    fig_bar.write_image(bar_chart_path)

    # --- PIE CHART ---
    fig_pie = px.pie(bar_data, names="Category", values="Emission (kg CO₂)", title=t("pie_chart_title", lang))
    st.plotly_chart(fig_pie, use_container_width=True)

    # Save pie chart image
    pie_chart_path = "data/pie_chart.png"
    fig_pie.write_image(pie_chart_path)

    # --- CO₂ INTENSITY ---
    st.subheader(t("intensity_title", lang))
    intensity_chart_path = None

    if "Quantity" in df_filtered.columns and "Activity" in df_filtered.columns:
        df_filtered["CO₂ Intensity"] = df_filtered["Emission (kg CO₂)"] / df_filtered["Quantity"]
        intensity_data = df_filtered.sort_values(by="CO₂ Intensity", ascending=False)

        fig_intensity = px.bar(intensity_data, x="Activity", y="CO₂ Intensity", color="Category", 
                               title=t("intensity_chart_title", lang), height=400)
        st.plotly_chart(fig_intensity, use_container_width=True)

        intensity_chart_path = "data/co2_intensity_chart.png"
        fig_intensity.write_image(intensity_chart_path)
    else:
        st.info(t("intensity_missing_data", lang))

    # --- RAW TABLE ---
    with st.expander(t("raw_data", lang)):
        st.dataframe(df_filtered)

    # --- EXPORT SECTION ---
    with st.expander(t("export_section", lang)):
        col1, col2 = st.columns(2)

        with col1:
            csv = df_filtered.to_csv(index=False).encode('utf-8')
            st.download_button(
                label=t("download_csv", lang),
                data=csv,
                file_name="emission_data.csv",
                mime="text/csv"
            )

        with col2:
            if st.button(t("generate_pdf", lang)):
                generate_pdf(
                    df_filtered,
                    total_emission,
                    filename="emission_report.pdf"
                )

                with open("emission_report.pdf", "rb") as f:
                    st.download_button(
                        label=t("download_pdf", lang),
                        data=f,
                        file_name="emission_report.pdf",
                        mime="application/pdf"
                    )
                    
except FileNotFoundError:
    st.warning(t("no_file_warning", lang))
