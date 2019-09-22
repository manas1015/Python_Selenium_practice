
# selenium
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keyboard
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
#Python - inbuilt
import time

# user-module
from Data import TestData1 as td
import EnvConfig as env
from ObjectRepo import Locators as loc


driver = webdriver.Chrome(env.DriverPATH)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.toolsqa.com/selenium-webdriver/mouse-hover-action/")


time.sleep(2)

mouseHOver_Tut_link = driver.find_element_by_xpath(loc.MOuseHover_Tutorials_Link)
ac = ActionChains(driver)

ac.move_to_element(mouseHOver_Tut_link)
ac.perform()
about=driver.find_element_by_xpath(loc.About)
ac.move_to_element(about).perform()


face_book=driver.find_element_by_xpath(loc.facebook)
face_book.click()

# bodyOFToolsQA_com = driver.find_element_by_xpath("//body[contains(@class,'post-template')]")
# bodyOFToolsQA_com.send_keys(keyboard.PAGE_DOWN)
# bodyOFToolsQA_com.send_keys(keyboard.PAGE_DOWN)
#
# keyboard_AC =  ActionChains(driver)
# keyboard_AC.key_down(keyboard.CONTROL).send_keys('a').key_up(keyboard.CONTROL).perform()
# # keyboard_AC.



