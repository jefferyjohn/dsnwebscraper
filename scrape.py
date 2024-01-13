import requests

URL = "https://eyes.nasa.gov/dsn/dsn.html"
page = requests.get(URL)

print(page.text)

