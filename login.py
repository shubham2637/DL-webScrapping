from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
import matplotlib.pyplot as plt

capatcha_path = "\\captacha\\1.png"
import cv2
from get_capcha import get_captcha


def get_capcha():
    capatchaID = input("Enter capcha")


def input_data():
    dl_number = input("Enter the DL number")
    dob = input("Enter Date of birth")
    # input_data = [dl_number,dob]
    # return input_data
    return [dl_number, dob]


chromedriver_path = 'E:\insta\chromedriver.exe'  # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path)
sleep(2)
webdriver.get(' https://parivahan.gov.in/rcdlstatus/?pur_cd=101')
sleep(3)
DLno_value = webdriver.find_element_by_css_selector('#form_rcdl\:tf_dlNO')
dob_value = webdriver.find_element_by_css_selector('#form_rcdl\:tf_dob_input')
capatcha_value = webdriver.find_element_by_css_selector('#form_rcdl\:j_idt34\:CaptchaID')
capatcha_image = webdriver.find_element_by_css_selector('#form_rcdl\:j_idt34\:j_idt41')
check_status_button = webdriver.find_element_by_css_selector('#form_rcdl\:j_idt46 > span')
data = input_data()

# comment out below lines
DLno = "DL-0420110149646"
dob = "09-02-1976"
data = [DLno, dob]
# till here
DLno_value.send_keys(data[0])
dob_value.send_keys(data[1])
# function call
# cap = str(get_capcha())
cap = input("Captcha : ")
capatcha_value.send_keys(cap)
check_status_button.click()
print("Login successful")
# webdriver.close()
