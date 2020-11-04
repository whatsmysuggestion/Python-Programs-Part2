from fpdf import FPDF
from sys import *
pdf = FPDF()

pdf.compress = False
pdf.add_page()
pdf.set_font('Arial', '', 14)
pdf.ln(10)
pdf.write(5, 'hello world')
pdf.image("logo.png", 50, 50)
pdf.output('py3k.pdf', 'F')