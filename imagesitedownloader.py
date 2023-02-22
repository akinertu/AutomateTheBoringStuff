#! python3
# imagesitedownloader.py #downloads bicycle images from flickr.com

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get('https://www.flickr.com/')
browser.maximize_window()
search = browser.find_element(By.ID, "search-field")
search.send_keys("bicycle")
search.send_keys(Keys.RETURN)

img = browser.find_element(By.CSS_SELECTOR, "img")
img.click()