import os
import random
from datetime import datetime
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from os import getenv


def newDR():
    chromeOptions = uc.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  # normal - full_load
    chromeOptions.add_argument("--single-process")
    chromeOptions.headless = False
    driver = uc.Chrome(options=chromeOptions, desired_capabilities=caps)
    return (driver)


def check_ufo():
    good_ufo = {'65e8bd83be647': '2 очка роста', '65ea39bcd81c0': '3 очка роста'}
    bad_ufo = {'65e8b9d2c19d8': 'экю', '65e9eb1a06fe1': 'морковь', '65ea393c33885': 'экю', '65eaccbb759c5': 'комбикорм'}
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

    driver.find_element(By.XPATH, '/html/body/aside/div/article/div/div[2]/div/div/div[3]/form/button').click()

    driver.find_element(By.XPATH, '//*[@id="header-login-label"]').click()
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


def women_horse():
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
            next_hourse = driver.find_element(By.XPATH, '//*[@id="nav-next"]').click()
        elif driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Эхография':
            next_hourse = driver.find_element(By.XPATH, '//*[@id="nav-next"]').click()


def childbirth(current_url):
    call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
    time.sleep(1)
    sex = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/img'
    ).get_attribute('alt')
    gen_potential = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[2]/tbody/tr[1]/td[2]/span').text
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
    farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]').click()
    get_farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]/select/option[2]'
    ).click()
    complete = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/button'
    ).click()
    return_to_mother = driver.get(current_url)


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

            if int(age[1]) < 2:
                young_horse(age, name, n)
            elif 'несколько' in age or ('лет' not in age and age[0] in (2, 4)):
                milk_hourse(age, name, n)
            elif int(age[1]) >= 2:
                try:
                    if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                        print('Ваша кобыла скоро родит!')
                        childbirth(current_url)
                except:
                    pass

                old_horse(age, name, n)

            if 'кобыла' in driver.find_element(
                    By.XPATH,
                    '//*[@id="characteristics-body-content"]/table/tbody/tr[3]/td[1]').text:
                women_horse()

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




