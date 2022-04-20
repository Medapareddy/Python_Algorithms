import json
#checklist_dict = json.loads()

import requests
from requests.auth import HTTPDigestAuth
import json
from fuzzywuzzy import fuzz  


Str1 = "30 6A/JUN 2029"
Str2 = "30Jun2029"
Ratio = fuzz.ratio(Str1.lower(),Str2.lower())
print(Ratio)

from shared_utils.base_imports import *

# Issue date is
# 13sep2017
# Issue date is
# 13sep2017
# visaIssueDate ++++++
# 13Sep2017


from datetime import datetime

s = "09JAN1988"
d = datetime.strptime(s, '%d%b%Y')
print(d.strftime('%Y-%m-%d'))

s3 = "1988-01-09"
d = datetime.strptime(s3, '%Y-%m-%d')
print(d.strftime('%d%b%Y'))



checklist = [{"caseId":"KBGFJG02117-17","applicantType":"Main","mainBNFId":"BGFJG02117","documentCheckList":[{"firstName":"Tengjiao","middleName":"","lastName":"XIAO","applicantID":"BGFJG02117","applicantType":"Main","requiredDocuments":["Certified LCA","Passport Biographic Page","I-94 Record","Visas (current and prior)","I-797 Approval Notices (current and prior)","Recapture Chart / I-94 History / Evidence (if applicable)","DS-2019 and/or J-1 Waiver (if applicable)","Equivalency Evaluation (if applicable)","Academic Degrees, Transcripts / Translations","3 Most Recent Paystubs","Client Specific Documentation (Annual Report / Financial Statement if applicable.)","AC21 Evidence (I-140 Approval Notice & Visa Bulletin if applicable)"],"visaIssueDate":"2017-09-13","visaExpiryDate":"2018-09-11","passportNo":"EG4994324","dob":"1988-01-09","placeOfBirth":"China","passportIssueDate":"2019-07-01","passportExpiryDate":"2029-06-30","passportCountry":"United States of America","eadIssuedate":"","eadExpiryDate":"","location":"\\\\CATORVWXFARSA1\\Raw Input Files\\KBGFJG02117-17\\BGFJG02117"}]}]

#extracted = [{'OeytestBGFJG021172021328714542.enc_plain.pdf': {'Issuing Post Name Control Number': 'BEIJING 20172514280021', 'issue': 'Not Found', 'Issue Date': '13SEP2017', '*issue Date': '13SEP2017', '*issue': '13SEP2017', 'Expiration Date': '11SEP2018', '*Expiration Date': '11SEP2018', 'Passport Number': '643297542', '*Passport Number': '18091', 'Document type': 'Visa', '*Type': 'H1B', 'Name in MRZ': 'TENGJIAO', '*Name in MRZ': 'TENGJIAO', 'Passport number in MRZ': '18091', 'Entries': 'M', 'Issuing Post Name': 'BEIJING', 'Control Number': '20172514280021', 'Birth Date': '09JAN1988', 'a Type /Class': 'H1B', '*Class': 'H1B', 'Nationality': 'CHIN', 'iven Name': 'ENG.1TAN', '*Given Name': 'ENG.1TAN', 'urname': 'TAO', '*Surname': 'TAO', 'DocType': 'Visa'}}, {'OeytestBGFJG021172021329261517.enc_plain.pdf': {'Receipt Number': 'EAC1912550318', 'Signature': 'Not Found', 'Received date': 'Received Date03/01/2019', 'Class': 'H1B', 'Petitioner': 'ERNST & YOUNG U S LLP,', 'Case Type': '1129 - PETITION FOR A NONIMMIGRANT WORKER', 'Notice Date': '| 03/19/2019', 'DocType': '797'}}]

