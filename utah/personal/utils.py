from django.http import HttpResponse
from django.template.loader import get_template
import os
import pdfkit
import barcode
import random
from editable.settings import PDF_OPTIONS


def generate_pdf(template, context={}, save_filename="outut.pdf", download=False):
    template = get_template(template)
    html = template.render(context)
    pdfkit.from_string(html, 'tmp.pdf', options=PDF_OPTIONS)
    pdf = open("tmp.pdf", 'rb')
    response = HttpResponse(pdf.read(), content_type='application/pdf')
    if download:
        response['Content-Disposition'] = 'attachment; filename={}'.format(save_filename)
    pdf.close()
    os.remove("tmp.pdf")
    return response

def generate_bar_code(num):
    svg = barcode.get('ean13', str(num))
    return svg.render().decode("utf-8")
