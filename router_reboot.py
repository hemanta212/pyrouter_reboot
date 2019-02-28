import time
from selenium import webdriver
from win_notify import balloon_tip as winnotifier


def setup(incognito=False):
    global browser
    if incognito:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--headless")
        browser = webdriver.Chrome(options=chrome_options)
    else:
        browser = webdriver.Chrome()

def authenticate(
        router_user, router_pass, element_name="username",
        element_password="userpass", button_onclick='return saveChanges()'):

    browser.get("http://192.168.1.1/login.htm")
    username = browser.find_element_by_name(element_name)
    password = browser.find_element_by_name(element_password)
    username.send_keys(router_user)
    password.send_keys(router_pass)
    browser.find_element_by_css_selector("input[onclick*='return saveChanges()']").click()

def reboot():
    browser.get("http://192.168.1.1/reboot.htm")
    time.sleep(1)
    browser.find_element_by_css_selector("input[onclick*='return rebootClick()']").click()
    alert_obj = browser.switch_to.alert
    time.sleep(2)
    alert_obj.accept()
    winnotifier("sharmaji: Wifi rebooted",\
     "TOTOLINK succesfully has been rebooted wait for 10-15 secs")
    time.sleep(3)
    browser.close()

setup(incognito=True)
try:
    authenticate("admin", "admin")
    reboot()
except:
    reboot()
