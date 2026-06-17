from pypdf import PdfReader

reader = PdfReader("../data/input/SalarySlip_Ritik_June2026.pdf")
text=""
for page in reader.pages:
    text+= page.extract_text()

print(text)