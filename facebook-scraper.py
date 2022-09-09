import time
import json
 
from lib2to3.pgen2.driver import Driver
from selenium import webdriver


f = open('data.json')
data = json.load(f)
facebookpwd = data["facebook-pwd"]
email = data["email"]
message = data["message"]
f.close()

driver = webdriver.Chrome()

driver.get("https://facebook.com")

driver.find_element("id","email").send_keys(email)
driver.find_element("id","pass").send_keys(facebookpwd)

driver.find_element("name","login").click()
time.sleep(3)
driver.get("https://facebook.com")
time.sleep(2)
driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span').click()
time.sleep(2)
driver.find_element("xpath",'/html/body/div[1]/div/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div/p').send_keys(message)
driver.close()
    