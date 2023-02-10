from selenium import webdriver
from selenium.webdriver.common.by import By
import time
browser = webdriver.Chrome()
browser.get('https://www.clickspeedtester.com/clicks-per-second-test/')
userElem = browser.find_element(By.ID, "clickButton")

for i in range(100):
    userElem.click()
    
