from selenium import webdriver
import time
import unittest
import logging


class TestCase02(unittest.TestCase):
    logging.basicConfig(level=logging.DEBUG)

    def setUp(self):
        self.driver = webdriver.Chrome(r"F:\Py browser engine\chromedriver_win32\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("http://javatpoint.com")



    def test_javatpoint_tc02(self):
        self.driver.find_element_by_xpath("//a[text()='Programs']").click()
        self.driver.find_element_by_xpath("//a[text()='Hindi100.com']").click()


    def tearDown(self):
        time.sleep(4)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

