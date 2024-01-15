# import requests
import time 
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import initialize_app, credentials
import os

# Set the current working directory to the directory of this script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Use a service account
cred = credentials.Certificate('lark-leaderboard-firebase-adminsdk-uqcox-f780cfe004.json')
initialize_app(cred)

db = firestore.client()

def send_to_firestore(data):
    doc_ref = db.collection(u'dsnwebscraper').document()
    data['timestamp'] = datetime.now()
    doc_ref.set(data)

 
variables = ['NAME', 'RANGE', 'ROUND-TRIP LIGHT TIME', 'NAME', 'AZIMUTH', 'ELEVATION', 'WIND SPEED', 'MODE', 'SOURCE', 'FREQUENCY BAND', 'DATA RATE', 'POWER RECEIVED']

res = dict.fromkeys(variables, 0)


URL = "https://eyes.nasa.gov/dsn/dsn.html"
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 

driver.implicitly_wait(3)

driver.get(URL) 
time.sleep(3)


small_dishes = driver.find_elements(By.CSS_SELECTOR, "div[class*='figure small_dish'")

for i in range(3):
    # --------------------------------- first row -------------------------------- #
    if i == 0:
        for j in range(5):
            temporary = "spacecraft_" + str(i) + "_" + str(j+1) #this should look like "spacecraft_0_1"
            try:
                spacecraft_div = small_dishes[i+j].find_element(By.CSS_SELECTOR, f"div[id*={temporary}]")
                actual_title = spacecraft_div.find_elements(By.CSS_SELECTOR, f"a[id*={temporary}]")

                for item in range(len(actual_title)): #if there are multiple items in the list
                    if actual_title[item].accessible_name == "APM1":
                        if actual_title[item].get_attribute("class") != "selected":
                            driver.find_element(By.CSS_SELECTOR, f"a[id*={temporary}_{item}]").click()
                        driver.find_element(By.CSS_SELECTOR, f"a[title*='more detail']").click()
                        sidebar = driver.find_element(By.CSS_SELECTOR, "div[id*='current_data']")
                        values = sidebar.find_elements(By.TAG_NAME, 'p')
                        for e in range(len(values)):
                            res[variables[e]] = values[e].text
                            # print(res[variables[e]])
                            print(values[e].text)
                        print(res)
                        break
            except:
                print("No element found")
    # ----------------------------- for rows 2 and 3 ----------------------------- #
    else:
        for j in range(3):
            temporary = "spacecraft_" + str(i) + "_" + str(j+1) #this should look like "spacecraft_0_1"
            try:
                spacecraft_div = small_dishes[5+3*(i-1)+j].find_element(By.CSS_SELECTOR, f"div[id*={temporary}]")
                actual_title = spacecraft_div.find_elements(By.CSS_SELECTOR, f"a[id*={temporary}]")

                for item in range(len(actual_title)): #if there are multiple items in the list
                    if actual_title[item].accessible_name == "APM1":
                        if actual_title[item].get_attribute("class") != "selected":
                            driver.find_element(By.CSS_SELECTOR, f"a[id*={temporary}_{item}]").click()
                        driver.find_element(By.CSS_SELECTOR, f"a[title*='more detail']").click()
                        sidebar = driver.find_element(By.CSS_SELECTOR, "div[id*='current_data']")
                        values = sidebar.find_elements(By.TAG_NAME, 'p')
                        for e in range(len(values)):
                            res[variables[e]] = values[e].text
                            # print(res[variables[e]])
                            print(values[e].text)
                        print(res)
		        send_to_firestore(res)

			
                        break
            except:
                print("No element found")



