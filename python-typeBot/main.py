from selenium import webdriver
import os
import time

number = '09360559427'
password = 'smo1383'


driver = webdriver.Chrome('chromedriver.exe')

def app():
    driver.get('http://typeiran.com/login')
    time.sleep(5)
    number_login = driver.find_element_by_css_selector('#CheckMobileFormMobile')
    number_login.send_keys(number)
    time.sleep(15)
    login_button1 = driver.find_element_by_css_selector('#CheckMobileFormBtnContinue')
    login_button1.click()
    time.sleep(5)
    password_login = driver.find_element_by_css_selector('#formLoginPassword')
    password_login.send_keys(password)
    login_button2 = driver.find_element_by_css_selector('#formLoginBtnLogin')
    login_button2.click()
    time.sleep(10)
    driver.get('http://typeiran.com/speed?lang=English')
    time.sleep(5)
    con = True
    i = 1
    while con == True:
        try:
            word = driver.find_element_by_css_selector('#word-{}'.format(i)).text
            input_text = driver.find_element_by_css_selector('#textbox')
            input_text.send_keys(word)
            input_text.send_keys(' ')
        except:
            con = False
        i = i+1
app()