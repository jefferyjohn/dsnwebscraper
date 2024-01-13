# import requests
import time 
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.common.by import By 
 
URL = "https://eyes.nasa.gov/dsn/dsn.html"
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 
driver.get(URL) 
time.sleep(3)

small_dishes = driver.find_elements(By.CSS_SELECTOR, "div[class*='figure small_dish'")

# print(driver.page_source)
# for elem in content:
#     test = driver.find_element(By.CSS_SELECTOR, "a[id*='spacecraft_0_2_0'")
#     print(test.accessible_name)
# # print(content)
# print(len(small_dishes))

for i in range(3):
    if i == 0:
        for j in range(5):
            temp = "spacecraft_" + str(i) + "_" + str(j+1)
            try:
                test = small_dishes[i+j].find_element(By.CSS_SELECTOR, f"a[id*={temp}]")
                # if test:
                print(test.accessible_name)
            except:
                print("No element found")
    else:
        for j in range(3):
            temp = "spacecraft_" + str(i) + "_" + str(j+1)
            try:
                test = small_dishes[5+3*(i-1)+j].find_element(By.CSS_SELECTOR, f"a[id*={temp}]")
                # if test:
                print(test.accessible_name)
            except:
                print("No element found")





            # temp = "spacecraft_" + str(i) + "_" + str(j+1)
            # try:
            #     test = small_dishes[5+3*(i-1)+j].find_elements(By.CSS_SELECTOR, f"div[id*={temp}]")
            #     print(len(test))
            #     for i in range(len(test)):
            #         print(f"a[id*={temp}_{i}]")
            #         item = test.find_element(By.CSS_SELECTOR, f"a[id*={temp}_{i}]")
            #         print(item.accessible_name)

            #     # if test:
                
            # except:
            #     print("No element found")
            

