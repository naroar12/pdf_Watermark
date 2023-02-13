import PyPDF2

file1 = "Django.pdf"
watermark = "watermark.pdf"
mergefile ="combine.pdf"


input_file = open(file1, "rb")
input_pdf1 = PyPDF2.PdfFileReader(input_file)

watermark_file = open(watermark, "rb")
watermark_pdf = PyPDF2.PdfFileReader(watermark_file)

file_page = input_pdf1.getPage(0)

watermark_page = watermark_pdf.getPage(0)

file_page.mergePage(watermark_page)

output = PyPDF2.PdfFileWriter()
output.addPage(file_page)

mergefile= open(mergefile, "wb")
output.write(mergefile)

mergefile.close()
watermark_file.close()
input_file.close()

