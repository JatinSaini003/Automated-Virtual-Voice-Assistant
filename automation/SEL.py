from selenium import webdriver
from time import *

path = "D:\\VS CODE\\Project\\main.py\\automation\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://www.Amazon.com")
sleep(5)
driver.close()
