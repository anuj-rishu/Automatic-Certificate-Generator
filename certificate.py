
from docxtpl import DocxTemplate
import pandas as pd
from docx2pdf import convert
import os

ans=pd.read_csv('data.csv')
n=(len(ans))

def mkw(n, j):
    tpl=DocxTemplate("temp.docx")
    context={i+1:{"name":ans['name'][i],}for i in range (n)}
    tpl.render(context[n])
    docx_filename = "%s - "%str(n)+ans['name'][j]+".docx"
    pdf_filename = "%s - "%str(n)+ans['name'][j]+".pdf"
    tpl.save(docx_filename)
    convert(docx_filename, pdf_filename)
    os.remove(docx_filename)

for i in range(n):
    mkw(i+1, i)
