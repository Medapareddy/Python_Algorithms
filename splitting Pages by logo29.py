# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:25:05 2019

@author: Srijan.Reddy
"""

import xlrd
from xlrd import open_workbook
import os
import shutil
import openpyxl
from openpyxl.reader.excel import load_workbook
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2 import PdfFileMerger, PageRange

import io
#from pytesseract import image_to_string
#from pytesseract import image_to_boxes
import wand
from wand.image import Image
import cv2
import numpy as np


#Camlot

#import camelot



#from spacy.pipeline import EntityRuler
#from spacy.lang.en import English
#from spacy.matcher import PhraseMatcher


# import spellchecker





cwd = os.getcwd()
workflow_Excel_path = os.path.join(cwd, "Workflow.xlsx")
wb = load_workbook(workflow_Excel_path)
workbook = open_workbook(workflow_Excel_path)
sheet = workbook.sheet_by_index(0)
ghostscriptpath = sheet.cell_value(6, 1)
imagemagickpath = sheet.cell_value(7, 1)

path_to_gs = ghostscriptpath
os.environ['PATH'] += os.pathsep + path_to_gs
os.environ['PATH'] += os.pathsep + imagemagickpath
# import StanfordNER




# >>>>>>>------   Support Functions ----------------------------

# Current Working Directory
cwd = os.getcwd()
# print(cwd)
# workflow_Excel_path = os.path.join(cwd, "Workflow.xlsx")




# ----  Get Source path details ------->>>

def getSourcePathDetails():
    workbook = open_workbook(workflow_Excel_path)
    sheet = workbook.sheet_by_index(0)
    # if sheet.cell_value(0, 2) == "Applicable":
    return sheet.cell_value(0, 1)
    # elif sheet.cell_value(1, 2) == "Applicable":
#         return sheet.cell_value(1, 1)


def getResultPathDetails():
    workbook = open_workbook(workflow_Excel_path)
    sheet = workbook.sheet_by_index(0)
    # if sheet.cell_value(1, 2) == "Applicable":
    return sheet.cell_value(1, 1)

# -------------------------------------
# ---  Preferences ------------------


def getPrefSplitpageByLogo():
    workbook = open_workbook(workflow_Excel_path)
    sheet = workbook.sheet_by_index(0)
    if sheet.cell_value(9, 2) == "Applicable":
        return sheet.cell_value(9, 2)


def getPagePreferences():
    workbook = open_workbook(workflow_Excel_path)
    sheet = workbook.sheet_by_index(0)
    if sheet.cell_value(8, 2) == "Applicable":
        return sheet.cell_value(8, 1)


def getExtractDataPref():
    workbook = open_workbook(workflow_Excel_path)
    sheet = workbook.sheet_by_index(0)
    if sheet.cell_value(10, 2) == "Applicable":
        return True


def getExtractTablesPref():
    workbook = open_workbook(workflow_Excel_path)
    sheet = workbook.sheet_by_index(0)
    if sheet.cell_value(11, 2) == "Applicable":
        return True


# --- End of Preferences ------------------   
 
    
def makddirectory(name):
    current_directory = os.getcwd()
    final_directory = os.path.join(current_directory, name)
    if not os.path.exists(final_directory):
        #print("***************final_directory********************")
        #print(final_directory)
        os.makedirs(final_directory) 
        
        # To check the image clarity


resofestimate = ""
              
    
rootPath = getSourcePathDetails()
   
print("rootPath -- "+rootPath)
     
pathforclientdirs = os.path.join(rootPath)
resultPath = getResultPathDetails()
clientdirname ="PDFs"
        
def splitpagesbyAssignees(pathforclientdirs,clientdirname,resultPath):
    for root, dirs, files in os.walk(pathforclientdirs):
        makddirectory(clientdirname)
      
        filecount = 0
        #fileName = os.path.basename(clientdirname).replace("/","-")
        for file in files:
              if file.endswith(".pdf") or file.endswith(".PDF"):
                  
                filecount = filecount+1  
                  
                shutil.copy(os.path.join(root, file), clientdirname)
                
                #To split the PDFs by pages
                reader = PdfFileReader(os.path.join(clientdirname, file))
                cnt = reader.getNumPages()
                print("Counttt")
                print(cnt)
                
                
                
                countformerge = 0
                temp = 0
                
               #get all pages text (After image conversion)
                for i in range(cnt):
                    
                    found = False
                    
                    writer = PdfFileWriter() 
                    writer.addPage(reader.getPage(i))
                    
                    
                  
                    pdf_bytes = io.BytesIO()
                    writer.write(pdf_bytes)
                    pdf_bytes.seek(0)
                   
                    
                    img = Image(file = pdf_bytes, resolution = 300)
                    img.save(filename = os.path.join(clientdirname, file)+str(i)+"-template-target.png") 
                    
                    
                    
                    image = cv2.imread(os.path.join(clientdirname, file)+str(i)+"-template-target.png")
                    
                    
                    for image_to_match in os.listdir(os.path.join(cwd+"\\Notice-header-templates")):
                        
                        #template = cv2.imread(os.path.join(cwd+"\\Notice-header-templates", "logo5.png"))
                        #print(image_to_match)
                        
                        template = cv2.imread(os.path.join(cwd+"\\Notice-header-templates",image_to_match))
                        #image = cv2.resize(image, (0,0), fx=0.5, fy=0.5)
                        #template = cv2.resize(template, (0,0), fx=0.5, fy=0.5)
                        
                        #print(os.path.join(cwd+"\\Notice-header-templates", "logo1.png"))
                        
                        # Convert to grayscale
                        
                        imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                        imageGray = cv2.resize(imageGray,None,fx=0.5,fy=0.5)
                        kernel = np.ones((2, 2), np.uint8)
                        imageGray = cv2.erode(imageGray, kernel, iterations=3)
                        
                        kernel = np.ones((3, 3), np.uint8)
                        template = cv2.erode(template, kernel, iterations=2)
                        templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
                        
                        w, h = templateGray.shape[::-1]
                        
                        w1, h1 = imageGray.shape[::-1]
                        
                        # Crop top part for matching logo here 
                        crop_img = imageGray[0:0+300, 0:0+w1]
                        cv2.imwrite(os.path.join(clientdirname, file)+str(i)+"-templateGray-cropped.png",crop_img)
                        
                        tobematched = cv2.imread(os.path.join(clientdirname, file)+str(i)+"-templateGray-cropped.png")
                  
                        tobematched = cv2.cvtColor(tobematched, cv2.COLOR_BGR2GRAY)
                        
                        #print(tobematched)
                        res = cv2.matchTemplate(tobematched,templateGray,cv2.TM_CCOEFF_NORMED)
                        threshold = 0.7
                        loc = np.where( res >= threshold)
    
                        for pt in zip(*loc[::-1]):
                            found = True
                            cv2.rectangle(tobematched, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
                        
                        #print("-------->>>> result <<<<<--**------")
                        #print(found)
                        #print(i)
                        #print(resultTemplateMatches)
                        #print(template)
                        cv2.imwrite(os.path.join(clientdirname, file)+str(i)+"-template-detected.png",tobematched)
                        cv2.imwrite(os.path.join(clientdirname, file)+str(i)+"-templateGray.png",templateGray)
                        
                        if found:
                            break
                        
                    
                     
                    print("----------- found ==============")
                    print(i)
                    print(found)
                    if found and i > 0:
                        
                        #found = False
                        #merger.append(os.path.join(clientdirname, file),pages=PageRange(0,i))
                        if countformerge == 0:
                           print("countformerge")
                           print(i)
                           merger = PdfFileMerger()
                           merger.append(os.path.join(pathforclientdirs, file),pages=(0,i),import_bookmarks=False)
                           merger.write(os.path.join(resultPath, file)+"page-"+str(i)+"split-by-assignee.pdf")
                           temp = i
                           countformerge = countformerge+1
                           merger.close() 
                        else:
                           merger = PdfFileMerger()
                           print("========== Temp ============")
                           print(temp)
                           print(i)
                           print("Count for mergeeeee")
                           merger.append(os.path.join(pathforclientdirs, file),pages=(temp,i),import_bookmarks=False)
                           merger.write(os.path.join(resultPath, file)+"page-"+str(i)+"split-by-assignee.pdf")
                           temp = i
                           merger.close()
                    if i==cnt-1:
                        merger = PdfFileMerger()       
                        print("Temp for last index -->")
                        print(i+1)
                        print(temp)
                        
                        
                        
                        # temp+1 changed to temp now due to include template page for last left
                        merger.append(os.path.join(pathforclientdirs, file),pages=(temp,i+1),import_bookmarks=False)
                        merger.write(os.path.join(resultPath, file)+"page-"+str(i-1)+"split-by-assignee.pdf")
                        merger.close()               
                        
                        #FileName = os.path.join(clientdirname, file)+"page-"+str(i)+"split-by-assignee.pdf"
                        #with open(FileName, 'wb') as outfile:
                                #writer.write(outfile)


splitpagesbyAssignees(pathforclientdirs,clientdirname,resultPath)
    
    

