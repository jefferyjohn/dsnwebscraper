# import requests
import time 
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service as ChromeService 
from webdriver_manager.chrome import ChromeDriverManager 
 
URL = "https://eyes.nasa.gov/dsn/dsn.html"
 
driver = webdriver.Chrome(service=ChromeService( 
	ChromeDriverManager().install())) 
 
driver.get(URL) 
time.sleep(3)
 
print(driver.page_source)
