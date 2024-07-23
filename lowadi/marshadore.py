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


def marshadore_female(driver, horses=100):
    print('Начинаем гонять маршадорок')
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=19637945'

    current_url = find_unworking_horse(driver, 'marshadore', 'female')

    if not current_url:
        print('Все спят, гонять нечего <3')
        return

    driver.get(current_url)

    children = 0
    get_mating = 0
    post_mating = 0
    stable = 0

    n = 1
    time.sleep(5)

    while horses != 0:
        check_ufo(driver)
        time.sleep(2)
        if check_equus(driver) == 'Good':
            spend_equus(driver)
        if check_young_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Лошадь-маршадор: {name}, уже получила уход.', *age)
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

                try:
                    stable += get_stable(driver)
                except:
                    pass

                if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                    milk_horse(driver, age, name, n)

                elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                    fourrage_horse(driver, age, name, n)

                    try:
                        blup_montains(driver, hour=8)
                    except:
                        print('Еще не дорос до прогулок')
                    time.sleep(1)

                elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '4', 'мес.']:

                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        young_horse(driver, age, name, n)

                    blup_montains(driver, hour=6)
                    get_doping(driver)[0].click()

                elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                    try:

                        if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                            print('Ваша кобыла скоро родит!')
                            call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                            time.sleep(1)
                            children += childbirth(driver, current_url, 'marshadore')

                    except:
                        pass

                    get_mating += female_marshadore(driver, current_url)

                    get_doping(driver)[-1].click()
                    time.sleep(2)
                    get_food(driver)
                    get_sleep(driver)

                    energy = get_energy(driver)
                    general_training_marshadore(driver, energy)
                    if get_energy(driver) < 20:
                        get_doping(driver)[0].click()
                        time.sleep(1)
                        get_doping(driver)[1].click()
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
    print(f'\n{now} прогон маршадорок окончен\n-- Родилось жеребят: {children}\n-- Принято случек: {get_mating}\n'
          f'-- Предложено случек: {post_mating}\n-- Куплено стойл: {stable}')


def marshadore_male(driver, horses=20):
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=92114142'

    current_url = find_unworking_horse(driver, 'marshadore', 'male')

    if not current_url:
        print('Все спят, гонять нечего <3')
        return

    driver.get(current_url)

    post_mating = 0
    stable = 0

    n = 1
    time.sleep(5)

    while horses != 0:
        check_ufo(driver)
        time.sleep(2)
        if check_young_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Конь-маршадор: {name}, уже получил уход.', *age)
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

                try:
                    stable += get_stable(driver)
                except:
                    pass

                if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                    milk_horse(driver, age, name, n)

                elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        fourrage_horse(driver, age, name, n)

                        try:
                            blup_montains(driver, hour=8)
                        except:
                            print('Еще не дорос до прогулок')
                        time.sleep(1)

                elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '4', 'мес.']:
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        young_horse(driver, age, name, n)
                    blup_montains(driver, hour=6)
                    get_doping(driver)[0].click()

                elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                    get_doping(driver)[1].click()
                    time.sleep(1)

                    if 'конь' in sex:
                        post_mating += male_marshadore(driver)

                    get_doping(driver)[4].click()
                    time.sleep(1)
                    get_food(driver)
                    time.sleep(1)
                    get_sleep(driver)
                    time.sleep(1)

                    energy = get_energy(driver)
                    general_training_marshadore(driver, energy)
                    if get_energy(driver) < 20:
                        get_doping(driver)[0].click()
                        time.sleep(1)
                        get_doping(driver)[1].click()
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
    print(f'\n{now} прогон мужиков окончен\n-- Предложено случек: {post_mating}')

