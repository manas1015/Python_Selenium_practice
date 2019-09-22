from selenium import webdriver
import time
import Locators1

chrome = webdriver.Chrome(r'F:\Py browser engine\chromedriver_win32\chromedriver.exe')
chrome.maximize_window()
chrome.implicitly_wait(10)
chrome.get("https://moneycontrol.com")

# homeText = chrome.find_element_by_xpath('(//a[@href="https://www.moneycontrol.com/"])[1]').text
# print(homeText)
#
listOfText = chrome.find_element_by_xpath(Locators1.ListOfMenuButtons).text
# print(listOfText.split())
print(listOfText)

listOfElements = chrome.find_elements_by_xpath(Locators1.ListOfElementsINMenuButton)
for singleELe in listOfElements:
    if singleELe.text == "Insurance":
        singleELe.click()

