import time

from lowadi.care import *


def tianma(driver):
    print('Разбудим Тианму')
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=96945603'
    driver.get(url)
    get_lesson(driver)
    get_doping(driver)[-1].click()
    time.sleep(1)
    get_food(driver)
    get_sleep(driver)
