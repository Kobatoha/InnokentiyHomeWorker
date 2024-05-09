from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys, ActionChains
import os
import random
from datetime import datetime
import time
import pretty_errors
from care import *


def training():
    stamina = 8     # endurance
    speed = 8       # vitesse
    dressage = 5    # dressage
    gallop = 7      # galop
    trot = 7        # trot
    jumping = 7     # saut

    mountains = 9   # montagne
    forest = 9      # forest

    flag = 'Тренировка завершена!'
    name = get_name_horse()

    genetic_potential = int(name.split()[1])

    try:
        energie = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]'
            '/div[2]/div/div/div/div[2]/div/div[1]/div[3]/strong/span'
        ).text)
    except:
        energie = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]'
            '/div[2]/div/div/div/div[2]/div/div[1]/div[3]/strong/span'
        ).text)

    try:

        if genetic_potential >= 300:

            if int(get_age_horse()[1]) <= 3:

                hours = ride_mountains(energie, mountains)
                return hours

            elif flag not in driver.find_element(
                    By.XPATH,
                    '//*[@id="training-tab-main"]/div/table/tbody/tr[2]/td[2]'
            ).get_attribute('data-tooltip'):

                hours = train_speed(energie, speed)
                return hours

            elif flag not in driver.find_element(
                    By.XPATH,
                    '//*[@id="training-tab-main"]/div/table/tbody/tr[3]/td[2]'
            ).get_attribute('data-tooltip'):

                hours = train_dressage(energie, dressage)
                return hours

            elif flag not in driver.find_element(
                    By.XPATH,
                    '//*[@id="training-tab-main"]/div/table/tbody/tr[4]/td[2]'
            ).get_attribute('data-tooltip'):

                hours = train_galop(energie, gallop)
                return hours

        else:
            return 0

    except:

        return 0


def train_speed(energie, speed):
    try:

        choice_speed = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[2]/td[3]/button/span'
        ).click()

        hour = (energie - 20) // speed
        time.sleep(1)

        click_speed = driver.find_element(
            By.XPATH,
            f'//*[@id="trainingVitesseSlider"]/ol/li[{hour + 1}]'
        ).click()
        time.sleep(1)

        train = driver.find_element(
            By.XPATH,
            '//*[@id="training-vitesse-submit"]/span/span/span'
        ).click()
        time.sleep(1)

        pat = driver.find_element(
            By.XPATH,
            '//*[@id="boutonCaresser"]'
        ).click()
        print(f'Лошадь провела тренировку скорости на {hour} часов')
        return hour

    except:
        print('Тренировка отменяется, ждем дитятко.')
        return 0


def train_dressage(energie, dressage):
    try:

        choice_dressage = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[3]/td[3]/button/span'
        ).click()

        hour = (energie - 20) // dressage
        time.sleep(1)

        click_dressage = driver.find_element(
            By.XPATH,
            f'//*[@id="trainingDressageSlider"]/ol/li[{hour + 1}]'
        ).click()
        time.sleep(1)

        train = driver.find_element(
            By.XPATH,
            '//*[@id="training-dressage-submit"]/span/span/span'
        ).click()
        time.sleep(1)

        pat = driver.find_element(
            By.XPATH,
            '//*[@id="boutonCaresser"]'
        ).click()
        print(f'Лошадь провела тренировку выездки на {hour} часов')
        return hour

    except:
        print('Тренировка отменяется, ждем дитятко.')
        return 0


def train_galop(energie, gallop):
    try:

        choice_galop = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[4]/td[3]/button/span'
        ).click()

        hour = (energie - 20) // gallop
        time.sleep(1)

        click_galop = driver.find_element(
            By.XPATH,
            f'//*[@id="trainingGalopSlider"]/ol/li[{hour + 1}]'
        ).click()
        time.sleep(1)

        train = driver.find_element(
            By.XPATH,
            '//*[@id="training-galop-submit"]/span/span/span'
        ).click()
        time.sleep(1)

        pat = driver.find_element(
            By.XPATH,
            '//*[@id="boutonCaresser"]'
        ).click()
        print(f'Лошадь провела тренировку галопа на {hour} часов')
        return hour

    except:
        print('Тренировка отменяется, ждем дитятко.')
        return 0


