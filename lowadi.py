from datetime import datetime
import time
from get_driver import new_drb, new_brave_dr
import pretty_errors
from lowadi.andalusian import work_female, work_male, work_unicorn
from lowadi.heavyhorse import work_heavyhorse
from lowadi.other import *


def begin(driver):
    xanthos(driver)
    time.sleep(5)
    topaz(driver)
    time.sleep(5)
    givre(driver)
    time.sleep(5)


if __name__ == '__main__':
    try:

        print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
        driver = new_drb()
        driver.set_window_size(1400, 1300)

    except:

        time.sleep(3)
        driver = new_brave_dr()
        driver.set_window_size(1700, 1360)
        login_lowadi(driver)
        begin(driver)

    login_lowadi(driver)
    work_heavyhorse(driver, 100)
    work_unicorn(driver, 50)
    work_female(driver, 2055)
    work_male(driver, 200)

    """
    75 коней с гп 15к+ = 4 х 75 = 300 ежедневных случек = 75 душевых и поилок = х2 набора случки\кач
    80 лугов нужно под 2000 стойл = 160 на два набора, пока один под пастбища, другой восстанавливает плодородность
    """
