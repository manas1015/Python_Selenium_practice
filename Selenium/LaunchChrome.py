from selenium import webdriver
# import time
#
# APPLICATION_UNDER_TEST = "https://www.facebook.com"
# CHROMEDRIVER_PATH = r'Z:\drivers\chromedriver_win32\chromedriver.exe'
# # APPLICATION_UNDER_TEST_Dict = {
#    #"facebook":'http://facebook.com',
# #     'JournalDev':'http://journaldev.com'
# # }
#
# list = [['facebook', 'http://facebook.com'],['JournalDev','http://journaldev.com']]
#
# CBA = webdriver.Chrome(CHROMEDRIVER_PATH)
#
# print(list[0][1])
# # CBA.get(list[0][1])
# # CBA.maximize_window()
# #
# # ExpectedTitle = 'facebook'
# #
# # ActualTitle = CBA.title
# # print(ActualTitle)
# # if ExpectedTitle in ActualTitle:
# #     print("Test Passed")
# # else:
# #     print("Test Failed")
#
#
# '''
# # prereq
# # 1. Python
# # 2. ChromeBrowser
# # 3. Application Under test --> google.com
# # 4. Selenium library --> pip / package module
# # 5. Browser engine
#
#
# '''
#
#
# time.sleep(3)
# CBA.quit()
#
#

from selenium import webdriver
import time
varAutomation = webdriver.Chrome(r'F:\Py browser engine\chromedriver_win32\chromedriver.exe')
varAutomation.maximize_window()
varAutomation.get("https://accounts.google.com")

# automation.set_window_size(1000,600)
title = varAutomation.title
print(title)



varPageSource = varAutomation.page_source

if 'kRoyt MbhUzd' in varPageSource:
    print("passed")
else:
    print("failed")
time.sleep(3)
varAutomation.quit()