import PyPDF2
import os
from cStringIO import StringIO
PDFfilename = 'directoryfolderpath/file.pdf'
pfr = PyPDF2.PdfFileReader(open(PDFfilename, "rb"))

pg1 = pfr.getPage(0)
writer = PyPDF2.PdfFileWriter()

writer.addPage(pg1)

NewPDFfilename = PDFfilename + "1" + ".pdf"

with open(NewPDFfilename, "wb") as outputStream:
    writer.write(outputStream)