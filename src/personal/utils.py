
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
import os


import pdfkit
def generate_pdf(template, context={}, save_filename="outut.pdf", download=False):
    options = {
	    'page-size': 'A4',
	    'margin-top': '0.75in',
	    'margin-right': '0.75in',
	    'margin-bottom': '0.75in',
	    'margin-left': '0.75in',
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
