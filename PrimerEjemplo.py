from selenium import webdriver
from selenium.webdriver.chrome.service import Service


PATH = "C:\ChromeDriver\chromedriver.exe" # el path para google chrome
PATH = "C:\geckodriver-v0.31.0-win64.zip\geckodriver.exe" # el path para google firefox

s = Service(PATH)
driver = webdriver.Chrome(service=s)
driver.get ("https://demoqa.com/text-box")

print("Bienvenido a Selenium")
print(driver.title)
driver.close()

