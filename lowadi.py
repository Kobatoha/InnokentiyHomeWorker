import os
import random
from datetime import datetime
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json


def newDR():
    chromeOptions = uc.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  # normal - full_load
    chromeOptions.add_argument("--single-process")
    chromeOptions.headless = False
    driver = uc.Chrome(options=chromeOptions, desired_capabilities=caps)
    return (driver)


def login_lowadi():
    url = 'https://www.lowadi.com'

    driver.get(url)

    driver.find_element(By.XPATH, '//*[@id="65e8b87c774cfaccept"]/button').click()

    driver.find_element(By.XPATH, '//*[@id="header-login-label"]').click()
    login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
    password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
    connect = driver.find_element(By.XPATH, '//*[@id="authentificationSubmit"]').click()
    try:
        if driver.find_element(By.XPATH, '//*[@id="Ufo_0"]'):
            if driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').children()[0].get_attribute('id') in ['65e8b9d2c19d8']:
                print(f'НЛО: экю, надо скипнуть')
                driver.get(url)
            elif driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').children()[0].get_attribute('id') in ['65e8bd83be647']:
                print(f'НЛО: 2 орки, надо ловить')
                driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').click()
                driver.find_element(By.XPATH, '//*[@id="agi-10972849001709751854"]').click()

    except:
        pass


def work_hourse():
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=19637945'
    driver.get(url)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    carrot = driver.find_element(By.XPATH, '//*[@id="boutonCarotte"]').click()
    mash = driver.find_element(By.XPATH, '//*[@id="boutonMash"]').click()
    pat = driver.find_element(By.XPATH, '//*[@id="boutonCaresser"]').click()
    


driver = newDR()
driver.set_window_size(1900, 1000)