extracted = [{'OeytestBGFJG021172021330278722.enc_plain.pdf': {'Place of Birth': 'Not Found', 'Country': 'CHN', 'Date of expiry': '30 6A/JUN 2029', 'Type': 'Passport', 'Name in MRZ': 'TENGJIADXK<K<KKKKK', 'Passport': '    ', 'Passport number in MRZ': 'E649943245', 'DocType': 'Passport'}}, {'OeytestBGFJG02117171209n622740.enc_plain.pdf': {'Issuing Post Name': 'Not Found', 'Type': 'R Fi\x0c', 'Name in MRZ': '', 'Passport Number': 'G43297542', 'issue Date': '20DEC2013', 'issue': '20DEC2013', 'Expiration Date': '17DEC2014', 'Visa': 'R Fi\x0c', 'Control Number': '20133528588020', 'Nationality': 'CHIN', 'DocType': 'Visa'}}, {'OeytestBGFJG021172021328714542.enc_plain.pdf': {'Issuing Post Name': 'Not Found', 'issue Date': '13SEP2017', 'issue': '13SEP2017', 'Expiration Date': '1ISEP2018', 'Passport Number': '6432975424', 'Type': 'H1B', 'Name in MRZ': 'TENGJIA0', 'Control Number': '20172514280021', 'Class': 'H1B', 'Nationality': 'CHIN', 'DocType': 'Visa'}}, {}, {}, {}, {'OeytestBGFJG021172021329261517.enc_plain.pdf': {'Receipt Number': 'BAC1912550318\x0c', 'Signature': 'Not Found', 'Received date': 'Received Date03/01/2019\x0c', 'Beneficiary': 'XIAO, TENGJIAO\x0c', 'Petitioner': 'ERNST & YOUNG U S LLP,\x0c', 'Class': 'HIB', 'Notice Date': '| 03/19/2019\x0c', 'DocType': 'notice of action'}}, {'OeytestBGFJG02117151161116180777.enc_plain.pdf': {'passport number': ': g43297542', 'DocType': 'i-94', 'most recent date of entry:': ' 2014 january 14', 'surname': ': xiao', '(given) name': ': tengjiao', 'country of issuance': ': china'}},{'OeytestBGFJG0211720930836237928.enc_plain.pdf': {'period beg/end': ': 08/22/2020 09/04/2020', 'advice date': ': 09/11/2020', 'batch number': ': 000000000615', 'basis of pay': ': salary', 'employee id': ' 11.95934', 'DocType': 'paystubs'}}, {'OeytestBGFJG021172093083650242.enc_plain.pdf': {'period beg/end': ': 09/05/2020 09/18/2020', 'advice date': ': 09/25/2020', 'batch number': ': 000000000641', 'basis of pay': ': salary', 'employee id': ' 11.95934', 'DocType': 'paystubs'}}, {'OeytestBGFJG0211720930836831295.enc_plain.pdf': {'period beg/end': ': 08/08/2020 08/21/2020', 'advice date': ': 08/28/2020', 'batch number': ': 000000000583', 'basis of pay': ': salary', 'employee id': ' 11.95934', 'DocType': 'paystubs'}}]
    
#print(checklist)

#print("*********")
#print(extracted_res) 


main_info = []
main_info_dict = {}
  
checklist_index = 0
checklist_info = []

#json_content

#print(json_content)



final_res = {}
doc_list = []

first_name = ""
visaIssueDate = ""
case_id_for_compilation = ""
passportNo = ""
passportExpiryDate = ""
visaExpiryDate = ""

compilation_shortlisted = []


# Initial declarations and assignements
for key, value in checklist[0].items():
    
    
    # Initial declarations and assignements
    
    if key == "documentCheckList":
        for i in range(len(value)):
            
            #print(value[i])
            for key3, value3 in value[i].items():
                 if key3 == "visaIssueDate":
                    visaIssueDate =  datetime.strptime(value3, '%Y-%m-%d')
                    visaIssueDate = visaIssueDate.strftime('%d%b%Y')
                    print("visaIssueDate ++++++")
                    print(visaIssueDate)
                    
                 if key3 == "passportExpiryDate":
                    passportExpiryDate =  datetime.strptime(value3, '%Y-%m-%d')
                    passportExpiryDate = passportExpiryDate.strftime('%d%b%Y')
                    print("passportExpiryDate ++++++")
                    print(passportExpiryDate)
                    
                 if key3 == "visaExpiryDate":
                    visaExpiryDate =  datetime.strptime(value3, '%Y-%m-%d')
                    visaExpiryDate = visaExpiryDate.strftime('%d%b%Y')
                    print("visaExpiryDate ++++++")
                    print(visaExpiryDate)
                    
                 if key3 == "passportNo":
                    passportNo = value3
                    print("passportNo ++++++")
                    print(passportNo)   
                    
                    

    if key == 'caseId':
        case_id_for_compilation = checklist[0]['caseId']
        print("Case_id ++++++")
        print(case_id_for_compilation)

