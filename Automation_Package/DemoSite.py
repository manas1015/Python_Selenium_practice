from selenium import webdriver
import time
import DemoSite_Loc as Locator
import DemoSite_config as config

chrome = webdriver.Chrome(config.DriverPath)
chrome.maximize_window()
chrome.implicitly_wait(config.Default_ImplicitWaitTimeOUT)
chrome.get(config.APPURL)

# clicking the check box
chrome.find_element_by_id(Locator.Simple_checkBox_id).click()


chrome.find_element_by_xpath("//label[text()='Option 2']/input").click()