def ride_mountains(energie, mountains):
    try:
        choice_mountains = driver.find_element(
            By.XPATH,
            '//*[@id="boutonBalade-montagne"]'
        ).click()

        hour = (energie - 20) // mountains
        time.sleep(1)

        click_mountains = driver.find_element(
            By.XPATH,
            f'//*[@id="walkmontagneSlider"]/ol/li[{hour + 1}]'
        ).click()
        time.sleep(1)

        if 'Скорость' not in driver.find_element(
                By.XPATH,
                '//*[@id="walk-montagne-form"]/table/tbody/tr[2]/td'
        ).text:
            return 0

        else:
            train = driver.find_element(
                By.XPATH,
                '//*[@id="walk-montagne-submit"]/span/span/span'
            ).click()
            time.sleep(1)

            pat = driver.find_element(
                By.XPATH,
                '//*[@id="boutonCaresser"]'
            ).click()
            time.sleep(1)

            water = driver.find_element(
                By.XPATH,
                '//*[@id="boutonBoire"]'
            ).click()
            print(f'Лошадь провела прогулку в горах на {hour} часов')

            return hour

    except:
        print('Прогулка отменяется, ждем дитятко.')


def blup_montains(hour):
    choice_mountains = driver.find_element(
        By.XPATH,
        '//*[@id="boutonBalade-montagne"]'
    ).click()
    time.sleep(1)
    choice_hours = driver.find_element(
        By.XPATH,
        f'//*[@id="walkmontagneSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(1)
    train = driver.find_element(
        By.XPATH,
        '//*[@id="walk-montagne-submit"]/span/span/span'
    ).click()
    time.sleep(2)


def blup_forest(hour):
    choice_forest = driver.find_element(
        By.XPATH,
        '//*[@id="boutonBalade-foret"]'
    ).click()
    time.sleep(1)
    choice_hours = driver.find_element(
        By.XPATH,
        f'//*[@id="walkforetSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(1)
    train = driver.find_element(
        By.XPATH,
        '//*[@id="walk-foret-submit"]/span/span/span'
    ).click()
    time.sleep(2)


def blup_dressage(hour):
    try:
        choice_dressage = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[3]/td[3]/button/span'
        ).click()
        time.sleep(1)
    except:
        choice_dressage = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[3]/td[3]/button/span'
        ).click()
        time.sleep(1)

    click_dressage = driver.find_element(
        By.XPATH,
        f'//*[@id="trainingDressageSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(1)

    train = driver.find_element(
        By.XPATH,
        '//*[@id="training-dressage-submit"]/span/span/span'
    ).click()
    time.sleep(2)


def blup_speed(hour):
    try:
        choice_speed = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[2]/td[3]/button/span'
        ).click()
        time.sleep(1)
    except:
        choice_speed = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[2]/td[3]/button/span'
        ).click()
        time.sleep(1)

    click_speed = driver.find_element(
        By.XPATH,
        f'//*[@id="trainingVitesseSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(1)

    train = driver.find_element(
        By.XPATH,
        '//*[@id="training-vitesse-submit"]/span/span/span'
    ).click()
    time.sleep(2)


def blup_galop(hour):
    try:
        choice_galop = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[4]/td[3]/button/span'
        ).click()
        time.sleep(1)
    except:
        choice_galop = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[4]/td[3]/button/span'
        ).click()
        time.sleep(1)

    click_galop = driver.find_element(
        By.XPATH,
        f'//*[@id="trainingGalopSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(1)

    train = driver.find_element(
        By.XPATH,
        '//*[@id="training-galop-submit"]/span/span/span'
    ).click()
    time.sleep(2)


def blup_step_forest(forest=190):
    if 'лесу' in driver.find_element(
        By.XPATH,
        '//*[@id="center-tab-main"]/div[1]/table/tbody/tr[1]/td/div[2]/div/div[2]/a'
    ).get_attribute('data-tooltip'):
        forest = 95
    while forest != 0:
        clean = get_doping()[4].click()
        time.sleep(1)

        hour = 11
        blup_forest(hour)
        forest -= hour

        for i in range(4):
            get_doping()[i].click()
            time.sleep(1)

        blup_diet()

        hour = 4
        blup_forest(hour)
        forest -= hour

        grow_up()
        time.sleep(2)


def train_blup():
    name = driver.find_element(
        By.XPATH,
        '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
    ).text
    gp = name.split()[1]
    age = get_age_horse()
    step = 1
    speed = 100
    dressage = 100
    galop = 100
    forest = 200
    montains = 200
    competitions_galop = 25
    competitions_trot = 25

    if age == ['Возраст:', 'несколько', 'часов']:
        for i in range(3):
            milk_horse(age, name, step)

            grow_up()
            step += 1

    age = get_age_horse()

    if age == ['Возраст:', '6', 'мес.']:
        wait_stable = input('Найди мне классное стойло с душем, поилкой, морковкой и комбикормом!')
        print('Спасибо, кек.')
        for i in range(6):
            fourrage_horse(name, age, step)
            grow_up()
            step += 1
        print('Nice!')

    age = get_age_horse()

    if age == ['Возраст:', '1', 'год', '6', 'мес.']:
        for i in range(3):
            hour = 12
            fourrage_horse(name, age, step)
            blup_montains(hour)
            montains -= hour
            for j in range(4):
                get_doping()[j].click()
                time.sleep(2)

            hour = 1
            blup_montains(hour)
            montains -= hour
            grow_up()

            step += 1

    age = get_age_horse()

    if age == ['Возраст:', '2', 'года']:
        n = 0
        for i in range(5):
            print(n)
            hour = 11
            blup_montains(hour)
            montains -= hour
            for j in range(4):
                get_doping()[j].click()
                time.sleep(2)
            blup_diet()
            hour = 4
            blup_montains(hour)
            montains -= hour
            hour = 1
            blup_dressage(hour)
            dressage -= hour
            grow_up()

            step += 1
            n += 1

    age = get_age_horse()

    if age == ['Возраст:', '2', 'года', '10', 'мес.']:
        for i in range(3):
            hour = 12
            blup_speed(hour)
            speed -= hour
            for j in range(4):
                get_doping()[j].click()
                time.sleep(2)
            blup_diet()
            hour = 4
            blup_speed(hour)
            speed -= hour
            grow_up()

            step += 1

    age = get_age_horse()

    if age == ['Возраст:', '5', 'лет']:
        for i in range(3):
            get_doping()[4].click()
            time.sleep(2)
            hour = 20
            blup_dressage(hour)
            dressage -= hour
            for j in range(3):
                get_doping()[j].click()
                time.sleep(2)
            blup_diet()
            hour = 4
            blup_dressage(hour)
            dressage -= hour
            grow_up()

            step += 1

    age = get_age_horse()

    if age == ['Возраст:', '5', 'лет', '6', 'мес.']:
        print('Начинаем качать соревнования.')
        get_classic = input('Выбери мне специализацию "Классическая езда" и снаряди вальтрап, седло и уздечку')
        print('Spasibo')
        for i in range(6):
            get_competition = driver.find_element(
                By.XPATH,
                '//*[@id="competition-body-content"]/table/tbody/tr[1]/td[2]/a'
            ).click()
            time.sleep(2)
            run = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[8]/button/span/span/span'
            ).click()
            competitions_galop -= 1
            time.sleep(3)

        get_doping()[0].click()
        time.sleep(2)
        get_doping()[4].click()
        time.sleep(2)
        blup_diet()
        grow_up()

        step += 1

    age = get_age_horse()

    if age == ['Возраст:', '5', 'лет', '6', 'мес.']:
        for i in range(5):
            get_doping()[4].click()
            time.sleep(2)
            hour = 14
            blup_galop(hour)
            galop -= hour
            for i in range(4):
                get_doping()[i].click()
                time.sleep(2)
            blup_diet()
            hour = 6
            blup_galop(hour)
            galop -= hour
            grow_up()

            step += 1
            time.sleep(2)

    age = get_age_horse()

    if age == ['Возраст:', '8', 'лет', '6', 'мес.']:
        while competitions_trot != 0:
            for i in range(6):
                get_competition = driver.find_element(
                    By.XPATH,
                    '//*[@id="competition-body-content"]/table/tbody/tr[1]/td[1]/a'
                ).click()
                time.sleep(1)
                check_ufo()
                run = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[8]/button/span/span/span'
                ).click()
                competitions_trot -= 1
                time.sleep(2)

            get_doping()[0].click()
            time.sleep(1)
            blup_diet()
            grow_up()

            step += 1
            time.sleep(2)