for key, value in checklist[0].items():
   
    
    if key == 'caseId':
        #print(checklist[0]['caseId'])
        final_res.update({'caseId':checklist[0]['caseId']})
        
    if key == 'documentCheckList':
        
        
        for i in range(len(value)):
            
            meta_index = 0
            for key3, value3 in value[i].items():
                 
                  if key3 == "firstName":
                     first_name =  value3
                   
                  #d = datetime.strptime(s3, '%Y-%m-%d') 
                 
                  
                  if key3 == "requiredDocuments":
                      
                      temp_dict = {}
                      
                      
                      for kk in range(len(value3)):
                          
                          #print(value3[kk])
                          #print("=======")
                          temp_dict.update({"requiredDocumentName":value3[kk]})
                          temp_dict.update({"applicantId":value[i]['applicantID']})
                          
                          match_flag = False
                          
                          for k in range(len(extracted)):
                              
                              
                              metadataIdentified = []
                              #meta_index = meta_index+1
                              
                              
                              
                              for key_ext, val_ext in extracted[k].items():
                                  
                                  
                                  for key_ext3, val_ext3 in val_ext.items():
                                      
                                      
                                      #metadataIdentified_dict.update({key_ext3:val_ext3})
                                      
                                      if key_ext3 == "DocType":
                                          
                                          #  --- Customization of file names
                                          if val_ext3.lower() == "notice of action":
                                              val_ext3 = "i-797"
                                              print("=== In notice of action ===")
                                              print(val_ext3)
                                              print(value3[kk].lower())
                                          
                                          # Match or check file names
                                          if val_ext3.lower() in value3[kk].lower():
                                              temp_dict.update({"documentName":key_ext})
                                              
                                              match_flag = True
                                              
                                              match_ratio = 0
                                              
                                              for key_ext4, val_ext4 in val_ext.items():
                                                 metadataIdentified_dict = {}
                                                 #metadataIdentified_dict.update({key_ext4:val_ext4})
                                                 
                                                 metadataIdentified_dict.update({"ParamName":key_ext4})
                                                 metadataIdentified_dict.update({"ParamValue":val_ext4.replace("<K","")})
                                                 
                                                 #print("visaIssueDate")
                                                 #print(visaIssueDate)
                                                 
                                                 # if first_name.lower() == val_ext4.lower():
                                                 #     metadataIdentified_dict.update({"Conf":"90"})
                                                 
                                                 # ---  For paystubs to append ------
                                                 if "salary" in val_ext4.lower():
                                                     match_ratio = match_ratio+20
                                                 
                                                 if fuzz.ratio(first_name.lower(),val_ext4.lower())>60 and fuzz.ratio(first_name.lower(),val_ext4.lower())<80:
                                                     #metadataIdentified_dict.update({"matched":first_name+":"+val_ext4+"(70%)"})
                                                     metadataIdentified_dict.update({"conf":"70"})

                                                     match_ratio = match_ratio+20
                                                     
                                                 elif fuzz.ratio(first_name.lower(),val_ext4.lower())>80 and fuzz.ratio(first_name.lower(),val_ext4.lower())<90:
                                                     #metadataIdentified_dict.update({"matched":first_name+":"+val_ext4+"(85%)"})
                                                     metadataIdentified_dict.update({"conf":"85"})
                                                     match_ratio = match_ratio+20
                                                     
                                                 elif fuzz.ratio(first_name.lower(),val_ext4.lower())>90:
                                                     #metadataIdentified_dict.update({"matched":first_name+":"+val_ext4+"(100%)"})
                                                     metadataIdentified_dict.update({"conf":"90"})
                                                     match_ratio = match_ratio+20
                                                 else:
                                                     fname1 = first_name.lower()[:4]
                                                     fname2 = val_ext4.lower()[:4]
                                                     similarity_ratio = fuzz.ratio(fname1,fname2)
                                                     if similarity_ratio > 80:
                                                         #metadataIdentified_dict.update({"matched":first_name+":"+val_ext4+"(80%)"})
                                                         metadataIdentified_dict.update({"conf":"80"})
                                                         match_ratio = match_ratio+20
                                                         
                                                     
                                                 # if visaIssueDate.lower() == val_ext4.lower():
                                                     
                                                 #     print("Issue date is not")
                                                 #     print(val_ext4.lower())
                                                 #     print(visaIssueDate.lower())
                                                 #     metadataIdentified_dict.update({"test":"90"})    
                                                  
                                                 if fuzz.ratio(visaIssueDate.lower(),val_ext4.lower())>80:
                                                     #metadataIdentified_dict.update({"matched":visaIssueDate.lower()+":"+val_ext4.lower()+"(100%)"})
                                                     metadataIdentified_dict.update({"conf":"100"})
                                                     match_ratio = match_ratio+20
                                                     
                                                 if key_ext4 == "Issue Date":
                                                     print("Issue date is >> here --")
                                                     print(visaIssueDate.lower())
                                                     print(val_ext4.lower())
                                                  
                                                 
                                                 if fuzz.ratio(passportNo.lower(),val_ext4.lower())>70:
                                                     #metadataIdentified_dict.update({"matched":visaIssueDate.lower()+":"+val_ext4.lower()+"(100%)"})
                                                     metadataIdentified_dict.update({"conf":"80"})
                                                     match_ratio = match_ratio+20
                                                     
                                                     
                                                 if fuzz.ratio(passportExpiryDate.lower(),val_ext4.lower())>75:
                                                     #metadataIdentified_dict.update({"matched":visaIssueDate.lower()+":"+val_ext4.lower()+"(100%)"})
                                                     metadataIdentified_dict.update({"conf":"100"})
                                                     match_ratio = match_ratio+20
                                                     
                                                 if fuzz.ratio(visaExpiryDate.lower(),val_ext4.lower())>75:
                                                     #metadataIdentified_dict.update({"matched":visaIssueDate.lower()+":"+val_ext4.lower()+"(100%)"})
                                                     metadataIdentified_dict.update({"conf":"100"})
                                                     match_ratio = match_ratio+20    
                                                     
                                                     
                                                 #if visaIssueDate.lower() in val_ext4.lower():
                                                    # metadataIdentified_dict.update({"Conf":"90"})    
                                                     
                                                 
                                                 if val_ext4 != "" and val_ext4 != "Not Found":
                                                     metadataIdentified_dict.update({"verdict":'Found'})
                                                     #match_ratio = match_ratio+10
                                                     
                                                 elif val_ext4 == "Not Found":
                                                     metadataIdentified_dict.update({"verdict":'Not Found'})
                                                
                                                 #print(metadataIdentified_dict)  
                                              
                                                 metadataIdentified.append(metadataIdentified_dict)
                                                 #metadataIdentified_dict = {}
                                                 temp_dict.update({"metadata":metadataIdentified})
                                              print("--- match Ratio ----") 
                                              print(match_ratio)
                                              print(value3[kk])
                                              if match_ratio>10:
                                                 compilation_shortlisted.append(key_ext)
                                          
                                    
                                  if match_flag == False:
                                     temp_dict.update({"documentName":"Not Found"})
                                  # else:
                                  #    print("--- match Ratio ----") 
                                  #    print(match_ratio)
                                  #    print(value3[kk])
                                  #    if match_ratio>10:
                                  #        compilation_shortlisted.append(val_ext3)
                          
                          doc_list.append(temp_dict)
                          temp_dict = {}
            final_res.update({"compilationstatus":"Success"})
            
            dest_path = "\\catorbmpfil11\\EganLLP H-Z\\RPA BOT Project - DO NOT USE\EY DataWarehouse KB Reivew\\INSZoom Database\\H1B Immigration Compilation Report\\CompiledOutput\\"
            final_res.update({"location":dest_path+case_id_for_compilation+"\\"+case_id_for_compilation+".pdf"})
            final_res.update({"Comment":"test"})               
        #print(value)
    final_res.update({"compilationOutput":doc_list})   
        
    #print(value)
    
