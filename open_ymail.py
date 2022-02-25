from selenium import webdriver
import time

from webdriver_manager.chrome import ChromeDriverManager
# Initiate the browser
browser  = webdriver.Chrome(ChromeDriverManager().install())

browser.get("https://ymail.com")
time.sleep(2.3)
print("2.3 seconds have elapsed")
browser.find_element_by_class_name('fuji-button-link.fuji-button-inverted.signin').click();


yname = "francisco_ortiz1@yahoo.com"
ypassword = ""

time.sleep(2.5)
print("2.4 seconds have elapsed") 

browser.find_element_by_class_name("phone-no").send_keys(yname)
browser.find_element_by_id("login-signin").click()

time.sleep(2.5)
print("2.5 seconds have elapsed")  

browser.find_element_by_id("login-passwd").send_keys(ypassword)
browser.find_element_by_id("login-signin").click()

