import os
import random
from datetime import datetime
import time
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import json
from os import getenv
from selenium.webdriver import Keys, ActionChains
import schedule


def newDR():
    chromeOptions = uc.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  # normal - full_load
    chromeOptions.add_argument("--single-process")
    chromeOptions.headless = False
    driver = uc.Chrome(options=chromeOptions, desired_capabilities=caps)

    return driver


def newDRB():
    chromeOptions = uc.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"  # normal - full_load
    chromeOptions.add_extension('browsec.crx')
    # chromeOptions.add_argument("--single-process")
    chromeOptions.headless = False
    driver = uc.Chrome(options=chromeOptions, desired_capabilities=caps)

    return driver


def check_ufo():

    good_ufo = {'vieillissement': 'очки роста'}
    bad_ufo = {'pomme': 'яблоко', 'carotte': 'морковь', 'classique': 'седло', 'mash': 'комбикорм',
               'equus': 'экю'}
    try:

        if driver.find_element(By.XPATH, '//*[@id="Ufo_0"]'):
            icon = driver.find_element(By.XPATH, '/html/body/div[1]/img').get_attribute('src')

            for bad_key in bad_ufo:
                if bad_key in icon:
                    print(f"НЛО: {bad_ufo[bad_key]}, надо скипнуть")
                    driver.refresh()

            for good_key in good_ufo:
                if good_key in icon:
                    print(f"НЛО: {good_ufo[good_key]}, надо брать")
                    driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="agi-10972849001709751854"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '/html/body/div[12]/aside/div[2]/button/span/span').click()
                    driver.refresh()
                    time.sleep(1)

            driver.refresh()
            time.sleep(1)

    except:

        return


def login_lowadi():
    now = datetime.now().strftime('%H:%M:%S')
    print(f'{now}: Логинимся на lowadi.com')
    url = 'https://www.lowadi.com'

    driver.get(url)

    try:

        print('Принимаем cookie')
        driver.find_element(By.XPATH, '/html/body/aside/div/article/div/div[2]/div/div/div[3]/form/button').click()

    except:
        print('Принять cookie не просили')

    try:

        print(f'Начинаем!')
        driver.find_element(By.XPATH, '/html/body/div[7]/header/nav/div/strong').click()
        time.sleep(2)
        print(f'Вводим логин..')
        login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
        time.sleep(1)
        print(f'Вводим пароль..')
        password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
        time.sleep(1)
        print(f'Входим')
        connect = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/header/nav/div/div/form/button/span/span/span'
        ).click()
        time.sleep(1)

    except:

        url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=20378769'
        driver.get(url)

        print(f'Пробуем зайти заново')
        time.sleep(60)
        print(f'Вводим логин..')
        login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
        time.sleep(1)
        print(f'Вводим пароль..')
        password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
        time.sleep(1)
        print(f'Входим')
        connect = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/aside/form/button'
        ).click()
        time.sleep(30)


def milk_horse(age, name, n):
    print(f'№{n} Молочный жеребенок: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonAllaiter"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)


def fourrage_horse(age, name, n):
    print(f'№{n} Жеребенок на фураже: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(2)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(1)
    choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[12]').click()
    time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)


def next_horse():
    try:
        next_hourse = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
        ).click()

    except:
        next_hourse = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
        ).click()


def young_horse(age, name, n):
    print(f'№{n} Молодая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(1)
    choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[12]').click()
    time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
    time.sleep(1)

    try:
        training()
    except:
        pass

    next_hourse = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
    ).click()


def old_horse(age, name, n):
    print(f'№{n} Взрослая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(2)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(2)

    try:

        if 'недостаточный вес' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[21]').click()
            time.sleep(1)
        else:
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[13]').click()
            time.sleep(1)

    except:

        choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[13]').click()
        time.sleep(1)

    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(2)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
    time.sleep(1)


def female_horse(current_url):
    try:

        not_ready = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-body-content"]/div[1]/table/tbody/tr[1]/td'
        ).text
        print(not_ready)
        time.sleep(1)
        training()

        try:
            try:

                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()
            except:
                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()

        except:

            next_hourse = driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
            ).click()

        return 0

    except:

        if driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Случить кобылу':

            print('Нужна случка, идем на брачный рынок..')
            check_ufo()
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
            time.sleep(1)

            training()

            try:
                try:

                    next_hourse = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                    ).click()
                except:
                    next_hourse = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                    ).click()

            except:

                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[8]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()

            return 1

        elif driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Эхография':

            print('Кобыла уже жеребая')
            time.sleep(1)

            training()

            try:
                try:

                    next_hourse = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                    ).click()
                except:
                    next_hourse = driver.find_element(
                        By.XPATH,
                        '/html/body/div[8]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                    ).click()

            except:

                next_hourse = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
                ).click()

            return 0


