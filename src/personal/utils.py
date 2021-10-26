
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import os


import pdfkit
def generate_pdf(template, context={}, save_filename="outut.pdf", download=False):
    margin = '0'
    options = {
	    'page-size': 'A4',
	    'margin-top': margin+'in',
	    'margin-right': margin+'in',
	    'margin-bottom': margin+'in',
	    'margin-left': margin+'in',
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