#print(final_res)    

json_object = json.dumps(final_res, indent = 4)   
print("Json output for end point")
print("---------------------------")
print(json_object)

print("***************************")

print("shortlisted files for compilation")
print("---------------------------")
print(list(set(compilation_shortlisted))) 
#print(compilation_shortlisted)

# -- Compilation to one PDF

merger = PdfFileMerger()

compilation_shortlist = list(set(compilation_shortlisted))

        
print("---  compilation_shortlist ----")
print(compilation_shortlist)

for i in range(len(compilation_shortlist)):
    print(compilation_shortlist[i])
    merger.append("temp\\"+compilation_shortlist[i])

merger.write(case_id_for_compilation+".pdf")     
merger.close()








#print(final_res)

#payload = {'json_payload': final_res}

data = {'data': json.dumps(final_res)}

# import requests
# r = requests.post('https://cibapiqa.ey.com/api/AI/UpdateCaseCompilationOutput', json=json_object)
# print(r.status_code)

url = "https://cibapiqa.ey.com/api/AI/UpdateCaseCompilationOutput"
# headers={
    
#     'Accept' : 'application/json', 'Content-Type' : 'application/json', "Accept-Encoding": "gzip, deflate, sdch, br", "Accept-Language": "en-US,en;q=0.8", 'User-Agent': 'curl/7.47.1'
# }

