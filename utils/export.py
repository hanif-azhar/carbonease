# utils/export.py
import pdfkit
import pandas as pd

PDFKIT_CONFIG = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

def generate_pdf(df, total_emission, filename="report.pdf"):
    html = f"""
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            body {{ font-family: Arial, sans-serif; margin: 30px; }}
            h1 {{ text-align: center; }}
            table {{ width: 100%; border-collapse: collapse; margin-top: 20px; }}
            th, td {{ border: 1px solid #ccc; padding: 8px; text-align: left; }}
        </style>
    </head>
    <body>
        <h1>CarbonEase Emission Report</h1>
        <p><strong>Total Emission:</strong> {total_emission:.2f} kg CO₂</p>
        <br>
        {df.to_html(index=False)}
    </body>
    </html>
    """
    pdfkit.from_string(html, filename, configuration=PDFKIT_CONFIG)
