from selenium import webdriver
import time
import DemoSite_Loc as Locator
import DemoSite_config as config

chrome = webdriver.Chrome(r'F:\Py browser engine\chromedriver_win32\chromedriver.exe')
chrome.maximize_window()
chrome.implicitly_wait(10)
chrome.get("https://www.javatpoint.com/")
# a=chrome.find_elements_by_xpath('//div[@class="ddsmoothmenu"]/ul/li/a')
# # print(a)
# for i in a:
#     print(i.text)
#     if i.text == 'SQL':
#         i.click()
#         print("Done")
#         chrome.fin
#     else:
#         print("Not clicked")


oListElements_xpath = "//ol[@class='points']/li/a"
listOfQuestionsElements = chrome.find_elements_by_xpath(oListElements_xpath)
for singleEle in listOfQuestionsElements:
    # print(singleEle.get_attribute('href')+": " +singleEle.text)
    print(singleEle.ge)




# chrome.get(config.APPURL)
#
# # clicking the check box
# chrome.find_element_by_id(Locator.Simple_checkBox_id).click()


[['react-native-google-maps',"3rd Aug - React Native Google Maps"],
 ["react-native-modal","3rd Aug - React Native Modal"],
 []]