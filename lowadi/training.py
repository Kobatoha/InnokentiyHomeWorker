import time
import pretty_errors
from selenium.webdriver.common.by import By
import re


def flag_train_complete(driver, train='speed'):
    discipline = {
        'speed': '//*[@id="training-tab-main"]/div/table/tbody/tr[2]/td[2]',
        'dressage': '//*[@id="training-tab-main"]/div/table/tbody/tr[3]/td[2]',
        'galop': '//*[@id="training-tab-main"]/div/table/tbody/tr[4]/td[2]'
    }
    find_flag = driver.find_element(
        By.XPATH,
        discipline[train]
    ).get_attribute('data-tooltip')
    if 'Тренировка завершена!' in find_flag:
        return 100
    else:
        flag = int(re.search(r'\b(?:100|\d{1,2})\b', find_flag).group())
        return flag


def flag_train_possible(driver, train='jump'):
    discipline = {
        'stamina': '//*[@id="training-tab-main"]/div/table/tbody/tr[1]/td[3]/button',
        'speed': '//*[@id="training-tab-main"]/div/table/tbody/tr[2]/td[3]/button',
        'dressage': '//*[@id="training-tab-main"]/div/table/tbody/tr[3]/td[3]/button',
        'galop': '//*[@id="training-tab-main"]/div/table/tbody/tr[4]/td[3]/button',
        'trot': '//*[@id="training-tab-main"]/div/table/tbody/tr[5]/td[3]/button',
        'jump': '//*[@id="training-tab-main"]/div/table/tbody/tr[6]/td[3]/button'

    }
    find_flag = driver.find_element(
        By.XPATH,
        discipline[train]
    ).get_attribute('data-tooltip')

    if not find_flag:
        return True
    elif 'ее больше нельзя обучать.' in find_flag:
        return False


def blup_montains(driver, hour):
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
    print(f'Погуляли в горах {hour/2} hours')
    time.sleep(2)


def blup_forest(driver, hour):
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
    print(f'Погуляли в лесу {hour} hours')
    time.sleep(2)


def blup_dressage(driver, hour):
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
    print(f'Тренировали выездку {hour} hours')
    time.sleep(2)


def blup_speed(driver, hour):
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
    print(f'Тренировали скорость {hour} hours')
    time.sleep(2)


def get_competition_galop(driver):
    click_competition = driver.find_element(
        By.XPATH,
        '//*[@id="competition-body-content"]/table/tbody/tr[1]/td[2]/a'
    ).click()
    time.sleep(2)
    run = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[8]/button/span/span/span'
    ).click()
    time.sleep(2)


def blup_galop(driver, hour):
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


def blup_step_forest(driver, forest=190):
    if 'лесу' in driver.find_element(
        By.XPATH,
        '//*[@id="center-tab-main"]/div[1]/table/tbody/tr[1]/td/div[2]/div/div[2]/a'
    ).get_attribute('data-tooltip'):
        forest = 95
    while forest != 0:
        clean = get_doping(driver)[4].click()
        time.sleep(1)

        hour = 11
        blup_forest(driver, hour)
        forest -= hour

        for i in range(4):
            get_doping(driver)[i].click()
            time.sleep(1)

        blup_diet()

        hour = 4
        blup_forest(driver, hour)
        forest -= hour

        grow_up(driver)
        time.sleep(2)


def general_training(driver, energy=20):
    if energy <= 29:
        print('Энергии слишком мало')
        return
    else:
        if not flag_train_possible(driver, 'jump'):
            print('Кобыла слишком жеребая, тренировка невозможна')
            return

    train_programm = ['speed', 'dressage', 'galop']

    speed = 8
    dressage = 5
    galop = 7

    flag = 100
    train = 'speed'

    for train in train_programm:
        flag = flag_train_complete(driver, train)
        time.sleep(0.5)
        if flag != 100:
            break

    if flag != 100:

        if train == 'speed':
            hour = (energy - 20) // speed
            if hour <= 100 - flag:
                blup_speed(driver, hour)
            else:
                hour = 100 - flag
                blup_speed(driver, hour)

        elif train == 'dressage':
            hour = (energy - 20) // dressage
            if hour <= 100 - flag:
                blup_dressage(driver, hour)
            else:
                hour = 100 - flag
                blup_dressage(driver, hour)

        elif train == 'galop':
            hour = (energy - 20) // galop
            if hour <= 100 - flag:
                blup_galop(driver, hour)
            else:
                hour = 100 - flag
                blup_galop(driver, hour)

    else:
        montains = 9
        hour = (energy - 20) // montains
        if not flag_montains_complete(driver):
            blup_montains(driver, hour)


    print(f'Проведена тренировка {train} на {hour / 2} hours')
    time.sleep(2)


