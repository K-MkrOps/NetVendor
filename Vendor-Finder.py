#!/usr/bin/env python3
import os
import sys
import csv
import time
import subprocess
import json

#if the library requests is not installed, install it via pip
try:
    import requests
except ImportError:
    print("[!] The requests library is not installed. Installing...")
    os.system("pip install requests")
    print("[+] The requests library has been installed.")
    time.sleep(1)
    import requests

time.sleep(1)
from jsondb.db import Database

OUI_list = [] 
OUI_list_final = []
company_list =[]
company_list_final = []

#Show the contents of the current directory
print("\nPlease select the #SH IP ARP Data text file from the current directory\n")
print(os.listdir(), "\n")

#while the file name is not valid, ask the user to input the file name again
while True:
    ip_arp_file = input("Please enter the file name: ")
    if os.path.isfile(ip_arp_file):
        break
    else:
        print("\nThe file name is not valid, please try again\n")

with open(ip_arp_file, 'r') as f:
        for line in f:
            #split the line into words
            words = line.split()
            #send words[2] to a list
            MAC_Element = words[2]
            #copy the first 7 characters to a new list called OUI_list
            OUI_ELEMENT= MAC_Element[0:7]
            #split oui_list into different elements
            OUI_ELEMENT = OUI_ELEMENT.split()
            #append OUI_ELEMENT to a list called OUI_list
            OUI_list.append(OUI_ELEMENT)

#sort OUI_list
OUI_list.sort()

#compare each element to the previous element, if the element is different, print the element
for i in range(len(OUI_list)):
    if OUI_list[i] != OUI_list[i-1]:
        #save each different element to a new list called OUI_list_final
        OUI_list_final.append(OUI_list[i])

#save oui list final to a file called oui_list_final.txt
with open('oui_list_final.txt', 'w') as f:
    for i in range(len(OUI_list_final)):
        f.write(OUI_list_final[i][0] + '\n')

#close the file
f.close()

#Check each line of the file oui_list_final.txt if it is 'MAC' delete it
with open('oui_list_final.txt', 'r') as f:
    lines = f.readlines()
with open('oui_list_final.txt', 'w') as f:
    for line in lines:
        if line.strip("\n") != 'MAC':
            f.write(line)
#close the file
f.close()

#Check each line of the file oui_list_final.txt if it is 'INCOMPL' delete it
with open('oui_list_final.txt', 'r') as f:
    lines = f.readlines()
with open('oui_list_final.txt', 'w') as f:
    for line in lines:
        if line.strip("\n") != 'INCOMPL':
            f.write(line)

#close the file
f.close()

#print please be patient the vendor information is being retrieved
print("\nPlease be patient, the vendor information is being retrieved\n")

#for each line in the file oui_list_final.txt, store this in a list called vendor_list
vendor_list = []
with open('oui_list_final.txt', 'r') as f:
    for line in f:
        vendor_list.append(line)

#for each element in vendor_list do a request to the OUI database
for i in range(len(vendor_list)):
    r = requests.get("https://macvendors.co/api/" + vendor_list[i])
    #if the request is successful, print the vendor name
    if r.status_code == 200:
        print(".", end="")
        #save the vendor name to a file called vendor_list.txt
        with open('raw_vendor_list.json', 'a') as f:
            f.write(r.text + '\n')
    #else if the request is not successful, print the error message
    else:
        print("\nError:", r.status_code, r.reason)

#close the file
f.close()

#Check each line of the file vendor_list.txt if it is "{"result":{"error":"no result"}}" delete it

with open('raw_vendor_list.json', 'r') as f:
    lines = f.readlines()
with open('raw_vendor_list.json', 'w') as f:
  for line in lines:
      if line.strip("\n") != '{\"result\":{\"error\":\"no result\"}}':
          f.write(line)

#close the file
f.close()

time.sleep(1)

def loads(txt):
    txt = txt.encode("utf-8")
    value = json.loads(txt)

    return value

#open the json file raw_vendor_list.json and read it, look for company name
with open('raw_vendor_list.json', 'r') as f:
    for line in f:
        #load the json file
        data = loads(line)
        #get the company name
        company = data['result']['company']
        #append the company name to a list called company_list
        company_list.append(company)

#close the file
f.close()

#sort company_list
company_list.sort()

#compare each element to the previous element, if the element is different, print the element
for i in range(len(company_list)):
    if company_list[i] != company_list[i-1]:
        #save each different element to a new list called OUI_list_final
        company_list_final.append(company_list[i])

print("\n\nThe Companies seen in the <<# sh ip arp>> data file are:\n")

#save the company list final to a file called company_list.txt
with open('company_list.txt', 'w') as f:
    for i in range(len(company_list_final)):
        f.write(company_list_final[i] + '\n')

#print the list company_list one element a t time
for i in range(len(company_list_final)):
    print(company_list_final[i])

#count the lines in the file oui_list_final.txt and print the number of lines
with open('oui_list_final.txt', 'r') as f:
    count = 0
    for line in f:
        count += 1
    print("\n\nThere are", count, "different OUIs in the", ip_arp_file, "file\n")

#close the files
f.close()

print(">>> Please see the oui_list_final.txt file in the current directory for the list of OUIs\n")
print(">>> Please see the company_list.txt file in the current directory for the list of companies seen\n")

#tell the user to press enter to quit
input("\nPress enter to quit: ")
#exit the program
sys.exit()





        