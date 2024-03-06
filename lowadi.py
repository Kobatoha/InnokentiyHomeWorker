import os
import random
from datetime import datetime
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from os import getenv


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
    login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(getenv("login"))
    password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(getenv("password"))
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
    while driver.find_element(
            By.XPATH,
            '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
    ).get_attribute('href') != 'https://www.lowadi.com/elevage/chevaux/cheval?id=19637945':
        try:
            clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
            time.sleep(1)
            food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
            time.sleep(1)
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[13]').click()
            time.sleep(1)
            get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
            time.sleep(1)
            sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
            time.sleep(1)
            lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
            time.sleep(1)
            driver.find_element(By.XPATH, '//*[@id="title-genetics"]').click()
            gp = int(driver.find_element(By.XPATH, '//*[@id="genetic-body-content"]/table[1]/tbody/tr[1]/td[3]').text[6:-3])
            if gp > 18000:
                print(f'Хороший ГП, можно качать')

            if 'кобыла' in driver.find_element(
                    By.XPATH,
                    '//*[@id="characteristics-body-content"]/table/tbody/tr[3]/td[1]').text:
                if driver.find_element(By.XPATH, '//*[@id="reproduction-body-content"]/div[1]/table/tbody/tr[1]/td'):
                    text = driver.find_element(
                        By.XPATH,
                        '//*[@id="reproduction-body-content"]/div[1]/table/tbody/tr[1]/td'
                    ).text
                    print(text)
                    next_hourse = driver.find_element(By.XPATH, '//*[@id="nav-next"]').click()
                elif driver.find_element(By.XPATH, '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]/a').text == 'Случить кобылу':
                    driver.find_element(By.XPATH, '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]/a').click()
                    time.sleep(1)
                    master = driver.find_element(By.XPATH, '//*[@id="breeder"]').send_keys('Kolgotki')
                    get_offers = driver.find_element(By.XPATH, '//*[@id="agi-40386814001709756394"]/button[1]').click()
                    price_sort = driver.find_element(By.XPATH, '//*[@id="table-0"]/thead/tr/td[6]/a').click()
                    get_mating = driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[8]/a').click()
                    if 'Kolgotki' in driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[2]').text:
                        mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                elif driver.find_element(By.XPATH, '//*[@id="boutonEchographie"]').text == 'Эхография':
                    next_hourse = driver.find_element(By.XPATH, '//*[@id="nav-next"]').click()

        except:
            print('Некакая error при уходе за лошадью')

    carrot = driver.find_element(By.XPATH, '//*[@id="boutonCarotte"]').click()
    mash = driver.find_element(By.XPATH, '//*[@id="boutonMash"]').click()
    pat = driver.find_element(By.XPATH, '//*[@id="boutonCaresser"]').click()
    water = driver.find_element(By.XPATH, '//*[@id="boutonBoire"]').click()






driver = newDR()
driver.set_window_size(1900, 1000)




