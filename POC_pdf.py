# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 14:51:54 2017

@author: Ramya.Medapareddy
"""
import os
#import pyPdf
#from PyPDF2 import PdfFileReader, PdfFileWriter
#
#path = "C:/Users/Ramya.Medapareddy/Documents/POC_Reader"
#dirs = os.listdir( path )
#Input_File = "C:/Users/Ramya.Medapareddy/Documents/POC_Reader/Audit client and affiliates.pdf"
#f = open(Input_File, 'rb')
#reader = PdfFileReader(f)
#contents = reader.getPage(1).extractText().split('\n')
#f.close()
#print(contents)

import PyPDF2


# Which you want to read file so give file name with ".pdf" extension
pdf_file = open("C:/Users/Ramya.Medapareddy/Documents/POC_Reader/Audit_client_and_affiliates.pdf","rb")
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()

#Give page number of the pdf file (How many page in pdf file).
# @param Page_Nuber_of_the_PDF_file: Give page number here i.e 1
page = read_pdf.getPage(0)

#page_content = page.extractText()
contents = read_pdf.getPage(2).extractText()

# Display content of the pdf
print(number_of_pages)
#print(page_content)
print(contents)
content = ""
pg3 = read_pdf.getPage(1).extractText() + " \n" #extract pg 2
content = " ".join(content.replace(u"\xa0", u" ").strip().split())
print(pg3)
f = open('a.txt','w+')

f.write(content)
f.close()
import re
pdf_file = open("C:/Users/Ramya.Medapareddy/Documents/POC_Reader/Audit_client_and_affiliates.pdf","rb")
for line in read_pdf.getPage(1).extractText(): #iterate through every line
	#return list of dates in that line
    #contents = read_pdf.getPage(1).extractText()
    x = re.findall('.*([a-zA-Z]+\s[0-9][0-9],\s[0-9][0-9][0-9][0-9]).*', line)
	#if a date is found
    if len(x) != 0:
	    print(x)
print(line)
