import os
import random
from datetime import datetime
import time
from get_driver import new_drb
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys, ActionChains
import pretty_errors
from lowadi.other import *
from lowadi.care import *
from lowadi.trade import *
from lowadi.training import *


def work_heavyhorse(driver, horses=100):
    print('Начинаем гонять тяжиков')
    url = 'https://www.lowadi.com/elevage/chevaux/?elevage=1593200'

    current_url = find_unworking_horse(driver, 'heavy_horse', '')
    driver.get(current_url)

    n = 1
    children = 0

    time.sleep(5)

    while horses != 0:
        check_ufo(driver)
        time.sleep(2)
        if check_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Лошадь-тяжеловоз: {name}, уже получила уход.', *age)
            n += 1
            print('-' * 50)
            horses -= 1

            time.sleep(1)
            continue
        else:
            try:
                check_ufo(driver)

                dead = death_horse(driver)

                if dead == 1:
                    driver.get(current_url)

                    next_horse(driver)

                current_url = get_current_url(driver)

                age = get_age_horse(driver)

                name = get_name_horse(driver)

                sex = get_sex(driver)

                if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                    milk_horse(driver, age, name, n)

                elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        fourrage_horse(driver, age, name, n)

                elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '4', 'мес.']:
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        young_horse(driver, age, name, n)

                elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                    try:

                        if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                            print('Ваша кобыла скоро родит!')
                            call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                            time.sleep(1)
                            children += childbirth(driver, current_url, 'heavy_horse')

                    except:
                        pass

                    old_horse(driver, age, name, n)
                    time.sleep(1)

                next_horse(driver)

            except Exception as e:

                print('Некакая error при уходе за лошадью:', e, current_url)
                try:
                    next_horse(driver)
                except:
                    try:
                        driver.get(current_url)
                    except:
                        driver.back()

            n += 1
            print('-' * 50)
            horses -= 1

    now = datetime.now().strftime('%d.%m %H:%M')
    print(f'\n{now} прогон тяжиков окончен')
