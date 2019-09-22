from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
driver_path= r'F:\Py browser engine\chromedriver_win32\chromedriver.exe'

from selenium.webdriver.chrome.options import Options
options=Options()
options.headless=True
driver=webdriver.Chrome(driver_path,options=options)
driver.get("http://google.com")
print(driver.title)
inputBox=driver.find_element_by_xpath("//input[@name='q']")
inputBox.send_keys("Map of India")

driver.save_screenshot(r"C:\Users\admin\PycharmProjects\Guru99_registration\screen_snaps\map_india.png")
driver.quit()