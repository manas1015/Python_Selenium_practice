from selenium import  webdriver
from selenium.webdriver.common.keys import Keys as keyBoard
import time
from selenium.webdriver.chrome.options import Options

PROXY = "127.0.0.1:8080"
x = Options()
x.headless = False
x.add_argument("--incognito")
x.add_argument("start-maximized")
# x.add_argument('--proxy-server=%s' % PROXY)
driver = webdriver.Chrome(r'F:\Py browser engine\chromedriver_win32\chromedriver.exe',options=x)
driver.get("https://www.snapdeal.com/search?keyword=football&santizedKeyword=&catId=&categoryId=0&suggested=false&vertical=&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy")

driver.find_element_by_xpath("(//img[@class='product-image '])[1]").click()

listOfWindows = driver.window_handles
for singleWindow in listOfWindows:
    if singleWindow != driver.current_window_handle:
        driver.switch_to.window(singleWindow)

driver.find_element_by_xpath("//span[@class='intialtext' and text()='add to cart']").click()

# driver.switch_to.window(idsOfWindow[0])

# driver.find_element_by_xpath("//*[@id='view-more-parent-cat']").click()
