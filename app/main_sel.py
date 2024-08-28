import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
fileds=["Name", "Designation", "Email"]
writer=None
file = open('document.csv','a')
writer=csv.writer(file)
writer.writerow(fileds)
    
        
driver = webdriver.Chrome()
def wait_for_text(by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element.text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

def extractor(url):
    count=0
    driver.get(url)
    name_text=""
    designation=""
    email=""
    while(name_text=="" or designation=="" or email==""):
        count+=1
        name_text=wait_for_text(By.XPATH, "/html/body/app-root/council-detail/section[2]/div/mat-card[2]/div/div/div/div[1]/div[2]/p[@class='anaContent']")
        designation=wait_for_text(By.XPATH, "/html/body/app-root/council-detail/section[2]/div/mat-card[2]/div/div/div/div[2]/div[2]/p[@class='anaContent']")
        email=wait_for_text(By.XPATH, "/html/body/app-root/council-detail/section[2]/div/mat-card[2]/div/div/div/div[3]/div[2]/p[@class='anaContent']")
        if(count==30):
            break
    fileds=[name_text, designation,email]
    writer.writerow(fileds)        



import requests
import certifi
import json
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class InstituteDetails:
    userId: str
    instituteName: str
    stateName: str
    instituteCity: str
    instituteZone: str
    annual_report: Optional[str] 

@dataclass
class Response:
    message: str
    instituteDetails: List[InstituteDetails]

url = "https://iicapi.mic.gov.in/api/getApprovedInstitute?per_page=13186"
payload = {}
headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.request("POST", url, headers=headers, data=payload,verify=False)
response=response.json()
institute_data = [
    InstituteDetails(**institute) 
    for institute in response["instituteDetails"]["data"]
]
college_num=10312
for i  in range(10312,13185):
    print(college_num)
    institute=institute_data[i]
    print(f"User ID: {institute.userId}")
    urrl=f"https://iic.mic.gov.in/council-detail/{institute.userId}"
    extractor(urrl)
    college_num+=1
driver.quit()    
