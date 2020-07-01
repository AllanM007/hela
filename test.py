import camelot
tables = camelot.read_pdf('Mpesa.pdf', pages='1-6')
tables

tables.export('mpesa.csv', f='csv', compress=True) # json, excel, html, sqlite
tables[1]

tables[1].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}
tables[1].to_csv('mpesa.csv') # to_json, to_excel, to_html, to_sqlite
tables[1].df # get a pandas DataFrame!