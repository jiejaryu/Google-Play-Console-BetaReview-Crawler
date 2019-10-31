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
time.sleep(5)
driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/table/tbody[1]/tr/td[1]/div").click()
time.sleep(5)
driver.get("YOUR BETA REVIEW PAGE URL") # the url of your beta review page
time.sleep(5)
print(driver.title) #check current page

# get page html
html = driver.page_source

# create html file
soup = BeautifulSoup(driver.page_source, "lxml")
fp = open("index.html", "w", encoding="utf8")
fp.write(soup.prettify())
print("Writing File index.html...")
fp.close()
driver.quit()

### get local html file content
soup = BeautifulSoup(open("index.html"),'lxml')
#print(soup)


### get user name
user_names = soup.select('span.GNVPVGB-Bn-j strong')
nameList= []
for name in user_names:
    nameList = nameList + [name.string.strip()]

print(nameList)


### get user rating
userRatings = soup.find_all("div", class_ = "GNVPVGB-Yn-b GNVPVGB-md-m")

reviewList= []
for review in userRatings:
    reviewList = reviewList + [review['aria-label']]

print(reviewList)


### get rating time

ratingTime = soup.select('span.GNVPVGB-rn-j')

timeList = []
for time in ratingTime:
    timeList = timeList + [time.text.strip()]

print(timeList)



# # go to next page -> will do this function later
# time.sleep(10)
# driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div/div[2]/div/div[3]/div/div[2]/div/div[1]/div/div/div[2]/div/section/div[4]/div[2]/div[3]/div[4]/span[2]/div/button[2]").click()

