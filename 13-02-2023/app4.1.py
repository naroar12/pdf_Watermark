   
import os      
import PyPDF2
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter




path = input("Enter path of your file  ")
os.chdir(path)

pageObj = input("Enter the name of your pdf file with pdf extension  ")




# this function is to ake a pdf file and megre watermak with the input file
def add_watermark(pageObj):
        
        pdf_file = pageObj
        watermark = "watermark.pdf"
        merged = "merged_file1.pdf"

        with open(pdf_file, "rb") as input_file, open(watermark, "rb") as watermark_file:
            input_pdf = PyPDF2.PdfFileReader(input_file)
            watermark_pdf = PyPDF2.PdfFileReader(watermark_file)
            watermark_page = watermark_pdf.getPage(0)

            output = PdfFileWriter()

            for i in range(input_pdf.getNumPages()):
                pdf_page = input_pdf.getPage(i)
                pdf_page.mergePage(watermark_page)
                output.addPage(pdf_page)

            with open(merged, "wb") as merged_file1:
                output.write(merged_file1)





    



        