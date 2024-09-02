from PyPDF2 import PdfReader


file = 'C:/Users/joqta/OneDrive/Instaladores/Proyectos/AutomatizacionS150/Ejemplo.pdf'
pdfReader = PdfReader(file)

for page in range(len(pdfReader.pages)):
    if pdfReader.get_fields(f'/Contents[{page}]') is not None:
        print(f'The PDF on page {page} uses AcroForm fields')
        break
    else:
        print('The PDF does not use AcroForm fields')

"""Checkboxes = pdfReader.get_fields()
print(Checkboxes)"""