def male_horse():
    mating = 25
    num = 0

    try:

        for i in range(5):
            energie = int(driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[2]'
                '/div/div/div/div[2]/div/div[1]/div[3]/strong/span'
            ).text)
            if energie - mating >= 20:
                create_mating = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[3]/a'
                )
                try:
                    create_mating.click()
                    time.sleep(1)
                    open_mating = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/ul/li[1]/input'
                    ).click()
                    choice_equus = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select'
                    ).click()
                    time.sleep(2)
                    lower_price = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[3]'
                    ).click()
                    time.sleep(1)
                    complete = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[3]/button/span'
                    ).click()
                    time.sleep(5)

                    num += 1

                except:
                    return num

        print(f'Конь предложил случек: {num}')

        training()

        try:

            next_hourse = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
            ).click()

            return num

        except:

            next_hourse = driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[4]/a[2]'
            ).click()

            return num

    except:

        print('error male_horse')

        return 0


def childbirth(current_url):
    age = 'Несколько часов'
    check_ufo()
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
        '/html/body/div[7]/main/section/section/form/table[3]/tbody'
        '/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]').click()
    time.sleep(2)
    get_farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody'
        '/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]/select/option[2]'
    ).click()
    time.sleep(1)
    complete = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/button'
    ).click()
    time.sleep(1)

    milk_horse(age, 'дитё', 0)
    time.sleep(1)

    return_to_mother = driver.get(current_url)

    return 1


def get_stable():
    try:
        print('Лошадь нуждается в стойле, ищем подходящий КСК..')
        current_url = driver.find_element(
            By.XPATH,
            '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
        ).get_attribute('href')

        find_stable = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[1]'
            '/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
        ).click()
        time.sleep(1)

        check_ufo()

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
        time.sleep(2)

        return 1

    except:

        return 0


def death_horse():
    try:

        death = driver.find_element(
            By.XPATH,
            '//*[@id="page-contents"]/section/div/div/div[1]/h1'
        ).text

        if 'умер' in death:
            paradise = driver.find_element(
                By.XPATH,
                '//*[@id="page-contents"]/section/div/div/div[1]/div[2]/a'
            ).click()
            print('Ваша лошадь умерла и отправилась в рай, аминь')

            return 1

    except:

        return 0


def training():
    stamina = 8                 # endurance
    speed = 8                   # vitesse
    dressage = 5                # dressage
    gallop = 7                  # galop
    trot = 7                    # trot
    jumping = 7                 # saut

    mountains = 9               # montagne

    flag = 'Тренировка завершена!'

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

    genetic_potential = driver.find_element(
        By.XPATH,
        '//*[@id="tab-genetics-title"]'
    ).click()

    time.sleep(0.2)

    try:
        gp = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[4]/div/div/div/div/table[2]'
            '/tbody[1]/tr/td/div/table[1]/tbody/tr[1]/td[3]/strong'
        ).text.split()[1][:-3])
    except:
        gp = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[4]/div/div/div/div/table[2]'
            '/tbody[1]/tr/td/div/table[1]/tbody/tr[1]/td[3]/strong'
        ).text.split()[1][:-3])


    try:

        if gp >= 300:

            if flag not in driver.find_element(
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
                train = driver.find_element(
                    By.XPATH,
                    '//*[@id="training-tab-main"]/div/table/tbody/tr[4]/td[2]'
                ).get_attribute('data-tooltip')
                print(train, 'Начинаем прогулки..')

                hours = ride_mountains(energie, mountains)
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


def find_unworking_horse():

    pages = len(driver.find_elements(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li'
    )[1:])

    print(f'Страниц во вкладке: {pages}')
    for i in range(2, pages + 2):
        page = driver.find_element(
            By.XPATH,
            f'/html/body/div[7]/main/section/section/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[{i}]/a'
        ).click()
        print(f'Page: {i - 1}')
        time.sleep(1)
        url = ''
        horses = driver.find_elements(By.XPATH, '//*[@class="damier-cell grid-cell width-25"]')

        for j in range(len(horses)):
            try:
                name = horses[j].find_element(By.CLASS_NAME, 'horsename').text
                status = horses[j].find_elements(By.XPATH, '//*[@class="cheval-status spacer-small-left"]/span[1]')[
                    j].get_attribute('data-tooltip')

                if status != 'Спит':
                    print('Найдена необработанная лошадь')
                    url = horses[j].find_element(By.CLASS_NAME, 'horsename').get_attribute('href')
                    return url
            except:
                pass


def check_horse_complete():
    try:
        history = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[1]/div[5]/div/div/div/div[1]/div/div/div/ul'
        ).text.split('\n')
        count = 0
        for i in history:
            if 'Полный уход' in i:
                count += 1
            elif 'съел(а)' in i:
                count += 1
            elif 'уложен(а) спать' in i:
                count += 1
            elif 'урок верховой езды' in i or 'выполнила миссию' in i:
                count += 1
        if count == 4:
            return True
        return False
    except Exception as error:
        print('error in check_horse_complete')


