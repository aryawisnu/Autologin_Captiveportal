from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import http.client

#website
website_link="**ur login portal link**"
#login username
username="**ur username**"
#login password
password="**urpassword**"
#data
httpresponse = ""
connectionstatus = ""

def checkcaptiveportal():
    global httpresponse
    global connectionstatus

    try:
        connection = http.client.HTTPConnection("www.google.com")
        connection.request("GET", "/")
        response = connection.getresponse()
        httpresponse = response.status
        connection.close()
        connectionstatus = True

    except :
        print("No internet connection")
        connectionstatus = False

def autologin():
    print("Loaded driver...")
    browser = webdriver.Chrome("/usr/bin/chromedriver")
    browser.get((website_link))	

    try:
        print("Driver loaded successfully")
        username_element = browser.find_element(By.NAME, 'une')
        username_element.send_keys(username)		
        print("Username entered")
        password_element  = browser.find_element(By.NAME, 'pass')
        password_element.send_keys(password)
        print("Password entered")
        signInButton = browser.find_element(By.ID, 'password_disclaimer')
        signInButton.click()
        print("Disclaimer Check")
        signInButton = browser.find_element(By.ID, 'password_submitBtn')
        signInButton.click()
        print("Login Successfully")
        time.sleep(3)
        browser.quit()
        time.sleep(1)
        browserExe = "Chrome"
        os.system("pkill "+browserExe)
    except Exception:
        print("Some error occured :(")
        browser.quit()
        browserExe = "Chrome"
        os.system("pkill "+browserExe)

checkcaptiveportal()
print("Response: ", httpresponse)
if httpresponse != 200 and connectionstatus :
    print("login")
    autologin()
else :
    print("x_x")
