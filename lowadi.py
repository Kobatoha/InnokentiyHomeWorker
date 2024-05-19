from datetime import datetime
import time
from get_driver import new_drb, new_brave_dr
import pretty_errors
from lowadi.andalusian import work_horse
from lowadi.other import *


def begin(driver):
    login_lowadi(driver)
    time.sleep(5)
    xanthos(driver)
    time.sleep(5)
    topaz(driver)
    time.sleep(5)
    givre(driver)
    time.sleep(60 * 130)
    atelier(driver)
    input('Включи впн')
    time.sleep(5)


def second_step(driver):
    xanthos(driver)
    time.sleep(5)
    topaz(driver)
    time.sleep(5)
    givre(driver)
    time.sleep(5)
    atelier(driver)
    time.sleep(5)


if __name__ == '__main__':
    try:

        print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
        driver = new_drb()
        driver.set_window_size(1900, 1000)

    except:

        time.sleep(30)
        driver = new_brave_dr()
        driver.set_window_size(1700, 1360)
        login_lowadi(driver)
        atelier(driver)

    begin(driver)
    work_horse(driver, 2000)
