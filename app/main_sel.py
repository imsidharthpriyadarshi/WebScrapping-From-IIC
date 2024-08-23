import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
url="https://iic.mic.gov.in/council-detail/IC202431360"
os.environ['MOZ_HEADLESS']='1'
driver = webdriver.Firefox()

driver.get(url)


def wait_for_text(by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return element.text
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None


name_text=""
designation=""
email=""
while(name_text=="" or designation=="" or email==""):
    name_text=wait_for_text(By.XPATH, "/html/body/app-root/council-detail/section[2]/div/mat-card[2]/div/div/div/div[1]/div[2]/p[@class='anaContent']")
    designation=wait_for_text(By.XPATH, "/html/body/app-root/council-detail/section[2]/div/mat-card[2]/div/div/div/div[2]/div[2]/p[@class='anaContent']")
    email=wait_for_text(By.XPATH, "/html/body/app-root/council-detail/section[2]/div/mat-card[2]/div/div/div/div[3]/div[2]/p[@class='anaContent']")


print(name_text)  
print(designation)
print(email)  

driver.quit()








