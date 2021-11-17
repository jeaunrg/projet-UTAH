from django.http import HttpResponse
from django.template.loader import get_template
import os
import pdfkit
import barcode

def get_patient_hospital_num(patient):
    return 251239853244

def generate_pdf(template, context=None, save_filename="outut.pdf", download=False):
    if context is None:
        context = {}
    margin = '0'
    options = {
        'page-size': 'A4',
        'margin-top': margin + 'in',
        'margin-right': margin + 'in',
        'margin-bottom': margin + 'in',
        'margin-left': margin + 'in',
    }

    template = get_template(template)
    html = template.render(context)
    pdfkit.from_string(html, 'out.pdf', options=options)
    pdf = open("out.pdf", 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')
    if download:
        response['Content-Disposition'] = 'attachment; filename={}'.format(save_filename)
    pdf.close()
    os.remove("out.pdf")
    return response

def generate_bar_code(num):
    svg = barcode.get('ean13', str(num))
    return svg.render().decode("utf-8")
