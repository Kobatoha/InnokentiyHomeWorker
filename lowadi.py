from datetime import datetime
import time
from get_driver import new_drb, new_brave_dr
import pretty_errors
from lowadi.andalusian import andalusian_female, andalusian_male, andalusian_unicorn, train_blup
from lowadi.andalusian import andalusian_elite_female, andalusian_male_reserve
from lowadi.heavyhorse import work_heavyhorse
from lowadi.marshadore import marshadore_female, marshadore_male
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
        '''
        main comp + chrome
        '''
        print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
        driver = new_drb()
        driver.set_window_size(1400, 1300)
        login_lowadi(driver)

    except:
        '''
        notebook + brave
        '''
        time.sleep(3)
        driver = new_brave_dr()
        driver.set_window_size(1700, 1360)
        login_lowadi(driver)
        begin(driver)

    login_lowadi(driver)
    work_heavyhorse(driver, 130)
    andalusian_unicorn(driver, 50)
    andalusian_female(driver, 1200)
    andalusian_male(driver, 300)
    andalusian_male_reserve(driver, 130)
    marshadore_female(driver, 130)
    marshadore_male(driver, 40)
    andalusian_elite_female(driver, 30)

    atelier(driver, 4)
    train_blup(driver)


    """
    75 коней с гп 15к+ = 4 х 75 = 300 ежедневных случек = 75 душевых и поилок = х2 набора случки\кач
    80 лугов нужно под 2000 стойл = 160 на два набора, пока один под пастбища, другой восстанавливает плодородность
    """
