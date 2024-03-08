import os
import random
from datetime import datetime
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from os import getenv
from selenium.webdriver.common.keys import Keys


def newDR():
    chromeOptions = uc.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  # normal - full_load
    chromeOptions.add_argument("--single-process")
    chromeOptions.headless = False
    driver = uc.Chrome(options=chromeOptions, desired_capabilities=caps)
    return (driver)


def check_ufo():
    icon = driver.find_element(
        By.XPATH,
        '/html/body/div[1]/img'
    ).get_attribute('src')
    good_ufo = {'65e8bd83be647': '2 очка роста', '65ea39bcd81c0': '3 очка роста'}
    bad_ufo = {'pomme': 'яблоко', 'carotte': 'морковь', '65ea393c33885': 'экю', '65eaccbb759c5': 'комбикорм',
               '65eb0087272f2': 'экю'}
    try:
        if driver.find_element(By.XPATH, '//*[@id="Ufo_0"]'):
            if driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').children()[0].get_attribute('id') in ['65e8b9d2c19d8',
                                                                                                       '65e9eb1a06fe1', '65ea393c33885']:
                print(f'НЛО: экю, надо скипнуть')
                driver.get(url)
            elif driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').children()[0].get_attribute('id') in ['65e8bd83be647', '65ea39bcd81c0']:
                print(f'НЛО: 2 орки, надо ловить')
                driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').click()
                driver.find_element(By.XPATH, '//*[@id="agi-10972849001709751854"]').click()

    except:
        print('НЛО неть')


def login_lowadi():
    url = 'https://www.lowadi.com'

    driver.get(url)
    try:
        driver.find_element(By.XPATH, '/html/body/aside/div/article/div/div[2]/div/div/div[3]/form/button').click()
    except:
        pass

    driver.find_element(By.XPATH, '//*[@id="header-login-label"]').click()
    time.sleep(2)
    login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
    time.sleep(1)
    password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
    time.sleep(1)
    connect = driver.find_element(By.XPATH, '//*[@id="authentificationSubmit"]').click()
    time.sleep(1)


def milk_hourse(age, name, n):
    print(f'№{n} Молочный жеребенок: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonAllaiter"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    next_hourse = driver.find_element(By.XPATH, '//*[@id="nav-next"]').click()


def young_horse(age, name, n):
    print(f'№{n} Жеребенок на фураже: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(1)
    choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[6]').click()
    time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    next_hourse = driver.find_element(By.XPATH, '//*[@id="nav-next"]').click()


def old_horse(age, name, n):
    print(f'№{n} Взрослая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(1)
    if 'недостаточный вес' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
        choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[21]').click()
        time.sleep(1)
    else:
        choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[13]').click()
        time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
    time.sleep(1)


def female_horse():
    try:
        text = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-body-content"]/div[1]/table/tbody/tr[1]/td'
        ).text
        print(text)
        next_hourse = driver.find_element(By.XPATH, '//*[@id="nav-next"]').click()
    except:
        if driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Случить кобылу':
            driver.find_element(By.XPATH, '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]/a').click()
            time.sleep(1)
            master = driver.find_element(By.XPATH, '//*[@id="breeder"]').send_keys('Kolgotki')
            time.sleep(1)
            get_offers = driver.find_element(By.XPATH,
                                             '/html/body/div[7]/main/section/section/form/button[1]/span/span').click()
            time.sleep(1)
            price_sort = driver.find_element(By.XPATH, '//*[@id="table-0"]/thead/tr/td[6]/a').click()
            time.sleep(1)
            get_mating = driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[8]/a').click()
            time.sleep(1)
            if 'Kolgotki' in driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[2]').text:
                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)
            print('Кобыла успешно провела случку')
            next_hourse = driver.find_element(By.XPATH, '//*[@id="nav-next"]').click()
        elif driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Эхография':
            print('Кобыла уже беременна')
            next_hourse = driver.find_element(By.XPATH, '//*[@id="nav-next"]').click()


def childbirth(current_url):
    sex = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/img'
    ).get_attribute('alt')
    gen_potential = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[2]/tbody/tr[1]/td[2]/span').text
    print(f'Родился жеребенок! Пол: {sex}, ГП: {gen_potential}')
    if sex == 'male':
        get_name = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/input'
        ).send_keys(f'Пуля {gen_potential}')
    elif sex == 'femelle':
        get_name = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/input'
        ).send_keys(f'Вишня {gen_potential}')
    profile = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[1]'
    ).click()
    time.sleep(1)
    farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]').click()
    time.sleep(2)
    get_farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]/select/option[2]'
    ).click()
    time.sleep(1)
    complete = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/button'
    ).click()
    time.sleep(1)
    return_to_mother = driver.get(current_url)


def get_stable():
    print('Лошадь нуждается в стойле, ищем подходящий КСК..')
    find_stable = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[4]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
    ).click()
    time.sleep(1)
    two_mouth = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[1]/table/thead/tr/td[6]/span[2]/span/span[9]/a'
    ).click()
    time.sleep(1)
    low_price_stable = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[1]/table/tbody/tr[1]/td[10]/button/span/span/span/span'
    )
    low_price_stable.click()
    alert = driver.switch_to.alert
    alert.accept()
    print(f'Стойло найдено за {low_price_stable.text}, продолжаем')


def work_hourse():
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=19637945'
    driver.get(url)
    n = 1

    while driver.find_element(
            By.XPATH,
            '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
    ).get_attribute('href') != 'https://www.lowadi.com/elevage/chevaux/cheval?id=19637945':

        try:
            current_url = driver.find_element(
                By.XPATH,
                '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
            ).get_attribute('href')
            age = driver.find_element(
                By.XPATH,
                '//*[@id="characteristics-body-content"]/table/tbody/tr[1]/td[2]'
            ).text.split()
            name = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[2]/h1/a'
            ).text

            try:
                if 'Зарегистрируйте свою лошадь' in driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[1]/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
                ).text:
                    get_stable()
            except:
                pass

            if (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) > 1 and age[2] == 'мес.'):
                young_horse(age, name, n)
            elif 'несколько' in age or ('лет' not in age and age[0] in (2, 4)):
                milk_hourse(age, name, n)
            elif int(age[1]) >= 2:

                try:
                    if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                        print('Ваша кобыла скоро родит!')
                        call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                        time.sleep(1)
                        childbirth(current_url)
                except:
                    pass

                old_horse(age, name, n)

            if 'кобыла' in driver.find_element(
                    By.XPATH,
                    '//*[@id="characteristics-body-content"]/table/tbody/tr[3]/td[1]').text:
                female_horse()
            elif 'конь' in driver.find_element(
                    By.XPATH,
                    '//*[@id="characteristics-body-content"]/table/tbody/tr[3]/td[1]').text:
                male_horse()

        except:
            print('Некакая error при уходе за лошадью')
        n += 1
        print('-' * 50)


    carrot = driver.find_element(By.XPATH, '//*[@id="boutonCarotte"]').click()
    mash = driver.find_element(By.XPATH, '//*[@id="boutonMash"]').click()
    pat = driver.find_element(By.XPATH, '//*[@id="boutonCaresser"]').click()
    water = driver.find_element(By.XPATH, '//*[@id="boutonBoire"]').click()


driver = newDR()
driver.set_window_size(1900, 1000)




