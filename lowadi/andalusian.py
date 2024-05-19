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


def work_horse(driver, horses=1000):
    print('Начинаем гонять лошадулек')
    url = 'https://www.lowadi.com/elevage/chevaux/?elevage=1582713'
    driver.get(url)
    time.sleep(3)
    current_url = find_unworking_horse(driver)

    driver.get(current_url)

    children = 0
    get_mating = 0
    post_mating = 0
    stable = 0
    n = 1
    time.sleep(5)

    equus = check_equus(driver)

    while horses != 0:
        check_ufo(driver)
        time.sleep(2)
        if check_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Лошадь: {name}, уже получила уход.', *age)
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

                get_stable(driver)

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

                    try:

                        if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                            print('Ваша кобыла скоро родит!')
                            call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                            time.sleep(1)
                            children += childbirth(driver, current_url)

                    except:
                        pass

                    old_horse(driver, age, name, n)

                    if 'кобыла' in sex:
                        get_mating += female_horse(driver, current_url)

                    elif 'конь' in sex:
                        post_mating += male_horse(driver)

                    energy = get_energy(driver)
                    general_training(driver, energy)
                    if get_energy(driver) < 20:
                        get_doping(driver)[0].click()

                next_horse(driver)

            except Exception as e:

                print('Некакая error при уходе за лошадью:', e, current_url)
                try:
                    next_horse(driver)
                except:
                    driver.refresh()

            n += 1
            print('-' * 50)
            horses -= 1

    now = datetime.now().strftime('%d.%m %H:%M')
    print(f'\n{now} прогон окончен\n-- Родилось жеребят: {children}\n-- Принято случек: {get_mating}\n'
          f'-- Предложено случек: {post_mating}\n-- Куплено стойл: {stable}')


def train_blup_one_click(driver, url):
    driver.get(url)
    age = get_age_horse(driver)
    name = get_name_horse(driver)
    step = 1
    speed = 100
    dressage = 100
    galop = 100
    forest = 200
    montains = 200
    competitions_galop = 25
    competitions_trot = 25




def train_blup_montains(driver, montains=200, dressage=100):
    """
    Обязательное наличие:
     🛁 душа
     💦 поилки
     🥕 морковки
     💊 смеси
    :param dressage:
    :param montains:
    :param driver:
    :return:
    """
    age = get_age_horse(driver)
    fourrage_age = [['Возраст:', '1', 'год', f'{x}', 'мес.'] for x in range(6, 12, 2)]
    doping = [3, 5]
    location = get_location_complex(driver)
    if 'Montagne' in location:
        montains -= 100

    if montains >= 15:
        energy = get_energy(driver)
        hour = energy // 8
        blup_montains(driver, hour)
        montains -= hour

        if age in fourrage_age:

            for i in range(doping[0]):
                get_doping(driver)[i].click()
                time.sleep(1)
            fourrage_horse(driver, age, name, step)
        else:
            for i in range(doping[1]):
                get_doping(driver)[i].click()
                time.sleep(1)
            blup_diet(driver)

        energy = get_energy(driver)
        hour = (energy - 20) // 8
        blup_montains(driver, hour)
        montains -= hour

        if age not in fourrage_age:
            energy = get_energy(driver)
            hour = int((energy - 20) // 4.5)
            blup_dressage(driver, hour)
            dressage -= hour

        grow_up(driver)
        return [montains, dressage]
    elif 15 > montains >= 11:
        energy = get_energy(driver)
        hour = energy // 8
        blup_montains(driver, hour)
        montains -= hour
        for i in range(doping[1]):
            get_doping(driver)[i].click()
            time.sleep(1)
        blup_diet(driver)
        blup_montains(driver, montains)
        montains -= montains
        energy = get_energy(driver)
        if montains == 0:
            print(f'Прибавка к навыкам от прогулок в горах закончилась, осталость еще {energy - 20} свободной энергии')
            hour = int((energy - 20) // 4.5)
            blup_dressage(driver, hour)
            dressage -= hour
            grow_up(driver)

        return [montains, dressage]

    else:
        blup_montains(driver, montains)
        print('Прибавка к навыкам от прогулок в горах закончилась, остальную энергию вкинем в Выездку')
        energy = get_energy(driver)
        hour = int(energy // 4.5)
        blup_dressage(driver, hour)
        dressage -= hour
        for i in range(doping[1]):
            get_doping(driver)[i].click()
            time.sleep(1)
        blup_diet(driver)
        energy = get_energy(driver)
        hour = int((energy - 20) // 4.5)
        blup_dressage(driver, hour)
        dressage -= hour
        grow_up(driver)

        return [0, dressage]


def train_blup_speed(driver, speed=100, dressage=100):
    """
    Обязательное наличие:
     🛁 душа
     💦 поилки
     🥕 морковки
     💊 смеси
    :param dressage:
    :param speed:
    :param driver:
    :return:
    """

    if speed >= 15:
        energy = get_energy(driver)
        hour = int(energy // 7.5)
        blup_speed(driver, hour)
        speed -= hour

        for i in range(5):
            get_doping(driver)[i].click()
            time.sleep(1)

        blup_diet(driver)

        energy = get_energy(driver)
        hour = int((energy - 20) // 7.2)
        blup_speed(driver, hour)
        speed -= hour

        grow_up(driver)
        return [montains, dressage]
