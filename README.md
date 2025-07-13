# 🧮 CarbonEase

**CarbonEase** is a lightweight Streamlit app that helps small and medium enterprises (SMEs) track, calculate, and visualize their carbon emissions. Built by [Hanif Azhar](https://github.com/hanif-azhar), this tool supports CSV-based logging and provides charts, smart insights, and PDF exports to help businesses stay on track toward Net Zero 2050.

---

## 🌍 Features

- 🔍 **Interactive Dashboard** – Filter emissions by date or category.
- 📊 **Visual Charts** – Bar, Pie, and Intensity charts using Plotly.
- 💡 **Smart Suggestions** – Auto-suggest actions based on top emitting category.
- 📁 **Raw Data Table** – View, export, and analyze all entries.
- 📄 **Export to PDF & CSV** – One-click report generation.
- 🌐 **Multilingual UI** – Supports English, Bahasa Indonesia, and Japanese.

---

## 📦 Tech Stack

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- [Plotly](https://plotly.com/)
- [FPDF](https://pyfpdf.github.io/)
- [pdfkit](https://pypi.org/project/pdfkit/) *(optional)*

---

## 🚀 How to Run

```bash
# Clone the repo
git clone https://github.com/hanif-azhar/carbonease.git
cd carbonease

# (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py

```
## Folder Structure
carbonease/
├── pages/             # Extra Streamlit pages
│   ├── 1_Input.py     # User input page
│   ├── 2_Log.py       # Emission log view
│   └── 3_Dashboard.py # Dashboard & reporting
├── utils/             # Helper functions
│   ├── export.py
│   └── lang.py
├── data/              # Emission CSV and chart images
├── app.py             # Main app
└── .gitignore

## Why
Many SMEs lack the tools to measure and reduce their carbon footprint. CarbonEase is built to change that — fast, easy, and transparent.

## Author (ME)
Made with love and cursing by Hanif Azhar
📍 SEA | 🧑‍💻 Building tech x sustainability | 🐰 Idol & gaming enthusiast

## License 
MIT License — free to use, remix, improve, and deploy.
