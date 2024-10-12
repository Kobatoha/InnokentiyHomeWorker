import time
import pretty_errors
from selenium.webdriver.common.by import By
import re
from competitions import *


def flag_train_complete(driver, train='speed'):
    discipline = {
        'stamina': '//*[@id="training-tab-main"]/div/table/tbody/tr[1]/td[2]',
        'speed': '//*[@id="training-tab-main"]/div/table/tbody/tr[2]/td[2]',
        'dressage': '//*[@id="training-tab-main"]/div/table/tbody/tr[3]/td[2]',
        'galop': '//*[@id="training-tab-main"]/div/table/tbody/tr[4]/td[2]',
        'trot': '//*[@id="training-tab-main"]/div/table/tbody/tr[5]/td[2]',
        'jump': '//*[@id="training-tab-main"]/div/table/tbody/tr[6]/td[2]',
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
    print(f'Погуляли в горах {hour / 2} hours')
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
    print(f'Погуляли в лесу {hour / 2} hours')
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

    if hour >= 21:
        hour = 20

    click_dressage = driver.find_element(
        By.XPATH,
        f'//*[@id="trainingDressageSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(1)

    train = driver.find_element(
        By.XPATH,
        '//*[@id="training-dressage-submit"]/span/span/span'
    ).click()
    message = f'Тренировали выездку {hour / 2} hours'
    print(message)
    time.sleep(2)

    return message


def blup_stamina(driver, hour):
    try:
        choice_stamina = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[1]/td[3]/button/span'
        ).click()
        time.sleep(1)
    except:
        choice_stamina = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[1]/td[3]/button/span'
        ).click()
        time.sleep(1)

    click_stamina = driver.find_element(
        By.XPATH,
        f'//*[@id="trainingEnduranceSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(1)

    train = driver.find_element(
        By.XPATH,
        '//*[@id="training-endurance-submit"]/span/span/span'
    ).click()
    print(f'Тренировали выносливость {hour/2} hours')
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
    print(f'Тренировали скорость {hour/2} hours')
    time.sleep(2)


def choice_competition(driver, race='andalusian'):
    if race == 'andalusian':
        get_competition_galop(driver)
    elif race == 'francy':
        get_competition_trot(driver)
    elif race == 'goland':
        get_competition_jump(driver)


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
    print(f'Тренировали галоп {hour / 2} hours')
    time.sleep(2)


def blup_trot(driver, hour):
    try:
        choice_trot = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[5]/td[3]/button/span'
        ).click()
        time.sleep(1)
    except:
        choice_trot = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[5]/td[3]/button/span'
        ).click()
        time.sleep(1)

    click_trot = driver.find_element(
        By.XPATH,
        f'//*[@id="trainingTrotSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(1)

    train = driver.find_element(
        By.XPATH,
        '//*[@id="training-tort-submit"]/span/span/span'
    ).click()
    print(f'Тренировали рысь {hour / 2} hours')
    time.sleep(2)


def blup_jump(driver, hour):
    try:
        choice_jump = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[6]/td[3]/button/span'
        ).click()
        time.sleep(1)
    except:
        choice_jump = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div/div/div'
            '/div[1]/div/table/tbody/tr[6]/td[3]/button/span'
        ).click()
        time.sleep(1)

    click_jump = driver.find_element(
        By.XPATH,
        f'//*[@id="trainingSautSlider"]/ol/li[{hour + 1}]'
    ).click()
    time.sleep(1)

    train = driver.find_element(
        By.XPATH,
        '//*[@id="training-saut-submit"]/span/span/span'
    ).click()
    print(f'Тренировали прыжки {hour / 2} hours')
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

    montains = 9
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
        hour = (energy - 20) // montains
        if not flag_montains_complete(driver):
            blup_montains(driver, hour)
        elif not flag_forest_complete(driver):
            blup_forest(driver, hour)


    print(f'Проведена тренировка {train} на {hour / 2} hours')
    time.sleep(2)


def general_training_marshadore(driver, energy=20):
    if energy <= 29:
        print('Энергии слишком мало')
        return
    else:
        if not flag_train_possible(driver, 'jump'):
            print('Кобыла слишком жеребая, тренировка невозможна')
            return

    train_programm = ['stamina', 'speed', 'dressage']

    montains = 9
    stamina = 8
    speed = 8
    dressage = 5

    flag = 100
    train = 'stamina'

    for train in train_programm:
        flag = flag_train_complete(driver, train)
        time.sleep(0.5)
        if flag != 100:
            break

    if flag != 100:

        if train == 'stamina':
            hour = (energy - 20) // stamina
            if hour <= 100 - flag:
                blup_stamina(driver, hour)
            else:
                hour = 100 - flag
                blup_stamina(driver, hour)

        elif train == 'speed':
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

    else:
        hour = (energy - 20) // montains
        if not flag_montains_complete(driver):
            blup_montains(driver, hour)
        elif not flag_forest_complete(driver):
            blup_forest(driver, hour)

    print(f'Проведена тренировка {train} на {hour / 2} hours')
    time.sleep(2)