def work_horse():
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

    horses = 1000
    equus = 'Good'

    while horses != 0:
        check_ufo()
        time.sleep(2)
        if check_horse_complete():

            age = driver.find_element(
                By.XPATH,
                '//*[@id="characteristics-body-content"]/table/tbody/tr[1]/td[2]'
            ).text.split()

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

            age = driver.find_element(
                By.XPATH,
                '//*[@id="characteristics-body-content"]/table/tbody/tr[1]/td[2]'
            ).text.split()

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


def xanthos():
    """
    Ежедневная глажка 5 Ксанфов.
    Есть вероятность получить рог изобилия.
    :return:
    """
    urls = [
        'https://www.lowadi.com/elevage/fiche/?id=1045736',
        'https://www.lowadi.com/elevage/fiche/?id=1047131',
        'https://www.lowadi.com/elevage/fiche/?id=1044747',
        'https://www.lowadi.com/elevage/fiche/?id=1044960',
        'https://www.lowadi.com/elevage/fiche/?id=1046269'
    ]
    for url in urls:
        driver.get(url)
        time.sleep(2)
        pat_xanthos = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/div[2]'
            '/div/div/div/div/div/div[1]/table/tbody/tr/td[3]/form/a'
        ).click()
        time.sleep(2)


def topaz():
    """
    Ежедневная глажка 5 Топазов.
    Есть вероятность получить 10 пропусков.
    :return:
    """
    urls = [
        'https://www.lowadi.com/elevage/fiche/?id=4763736',
        'https://www.lowadi.com/elevage/fiche/?id=4775333',
        'https://www.lowadi.com/elevage/fiche/?id=4771120',
        'https://www.lowadi.com/elevage/fiche/?id=4792032',
        'https://www.lowadi.com/elevage/fiche/?id=4789329'
    ]
    for url in urls:
        driver.get(url)
        time.sleep(2)
        pat_topaz = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/div[2]'
            '/div/div/div/div/div/div[1]/table/tbody/tr/td[3]/form/a'
        ).click()
        time.sleep(2)


def givre():
    """
    Ежедневная разморозка Морозницы.
    Есть вероятность получить Одеяло Гипноса.
    :return:
    """
    urls = [
        'https://www.lowadi.com/elevage/fiche/?id=12086505'
    ]
    for url in urls:
        driver.get(url)
        time.sleep(2)
        pat_givre = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/div[2]/'
            'div/div/div/div/div/div[1]/table/tbody/tr/td[3]/a'
        ).click()
        time.sleep(2)


