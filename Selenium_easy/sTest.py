from selenium import webdriver
import time
import slocators
import sconfig
selenium_automation=webdriver.Chrome(r'F:\Py browser engine\chromedriver_win32\chromedriver.exe')
selenium_automation.maximize_window()
selenium_automation.get(sconfig.app_url)
selenium_dropdown=selenium_automation.find_element_by_xpath(slocators.selenium_dropdown).click()
selenium_automation.implicitly_wait(30)
selenium_with_python=selenium_automation.find_element_by_xpath(slocators.selenium_with_python).click()
# Fb=selenium_automation.find_element_by_xpath(slocators.FB).click()
time.sleep(5)
search=selenium_automation.find_element_by_xpath(slocators.search).click()