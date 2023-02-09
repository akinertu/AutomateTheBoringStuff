from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://nardisjazz.com/')
linkElem = browser.find_element("class", 'evcal_desc2 evcal_event_title')
type(linkElem)
linkElem.click()