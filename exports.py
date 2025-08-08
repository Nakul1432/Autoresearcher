# export.py
from fpdf import FPDF

def export_to_pdf(report_data, filename="report.pdf"):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Research Report", ln=True, align="C")
    pdf.ln(10)
    for item in report_data:
        pdf.multi_cell(0, 10, f"Source: {item['url']}")
        pdf.multi_cell(0, 10, item['summary'])
        pdf.ln(5)
    pdf.output(filename)

def export_to_markdown(report_data, filename="report.md"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# Research Report\n\n")
        for item in report_data:
            f.write(f"## Source: {item['url']}\n\n")
            f.write(f"{item['summary']}\n\n")