#headers = {'Accept' : 'application/json', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36', 'Content-type': 'application/json', 'Accept': 'text/plain'}
#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

#headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.90 Safari/537.36'}

#headers = {'Content-Type' : 'application/json', 'Accept' : '*/*', 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


headers={
    'Referer': 'https://itunes.apple.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }



    # proxy_var=requests.session()
    # proxy_var.proxies={"http": "https://link@amweblink.net:00","https": "link",}
    # # It is a good practice not to hardcode the credentials. So ask the user to enter credentials at runtime
#response = requests.post(url, json = final_res, headers = headers)
#print(response.content)



# for key, value in checklist[0].items():
  
      
#       if key != "documentCheckList":
#           print(key)
#           print(value)
#           main_info_dict.update({key:value})
      
#       #print("main_info_dict")
#       #print(main_info_dict)    
#       if key == "documentCheckList":
      
#       if key == "documentCheckList":
          
#           checklist_index = checklist_index+1
#           checklist_item = "list"+str(checklist_index)
#           checklist_item = []     
         
#           #print(" --- DocumentCheckList --")
#           #print(value)
#           #print("-----------***---------")
          
#           print(len(value))
          
#           for i in range(len(value)):
#               #print("----------")
#               #print(value[i])
#               #print("----------")
              
#               new_dict = {}
#               new_list = []
              
#               for key3, value3 in value[i].items():
#                  if key3 != "requiredDocuments": 
#                    #print(key3)
#                    #print(value3)
#                    new_dict.update({key3:value3})
#                  elif key3 == "requiredDocuments":
#                    for i in range(len(value3)):
#                        #print("======")
#                        #print(value3[i])
#                        #print("======")
#                        new_list.append(value3[i])
              
#               #print("++++ new dict +++===")
#               #print(new_dict)
#               #print("--------")
#               #print(new_list)
#               #print("++++ new dict +++===")
              
              
#               checklist_item.append(new_dict)
#               checklist_item.append(new_list)
          
#           #print("pppp")
#           #print(checklist_item)
          
#               checklist_info.append(checklist_item)
#               checklist_item = []

# # print("---  Main Info-----")
# # print(main_info_dict)

# print("=== applicant list items ======")    
# print(checklist_info)  


# #print(len(checklist_info))

# file_list = []
# fields_list = []

# for i in range(len(checklist_info)):
#     #print(checklist_info[i])
#     print(len(checklist_info[i]))
#     #for k in range(len(checklist_info[i])):
#     print(checklist_info[i][0])
#     print("--------")
#     print(checklist_info[i][1])
#     for file_itmes in range(len(checklist_info[i][1])):
#         file_list.append(checklist_info[i][1][file_itmes])

# print("===== file_list ======")    
# print(file_list)


# matched_list = {}
# missing_list = []

# for i in range(len(file_list)):
    
#        match_flag = False 
#        for k in range(len(extracted)):
#            for key, val in extracted[k].items():
#                #if key == "DocType":
#                    #print(key)
#                    #print(".....")
                   
                   
                   
#                    for key_item, val_item in val.items():
#                        if key_item == "DocType":
#                            # print(val_item)
#                            # print(file_list[i])
#                            if val_item in file_list[i]:
#                                 # print("Matched")
#                                 # print(key)
#                                 # print(val_item)
#                                 match_flag = True
#                                 matched_list.update({val_item:key})
                                
#        if match_flag == False:
#            missing_list.append(file_list[i])                  




# print(matched_list)
# print(missing_list)



   
    
    
# for i in range(len(checklist)):
    
#     #name_of_applicant = case_info[i][0]['firstName']
   
#     print("Doc names")
#     for k in range(len(checklist[i][1])):
#         print(checklist[i][1][k])
#         doc_dict.update({"Document"+str(k+1):checklist[i][1][k]})
#     #checklist_dict.update({case_info[i][0]['applicantType']:doc_dict})    

















    
    
