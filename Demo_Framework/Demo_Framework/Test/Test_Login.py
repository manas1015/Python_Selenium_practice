

from Functions import Browser
from Functions import Business
from Data import TestData1 as td
# from selenium.webdriver.chrome.options import Options
# x=Options
# x.add_argument("--incognito")

browser_action = Browser.BrowserActions()

business_action = Business.BusinessActions()

driver = browser_action.launch_application("chrome")
business_action.login(driver, td.InitialEmailID)
business_action.Name(driver,td.First_Name,td.Last_Name)
business_action.Address(driver,td.Email,td.phone,td.address,gender=" ",hobbies=" ")
business_action.LSCC(driver,lang=" ",skill=" ",country=" ",Scountry=" ")
business_action.DOB(driver,year=" ",month=" ",day=" ")
business_action.submit(driver,pwd=" ",conf_pwd=" ")

# Browser.BrowserActions.quitBrowser(driver)