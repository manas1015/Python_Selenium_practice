from selenium import webdriver
import time
from Data import TestData1 as td
import EnvConfig as env
from ObjectRepo import Locators as loc
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(env.DriverPATH)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/droppable/")

time.sleep(3)
myFrame = driver.find_element_by_xpath(loc.JqueryUI_Frame)
driver.switch_to.frame(myFrame)

draggable_text_element = driver.find_element_by_id(loc.Drag_Draggable)
# draggable_text = draggable_text_element.text
# print(draggable_text)
droppable_Element = driver.find_element_by_id(loc.Drag_Dropable)

actionChains = ActionChains(driver)
actionChains.drag_and_drop(draggable_text_element,droppable_Element).perform()
driver.switch_to.default_content()
search=driver.find_element_by_xpath(loc.search).click()

# driver.refresh()
# driver.back()
# driver.forward()
#
# time.sleep(2)
#
# mouseHover_Element = driver.find_element_by_xpath(loc.MouseHover_Image)
#
# mouseHover_AC = ActionChains(driver)
# mouseHover_AC.move_to_element(mouseHover_Element)
# mouseHover_AC.perform()