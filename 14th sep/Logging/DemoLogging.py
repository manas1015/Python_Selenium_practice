import logging

from selenium import webdriver
import time

logging.basicConfig(level = logging.DEBUG)

driver = webdriver.Chrome(r"F:\Py browser engine\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("http://javatpoint.com")
driver.find_element_by_xpath("//a[text()='Programs']").click()

driver.find_element_by_id("gsc-i-id1").send_keys("python")

driver.find_element_by_xpath("(//button[contains(@class,'search')])[1]").click()

time.sleep(4)

# driver.quit()