def flag_montains_complete(driver):
    driver.find_element(
        By.XPATH,
        '//*[@id="boutonBalade-montagne"]'
    ).click()
    time.sleep(1)
    driver.find_element(
        By.XPATH,
        '//*[@id="walkmontagneSlider"]/ol/li[2]/span'
    ).click()
    skills = driver.find_element(
        By.XPATH,
        '//*[@id="walk-montagne-form"]/table/tbody/tr[2]/td/ul'
    ).text
    time.sleep(1)
    close = driver.find_element(
        By.XPATH,
        '//*[@id="agi-370662083001717443606"]/img'
    ).click()
    time.sleep(2)
    if '+' in skills:
        return False
    else:
        return True



def train_blup(driver):
    name = driver.find_element(
        By.XPATH,
        '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
    ).text
    gp = name.split()[1]
    age = get_age_horse(driver)
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

            grow_up(driver)
            step += 1

    age = get_age_horse()

    if age == ['Возраст:', '6', 'мес.']:
        wait_stable = input('Найди мне классное стойло с душем, поилкой, морковкой и комбикормом!')
        print('Спасибо, кек.')
        for i in range(6):
            fourrage_horse(name, age, step)
            grow_up(driver)
            step += 1
        print('Nice!')

    age = get_age_horse(driver)

    if age == ['Возраст:', '1', 'год', '6', 'мес.']:
        for i in range(3):
            hour = 12
            fourrage_horse(name, age, step)
            blup_montains(driver, hour)
            montains -= hour
            for j in range(4):
                get_doping(driver)[j].click()
                time.sleep(2)

            hour = 1
            blup_montains(driver, hour)
            montains -= hour
            grow_up(driver)

            step += 1

    age = get_age_horse(driver)

    if age == ['Возраст:', '2', 'года']:
        n = 0
        for i in range(5):
            print(n)
            hour = 11
            blup_montains(driver, hour)
            montains -= hour
            for j in range(4):
                get_doping(driver)[j].click()
                time.sleep(2)
            blup_diet(driver)
            hour = 4
            blup_montains(driver, hour)
            montains -= hour
            hour = 1
            blup_dressage(driver, hour)
            dressage -= hour
            grow_up(driver)

            step += 1
            n += 1

    age = get_age_horse(driver)

    if age == ['Возраст:', '2', 'года', '10', 'мес.']:
        for i in range(3):
            hour = 12
            blup_speed(driver, hour)
            speed -= hour
            for j in range(4):
                get_doping(driver)[j].click()
                time.sleep(2)
            blup_diet(driver)
            hour = 4
            blup_speed(driver, hour)
            speed -= hour
            grow_up(driver)

            step += 1

    age = get_age_horse(driver)

    if age == ['Возраст:', '5', 'лет']:
        for i in range(3):
            get_doping(driver)[4].click()
            time.sleep(2)
            hour = 20
            blup_dressage(driver, hour)
            dressage -= hour
            for j in range(3):
                get_doping(driver)[j].click()
                time.sleep(2)
            blup_diet(driver)
            hour = 4
            blup_dressage(driver, hour)
            dressage -= hour
            grow_up(driver)

            step += 1

    age = get_age_horse(driver)

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

        get_doping(driver)[0].click()
        time.sleep(2)
        get_doping(driver)[4].click()
        time.sleep(2)
        blup_diet(driver)
        grow_up(driver)

        step += 1

    age = get_age_horse(driver)

    if age == ['Возраст:', '5', 'лет', '6', 'мес.']:
        for i in range(5):
            get_doping(driver)[4].click()
            time.sleep(2)
            hour = 14
            blup_galop(driver, hour)
            galop -= hour
            for i in range(4):
                get_doping(driver)[i].click()
                time.sleep(2)
            blup_diet(driver)
            hour = 6
            blup_galop(driver, hour)
            galop -= hour
            grow_up(driver)

            step += 1
            time.sleep(2)

    age = get_age_horse(driver)

    if age == ['Возраст:', '8', 'лет', '6', 'мес.']:
        while competitions_trot != 0:
            for i in range(6):
                get_competition = driver.find_element(
                    By.XPATH,
                    '//*[@id="competition-body-content"]/table/tbody/tr[1]/td[1]/a'
                ).click()
                time.sleep(1)
                check_ufo(driver)
                run = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div/div/div[1]'
                    '/table/tbody/tr[1]/td[8]/button/span/span/span'
                ).click()
                competitions_trot -= 1
                time.sleep(2)

            get_doping(driver)[0].click()
            time.sleep(1)
            blup_diet(driver)
            grow_up(driver)

            step += 1
            time.sleep(2)

