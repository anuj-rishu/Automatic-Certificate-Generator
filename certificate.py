from docxtpl import DocxTemplate
import pandas as pd
from docx2pdf import convert
import os

ans = pd.read_csv('data.csv')
n = len(ans)

def mkw(record, index):
    tpl = DocxTemplate("certificate.docx")
    context = {"name": record['name']}
    tpl.render(context)
    docx_filename = f"{index} - {record['name']}.docx"
    pdf_filename = f"{record['name']}.pdf"  # Modified line, removing the index prefix
    tpl.save(docx_filename)
    convert(docx_filename, pdf_filename)
    os.remove(docx_filename)

for i in range(n):
    mkw(ans.iloc[i], i+1)
