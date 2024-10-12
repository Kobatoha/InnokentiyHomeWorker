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
