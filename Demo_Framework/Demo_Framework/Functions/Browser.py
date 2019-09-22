from selenium import webdriver

import Testconfig as env
from selenium.webdriver.chrome.options import Options
# x=Options

# x.add_argument("--incognito")
class BrowserActions:
    x=Options()
    x.add_argument("--incognito")
    def __init__(self):
        print("Browser actions inti")

    def launch_application(self,typeOfBrowser):
        if typeOfBrowser == 'chrome':
            someDriver = webdriver.Chrome(env.Chrome_DriverPATH,options=self.x)
        elif typeOfBrowser == 'firefox':
            someDriver = webdriver.Firefox(env.Firefox_DriverPATH)
        else:
            someDriver = webdriver.Ie(env.IE_DriverPATH)
        someDriver.get(env.AppURL)
        someDriver.maximize_window()
        someDriver.implicitly_wait(10)
        return someDriver

    def quitBrowser(driver):
        driver.quit()
