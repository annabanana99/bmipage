from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium import webdriver

def before_all(context):
    binary = FirefoxBinary(
        "C:\\Program Files\\Mozilla Firefox\\firefox.exe")
    context.driver = webdriver.Firefox(firefox_binary=binary)
    context.driver.maximize_window()
    context.driver.implicitly_wait(15)

def after_all(context):
    context.driver.close()