def atelier():
    print(datetime.now().strftime('%H:%M:%S'), 'Проверяем мастерские..')
    url = 'https://www.lowadi.com/centre/atelier/'
    driver.get(url)
    try:
        for _ in range(2):
            try:
                get_stable_1 = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/form/table/tbody/tr[3]/td[6]/a/span'
                )
            except:
                get_stable_1 = driver.find_element(
                    By.XPATH,
                    '/html/body/div[8]/main/section/section/form/table/tbody/tr[3]/td[6]/a/span'
                )
            match get_stable_1.text:
                case 'Получить':
                    print('Стойла готовы, собираем')
                    get_stable_1.click()
                    time.sleep(2)
                    try:
                        driver.find_element(
                            By.XPATH,
                            '/html/body/div[11]/div/div/form/button/span/span/span'
                        ).click()
                    except:
                        driver.find_element(
                            By.XPATH,
                            '/html/body/div[12]/div/div/form/button/span/span/span'
                        ).click()
                    time.sleep(2)
                case 'Стоп':
                    print('Стойла не готовы, сваливаем')
                    return 0

        for _ in range(2):
            begin_stable = driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/form/table/tbody/tr[1]/td[6]/button/span/span/span'
            )
            match begin_stable.text:
                case 'Производство':
                    print('Мастерская свободна, пора запускать постройку стойла')
                    begin_stable.click()
                    time.sleep(2)
                    driver.find_element(
                        By.XPATH,
                        '/html/body/div[12]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]/div/span'
                    ).click()
                    time.sleep(2)
                    driver.find_element(
                        By.XPATH,
                        '/html/body/div[12]/div/div/div/div/div/div/div[2]/form[8]/div[2]/button/span/span/span'
                    ).click()
                    time.sleep(2)

    except:
        print('Проверка мастерской провалилась')


def check_equus():
    equus = int(driver.find_element(
        By.XPATH,
        '/html/body/div[7]/header/nav[1]/ul/li[8]/a/span/span[2]/strong'
    ).text.replace(' ', ''))

    if equus >= 10000:
        return 'Good'
    else:
        return 'Bad'


def buy_marshadore():
    check_ufo()
    equus = check_equus()

    while equus == 'Good':
        check_ufo()
        time.sleep(0.1)
        equus = check_equus()

        url = ['https://www.lowadi.com/marche/vente/?chevalType=&chevalEspece=any-all&unicorn=2&pegasus=2&'
               'amountComparaison=g&amount=0&currency=soft&competencesComparaison=g&competences=0&race-cheval=&'
               'race-poney=&race-ane=&race-cheval-trait=&race-all=78&race-cheval-pegase=&race-poney-pegase=&'
               'race-cheval-licorne=&race-poney-licorne=&race-cheval-licorne-ailee=&race-poney-licorne-ailee=&'
               'race-cheval-trait-pegase=&race-cheval-trait-licorne=&race-cheval-trait-licorne-ailee=&race-ane-pegase=&'
               'race-ane-licorne=&race-ane-licorne-ailee=&chevalTypeRace=78&aneRaceId=49&ageComparaison=g&age=0&'
               'uniteAge=ans&sexe=femelle&genetiqueComparaison=g&genetique=0&pierre-philosophale=2&sablier-chronos=2&'
               'bras-morphee=2&pommeOr=2&pommeOrDisparue=2&rayonHelios=2&lyre-apollon=2&5th-element=2&fragment=2&'
               'jouvence=2&pack-poseidon=2&eleveur=&excellenceComparaison=g&excellence=0&blupComparaison=g&blup=-100&'
               'purete=1&rall=&r58=&r38=&r43=&r31=&r60=&r30=&r41=&r75=&r32=&r61=&r45=&r33=&r71=&r53=&r63=&r74=&r72=&'
               'r57=&r40=&r46=&r50=&r78=&r47=&r55=&r56=&r76=&r39=&r49=&r36=&r66=&r64=&r59=&r51=&r42=&r77=&r73=&r65=&'
               'r34=&r70=&r35=&r48=&r52=&r44=&r37=&r54=&r67=&r62=&moisNaissance=0&anneeNaissance=0&gestation=2&'
               'nbSaillie=2&hasCompanion=2&affixe=2&mesEncheres=2&bookmarks=2&classique=2&western=2&enduranceComparaison=g&'
               'endurance=0&vitesseComparaison=g&vitesse=0&dressageComparaison=g&dressage=0&galopComparaison=g&galop=0&'
               'trotComparaison=g&trot=0&sautComparaison=g&saut=0&cVictoiresComparaison=g&cVictoires=0&cFlotsComparaison=g&'
               'cFlots=0&distinctionGP=2&pack-nyx=2&caresse-philotes=2&don-hestia=2&citrouille-ensorcelee=2&'
               'sceau-apocalypse=2&chapeau-magique=2&double-face=2&livre-monstres=2&trail-riding-diary=2&catrina-brooch=2&'
               'esprit-nomade=2&diamond-apple=2&pomme-vintage=2&iris-coat=2&button-braided-mane=2&tail-braid-1=2&'
               'parade-apple=2&alexandre-dumas-inkwell=2&arthur-conan-doyle-inkwell=2&heracles-horseshoes=2&cloches=2&'
               'cravache=2&eperons=2&longe=2&crampons=2&bride=&selle=&tapis=&bonnet=&bande=&search=0&noFilter=1&advanced=0&'
               'tri=amount&sens=ASC&submit=']
        driver.get(url[0])
        first_price = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[3]/table/tbody/tr[1]/td[9]'
        ).text.replace(' ', ''))

        if first_price <= 3000 and equus == 'Good':
            driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[3]/table/tbody/tr[1]/td[9]/div/div[1]'
             ).click()
            alert.accept()
        time.sleep(0.5)