def blup_training(driver, energy=20, race='andalusian'):
    if race == 'andalusian':
        train_programm = ['speed', 'dressage', 'galop']
    elif race == 'francy':
        train_programm = ['speed', 'dressage', 'trot']
    elif race == 'goland':
        train_programm = ['speed', 'dressage', 'jump']

    montains = 8.1
    speed = 7.2
    dressage = 4.5
    galop = 6.3
    trot = 6.3
    jump = 6.3

    flag = 100
    hour = 0
    train = 'speed'

    for train in train_programm:
        flag = flag_train_complete(driver, train)
        time.sleep(0.5)
        if flag != 100:
            break

    if flag != 100:

        if train == 'speed':
            hour = energy // speed
            if hour <= 100 - flag:
                blup_speed(driver, hour)
            else:
                hour = 100 - flag
                blup_speed(driver, hour)

        elif train == 'dressage':
            hour = energy // dressage
            if hour <= 100 - flag:
                blup_dressage(driver, hour)
            else:
                hour = 100 - flag
                blup_dressage(driver, hour)

        elif train == 'galop':
            hour = energy // galop
            if hour <= 100 - flag:
                blup_galop(driver, hour)
            else:
                hour = 100 - flag
                blup_galop(driver, hour)

        elif train == 'trot':
            hour = energy // trot
            if hour <= 100 - flag:
                blup_trot(driver, hour)
            else:
                hour = 100 - flag
                blup_trot(driver, hour)

        elif train == 'jump':
            hour = energy // jump
            if hour <= 100 - flag:
                blup_jump(driver, hour)
            else:
                hour = 100 - flag
                blup_jump(driver, hour)

        return train

    else:
        hour = energy // montains

        if not flag_montains_complete(driver):
            blup_montains(driver, hour)
        elif not flag_forest_complete(driver):
            blup_forest(driver, hour)
        else:
            hour = 0
            train = ''
    if train and hour:
        message = f'Проведена тренировка {train} на {hour / 2} hours'
    else:
        message = f'Тренировка не требуется - скорость, выездка, галоп, горы и лес успешно пройдены'
    time.sleep(2)
    return message


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
    try:
        close = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]'
            '/div[2]/div/div/div/div/div/div[3]/table/tbody/tr[1]/td[2]/a/img'
        ).click()
    except:
        close = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[3]'
            '/div[2]/div/div/div/div/div/div[3]/table/tbody/tr[1]/td[2]/a/img'
        ).click()
    time.sleep(2)
    if '+' in skills:
        return False
    else:
        return True


def flag_forest_complete(driver):
    driver.find_element(
        By.XPATH,
        '//*[@id="boutonBalade-foret"]'
    ).click()
    time.sleep(1)
    driver.find_element(
        By.XPATH,
        '//*[@id="walkforetSlider"]/ol/li[2]/span'
    ).click()
    skills = driver.find_element(
        By.XPATH,
        '//*[@id="walk-foret-form"]/table/tbody/tr[2]/td/ul'
    ).text
    time.sleep(1)
    try:
        close = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]'
            '/div/div[3]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/a/img'
        ).click()
    except:
        close = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]'
            '/div/div[3]/div[2]/div/div/div/div/div/div[2]/table/tbody/tr[1]/td[2]/a/img'
        ).click()
    time.sleep(2)
    if '+' in skills:
        return False
    else:
        return True


def flag_complete_skill(driver, race):
    div = [7, 8, 9]
    for num in div:
        try:
            stamina = driver.find_element(
                By.XPATH,
                f'/html/body/div[{num}]/main/section/section/div[5]/div/div[2]/div[3]/div/div/div/div/table/tbody'
                f'/tr[1]/td[1]'
            ).get_attribute('class')

            speed = driver.find_element(
                By.XPATH,
                f'/html/body/div[{num}]/main/section/section/div[5]/div/div[2]/div[3]/div/div/div/div/table/tbody'
                f'/tr[2]/td[1]'
            ).get_attribute('class')

            dressage = driver.find_element(
                By.XPATH,
                f'/html/body/div[{num}]/main/section/section/div[5]/div/div[2]/div[3]/div/div/div/div/table/tbody'
                f'/tr[3]/td[1]'
            ).get_attribute('class')

            galop = driver.find_element(
                By.XPATH,
                f'/html/body/div[{num}]/main/section/section/div[5]/div/div[2]/div[3]/div/div/div/div/table/tbody'
                f'/tr[4]/td[1]'
            ).get_attribute('class')

            trot = driver.find_element(
                By.XPATH,
                f'/html/body/div[{num}]/main/section/section/div[5]/div/div[2]/div[3]/div/div/div/div/table/tbody'
                f'/tr[5]/td[1]'
            ).get_attribute('class')

            jump = driver.find_element(
                By.XPATH,
                f'/html/body/div[{num}]/main/section/section/div[5]/div/div[2]/div[3]/div/div/div/div/table/tbody'
                f'/tr[6]/td[1]'
            ).get_attribute('class')

            if race == 'andalusian':
                return [speed, dressage, galop]
            elif race == 'marshadore':
                return [stamina, speed, dressage]
            elif race == 'curly':
                return [stamina, speed, trot]
            elif race == 'goland':
                return [speed, dressage, jump]

        except:
            pass

