# Automated Document Generation from CSV Data

This Python script automates the generation of documents (in both .docx and .pdf formats) from a CSV file containing data. It uses the `docxtpl` library to fill in a template document with data from the CSV file, and then converts the filled-in document into a PDF format using `docx2pdf`. 

## Requirements

- Python 3.x
- `pandas` library (`pip install pandas`)
- `docxtpl` library (`pip install docxtpl`)
- `docx2pdf` library (`pip install docx2pdf`)

## Usage

1. **Prepare your data**: Ensure your data is in a CSV format (`data.csv`) and contains the necessary fields.
   
2. **Prepare the template document**: Create a Word document (`certificate.docx`) with placeholders that will be replaced by the data from the CSV file. Placeholders should be in double curly braces, e.g., `{{ name }}`.

3. **Run the script**: Execute the Python script `generate_documents.py`. The script will read data from `data.csv`, fill in the template document `certificate.docx`, convert it into both `.docx` and `.pdf` formats, and save them in the current directory.

```bash
python generate_documents.py
