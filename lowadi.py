from datetime import datetime
import time
from get_driver import new_drb, new_brave_dr
import pretty_errors
from lowadi.andalusian import andalusian_female, andalusian_male, andalusian_unicorn, train_blup
from lowadi.andalusian import andalusian_elite_female, andalusian_male_reserve
from lowadi.heavyhorse import work_heavyhorse
from lowadi.marshadore import marshadore_female, marshadore_male
from lowadi.other import *
from lowadi.states import *


def begin(driver):
    xanthos(driver)
    time.sleep(5)
    topaz(driver)
    time.sleep(5)
    givre(driver)
    time.sleep(5)


def create_driver_chrome():
    '''
    main comp + chrome
    '''
    print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
    driver = new_drb()
    driver.set_window_size(1400, 1300)
    login_lowadi(driver)

    return driver


def create_driver_brave():
    '''
    notebook + brave
    '''
    driver = new_brave_dr()
    driver.set_window_size(1400, 1360)
    login_lowadi(driver)

    return driver


def login_begin():
    driver = create_driver_brave()
    begin(driver)
    driver.quit()


def login_running():
    driver = create_driver_brave()
    work_heavyhorse(driver, 100)
    andalusian_unicorn(driver, 50)
    driver.quit()


def login_andalusian():
    driver = create_driver_brave()
    andalusian_female(driver, 1350)
    driver.quit()


def login_male_andalusian():
    driver = create_driver_chrome()
    andalusian_elite_female(driver, 100)
    andalusian_male(driver, 200)
    andalusian_male_reserve(driver, 150)

    driver.quit()


def login_marshadore():
    driver = create_driver_chrome()
    marshadore_female(driver, 110)
    marshadore_male(driver, 5)
    driver.quit()


train_blup(driver)
