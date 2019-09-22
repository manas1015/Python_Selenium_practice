from selenium import webdriver
import time
import unittest
import logging

class TestCase01(unittest.TestCase):

    logging.basicConfig(level= logging.DEBUG)
    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome(r"F:\Py browser engine\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://javatpoint.com")

    def test_javatpoint_tc01(self):
        self.driver.find_element_by_xpath("//a[text()='Programs']").click()
        self.driver.find_element_by_id("gsc-i-id1").send_keys("python")
        self.driver.find_element_by_xpath("(//button[contains(@class,'search')])[1]").click()

    def test_javatpoint_tc02(self):
        self.driver.find_element_by_xpath("//a[text()='Programs']").click()
        self.driver.find_element_by_xpath("//a[text()='Hindi100.com']").click()

    @classmethod
    def tearDownClass(self):
        time.sleep(4)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

