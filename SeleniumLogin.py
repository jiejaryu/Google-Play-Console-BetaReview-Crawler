from selenium import webdriver
import time
import pandas as pd
from bs4 import BeautifulSoup
import os

# login google play console page
driver = webdriver.Chrome("chromedriver.exe")
driver.get("https://accounts.google.com/signin/v2/identifier?service=androiddeveloper&passive=1209600&continue=https%3A%2F%2Fplay.google.com%2Fapps%2Fpublish%2F%3Fhl%3Dzh-tw%26dev_acc%3D10596334177471237299%23AppListPlace&followup=https%3A%2F%2Fplay.google.com%2Fapps%2Fpublish%2F%3Fhl%3Dzh-tw%26dev_acc%3D10596334177471237299&hl=zh-tw&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
driver.find_element_by_name("identifier").send_keys("YOUR EMAIL") # your mail
driver.find_element_by_xpath("//*[@id='identifierNext']/span/span").click()
driver.implicitly_wait(4)
driver.find_element_by_name("password").send_keys("YOUR PASSWORD") # your password
time.sleep(3)
driver.find_element_by_xpath("//*[@id='passwordNext']/span/span").click()

#open beta review page
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/table/tbody[1]/tr/td[1]/div").click()
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/div[1]/div[1]/nav/ul/li[9]/button").click()
time.sleep(10)
driver.find_element_by_xpath("//*[@id='gwt-uid-2253']/ul/li[4]").click()

# get page html
driver.get("https://play.google.com/apps/publish/?hl=zh-tw&account=7711559340013331641#BetaFeedbackPlace:p=com.silvrlin.within&appid=4973651716943245306")
html = driver.page_source
print(driver.title)

# create html file
soup = BeautifulSoup(driver.page_source, "lxml")
fp = open("index.html", "w", encoding="utf8")
fp.write(soup.prettify())
print("寫入檔案index.html...")
fp.close()
driver.quit()

# go to next page
time.sleep(10)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/div[4]/div[2]/div[3]/div[4]/span[2]/div/button[2]").click()