def get_age_horse():
    age = driver.find_element(
        By.XPATH,
        '//*[@id="characteristics-body-content"]/table/tbody/tr[1]/td[2]'
    ).text.split()
    return age


def grow_up():
    grow_up = driver.find_element(
        By.XPATH,
        '//*[@id="boutonVieillir"]'
    ).click()
    time.sleep(1)
    try:
        agree = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[1]/div[2]/div/div/div[2]'
            '/div/div/div[2]/table/tbody/tr[2]/td/form/div/button/span/span/span'
        ).click()
    except:
        agree = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[1]/div[2]/div/div/div[2]'
            '/div/div/div[2]/table/tbody/tr[2]/td/form/div/button/span/span/span'
        ).click()


def get_doping():
    pat = driver.find_element(
        By.XPATH,
        '//*[@id="boutonCaresser"]'
    ).click()
    time.sleep(1)
    water = driver.find_element(
        By.XPATH,
        '//*[@id="boutonBoire"]'
    ).click()
    time.sleep(1)
    carrot = driver.find_element(
        By.XPATH,
        '//*[@id="boutonCarotte"]'
    ).click()
    time.sleep(1)
    mash = driver.find_element(
        By.XPATH,
        '//*[@id="boutonMash"]'
    ).click()
    time.sleep(1)


def blup_diet():
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(2)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(1)
    choice_hay = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[15]').click()
    time.sleep(1)
    choice_oats = driver.find_element(By.XPATH, '//*[@id="oatsSlider"]/ol/li[13]').click()
    time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)


def blup_montains(hour):
    choice_mountains = driver.find_element(
        By.XPATH,
        '//*[@id="boutonBalade-montagne"]'
    ).click()
    time.sleep(0.5)
    choice_hours = driver.find_element(
        By.XPATH,
        f'//*[@id="walkmontagneSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(0.5)
    train = driver.find_element(
        By.XPATH,
        '//*[@id="walk-montagne-submit"]/span/span/span'
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
            get_doping()
            hour = 1
            blup_montains(hour)
            grow_up()

            step += 1

    age = get_age_horse()

    if age == ['Возраст:', '2', 'года']:
        for i in range(11):
            hour = 11
            blup_montains(hour)
            get_doping()
            blup_diet()
            hour = 4
            blup_montains(hour)
            hour = 1
            blup_dressage(hour)
            grow_up()

            step += 1

    age = get_age_horse()

    if age == ['Возраст:', '4', 'года']:
        for i in range(3):
            hour = 13
            blup_speed(hour)
            get_doping()
            blup_diet()
            hour = 4
            blup_speed(hour)
            grow_up()

            step += 1

    age = get_age_horse()

    if age == ['Возраст:', '5', 'лет']:
        for i in range(3):
            hour = 20
            blup_dressage(hour)
            dressage -= hour
            get_doping()
            blup_diet()
            hour = 3
            blup_dressage(hour)
            dressage -= hour
            grow_up()

            step += 1


def refresh():
    driver.refresh()


def quit_lowadi():
    print(f'{datetime.now().strftime("%H:%M:%S")}: закрываем chrome')
    driver.quit()


if __name__ == '__main__':
    try:

        print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
        driver = newDRB()
        driver.set_window_size(1900, 1000)

    except:

        time.sleep(30)
        driver = newDRB()
        driver.set_window_size(1900, 1000)

    schedule.every().day.at(f'05:05').do(login_lowadi)
    schedule.every().day.at(f'05:{random.randint(10, 47)}').do(work_horse)
    schedule.every(1).hours.do(refresh)
    schedule.every(3).hours.do(atelier)

    while True:
        schedule.run_pending()
        time.sleep(1)


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
