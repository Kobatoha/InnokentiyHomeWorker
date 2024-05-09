import os
import random
from datetime import datetime
import time
from chrome_driver import newDRB
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys, ActionChains
import json
from os import getenv
from lowadi.other import *
from lowadi.care import *
from lowadi.trade import *
from lowadi.training import *


def work_horse(horses=1000):
    print('Начинаем гонять лошадулек')
    url = 'https://www.lowadi.com/elevage/chevaux/?elevage=1582713'
    driver.get(url)
    time.sleep(3)
    current_url = find_unworking_horse()

    driver.get(current_url)

    children = 0
    get_mating = 0
    post_mating = 0
    stable = 0
    n = 1
    time.sleep(5)

    equus = 'Good'

    while horses != 0:
        check_ufo()
        time.sleep(2)
        if check_horse_complete():

            age = get_age_horse()

            name = driver.find_element(
                By.XPATH,
                '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
            ).text
            try:
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()
            except:
                driver.get(current_url)

            print(f'№{n} Лошадь: {name}, уже получила уход.', *age)
            n += 1
            print('-' * 50)
            horses -= 1

            time.sleep(1)
            continue

        try:
            check_ufo()

            dead = death_horse()

            if dead == 1:
                driver.get(current_url)
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()

            equus = check_equus()

            current_url = driver.find_element(
                By.XPATH,
                '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
            ).get_attribute('href')

            age = get_age_horse()

            name = driver.find_element(
                By.XPATH,
                '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
            ).text

            try:

                if 'Зарегистрируйте свою лошадь' in driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[1]'
                    '/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
                ).text and equus == 'Good':

                    print('Нужно стойло')
            except:

                pass

            if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                milk_horse(age, name, n)
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()

            elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                fourrage_horse(age, name, n)
                time.sleep(1)
                next_horse()

            elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                    ['Возраст:', '2', 'года', '4', 'мес.']:
                young_horse(age, name, n)

            elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                    ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                try:

                    if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                        print('Ваша кобыла скоро родит!')
                        call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                        time.sleep(1)
                        children += childbirth(current_url)

                except:

                    pass

                old_horse(age, name, n)

                if 'кобыла' in driver.find_element(
                        By.XPATH,
                        '//*[@id="characteristics-body-content"]/table/tbody/tr[3]/td[1]').text:
                    get_mating += female_horse(current_url)
                elif 'конь' in driver.find_element(
                        By.XPATH,
                        '//*[@id="characteristics-body-content"]/table/tbody/tr[3]/td[1]').text:
                    post_mating += male_horse()

        except:

            print('Некакая error при уходе за лошадью')
            try:
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()
            except:
                driver.get(current_url)

        n += 1
        print('-' * 50)
        horses -= 1

    now = datetime.now().strftime('%d.%m %H:%M')
    print(f'\n{now} прогон окончен\n-- Родилось жеребят: {children}\n-- Принято случек: {get_mating}\n'
          f'-- Предложено случек: {post_mating}\n-- Куплено стойл: {stable}')


if __name__ == '__main__':
    try:

        print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
        driver = newDRB()
        driver.set_window_size(1900, 1000)

    except:

        time.sleep(30)
        driver = newDRB()
        driver.set_window_size(1900, 1000)

    login_lowadi()
    time.sleep(5)
    xanthos()
    time.sleep(5)
    topaz()
    time.sleep(5)
    givre()
    time.sleep(5)
    atelier()
    time.sleep(5)
    work_horse()
    time.sleep(5)
    for i in range(3):
        atelier()
        time.sleep(60 * 180)
