from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from dateutil.relativedelta import relativedelta
from selenium.webdriver.chrome.options import Options


def todayDate(days_plus):
    now = datetime.datetime.now()
    days_ahead = (datetime.datetime.now() + relativedelta(days=days_plus)).strftime('%m-%d-%Y').replace("-", "/")
    #print (days_ahead)
    return(days_ahead)


def login():
    login = driver.find_element_by_link_text("Log In").click()
    time.sleep(1)

    watiam = driver.find_element_by_xpath('//*[@id="divLoginOptions"]/div[2]/div[2]/div/button').click()

    userName = driver.find_element_by_id("userNameInput")
    userName.send_keys("user name here")
    userName.send_keys(Keys.RETURN)

    password = driver.find_element_by_id("passwordInput")
    password.send_keys("password here")
    password.send_keys(Keys.RETURN)
    time.sleep(1)


def selectProgram():
    bar = driver.find_elements_by_xpath("//button[@class = 'btn btn-primary pull-left']")
    time.sleep(1)
    bar[len(bar) - 1].click()
    time.sleep(1)


def accept():
    accept = driver.find_element_by_id("btnAccept").click()
    time.sleep(1)


def noAddCart():
    noButton = driver.find_elements_by_id("rbtnNo")

    for i in range(8):
        noButton[i].click()

    addCart = driver.find_element_by_xpath("//*[@id='mainContent']/div[2]/form[2]/div[2]/button[2]").click()
    time.sleep(1)


def lastStep():
    checkout = driver.find_element_by_id("checkoutButton").click()
    time.sleep(1)
    finish = driver.find_element_by_xpath('//*[@id="CheckoutModal"]/div/div[3]/button[2]').click()


PATH = "C:\Program Files (x86)\chromedriver.exe"
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(PATH, options=chrome_options)
#driver = webdriver.Chrome(PATH)


driver.get("https://warrior.uwaterloo.ca/Program/GetProgramDetails?courseId=cc2a16d7-f148-461e-831d-7d4659726dd1&semesterId=b0d461c3-71ea-458e-b150-134678037221")

login()
todayDate(5)
selectProgram()
accept()
noAddCart()
lastStep()
driver.quit()