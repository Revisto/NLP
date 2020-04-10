
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import time
import random
File=open("API_KEY_.txt", "a+")
for i in range (100000):
    Path="C:\ChromeDriver2\chromedriver.exe"
    Drive = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
    Drive.get("https://app.text-mining.ir/account/register")
    SearchBox = Drive.find_element_by_name("Email")
    SearchBox.send_keys(str(random.randint(999999999999999999999,999999999999999999999999999999999999999999))+"@gmail.com")
    SearchBox.send_keys(Keys.ENTER)
    SearchBox = Drive.find_element_by_name("Password")
    SearchBox.send_keys("ThisIsABot123456789")
    SearchBox.send_keys(Keys.ENTER)
    SearchBox = Drive.find_element_by_name("ConfirmPassword")
    SearchBox.send_keys("ThisIsABot123456789")
    SearchBox.send_keys(Keys.ENTER)
    Drive.get("https://app.text-mining.ir/CustomerPanel/ApiKeys/Create")
    SearchBox=Drive.find_element_by_class_name("form-control")
    SearchBox.send_keys("1")
    SearchBox.send_keys(Keys.ENTER)
    SearchBox=Drive.find_element_by_xpath('//*[@id="listtable"]/tbody/tr[2]/td[2]/span').text
    print (SearchBox)
    File.write('"'+SearchBox+'"'+","+"\n")
    Drive.close()

File.close()