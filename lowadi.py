from datetime import datetime
import time
from chrome_driver import newDRB
import pretty_errors
from lowadi.andalusian import *
from lowadi.other import login_lowadi


if __name__ == '__main__':
    try:

        print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
        driver = newDRB()
        driver.set_window_size(1900, 1000)

    except:

        time.sleep(30)
        driver = newDRB()
        driver.set_window_size(1900, 1000)

    login_lowadi(driver)
    time.sleep(5)
    xanthos(driver)
    time.sleep(5)
    topaz(driver)
    time.sleep(5)
    givre(driver)
    time.sleep(5)
    atelier(driver)
    time.sleep(5)
    work_horse()
    time.sleep(5)
    for i in range(3):
        atelier()
        time.sleep(60 * 180)
