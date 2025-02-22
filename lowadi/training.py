import time
import pretty_errors
from selenium.webdriver.common.by import By
import re
from lowadi.competitions import *


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
    try:
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
    except:
        print('Еще не дорос до прогулок')


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
        '//*[@id="training-trot-submit"]/span/span/span'
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


def get_train_program(race='andalusian'):
    train_program = {
        'andalusian': ['speed', 'dressage', 'galop'],
        'francais': ['speed', 'dressage', 'trot'],
        'goland': ['speed', 'dressage', 'jump'],
        'marshadore': ['stamina', 'speed', 'dressage'],
        'lusitanien': ['dressage', 'galop', 'trot']
    }
    return train_program[race]


def train_cost(train):
    costs = {
        'mountains': 9,
        'stamina': 8,
        'speed': 8,
        'dressage': 5,
        'galop': 7,
        'trot': 7,
        'jump': 7,
    }
    return costs[train]


def get_training(_type='speed'):
    train_types = {
        'stamina': blup_stamina,
        'speed': blup_speed,
        'dressage': blup_dressage,
        'galop': blup_galop,
        'trot': blup_trot,
        'jump': blup_jump,
    }
    return train_types[_type]


def general_training(driver, energy=20, race='andalusian'):
    if energy <= 29:
        print('Энергии слишком мало')
        return
    else:
        try:
            if not flag_train_possible(driver, 'jump'):
                print('Кобыла слишком жеребая, тренировка невозможна')
                return
        except:
            if 'close' in driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[3]/div/div/div'
            ).get_attribute('class'):
                print('Тренировки польностью закончены - молодец <3')
                return

    train_program = get_train_program(race)

    flag = 100
    train = 'speed'

    for train in train_program:
        flag = flag_train_complete(driver, train)
        time.sleep(0.5)
        if flag != 100:
            break

    if flag != 100:
        hour = (energy - 20) // train_cost(train)
        if hour <= 100 - flag:
            run_train = get_training(train)(driver, hour)
        else:
            hour = 100 - flag
            run_train = get_training(train)(driver, hour)

    else:
        hour = (energy - 20) // train_cost('mountains')
        if not flag_mountains_complete(driver):
            blup_montains(driver, hour)
        elif not flag_forest_complete(driver):
            blup_forest(driver, hour)

    time.sleep(2)


def blup_training(driver, energy=20, race='andalusian'):
    train_program = get_train_program(race)

    mountains = 8.1
    speed = 7.2
    dressage = 4.5
    galop = 6.3
    trot = 6.3
    jump = 6.3

    flag = 100
    hour = 0
    train = 'speed'

    for train in train_program:
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
        hour = energy // mountains

        if not flag_mountains_complete(driver):
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


def flag_mountains_complete(driver):
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


def train_blup(driver, race='andalusian', child=False, male_mating=''):
    name = get_name_horse(driver)
    age = get_age_horse(driver)

    print(f'{datetime.now().strftime("%H:%M")} Начинаем качать [{name}] до 100 блюпа')

    if child is True:
        if not male_mating:
            male_mating = input('Дайте ссылку на коня для случек')

    current_url = get_current_url(driver)
    driver.get(current_url)
    training = True
    competitions = 25
    equip = False
    complete = False

    step = 1
    time.sleep(1)

    while complete is not True:
        age = get_age_horse(driver)

        try:

            if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:

                milk_horse(driver, age, name, step)
                time.sleep(1)
                grow_up(driver)

            elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):

                try:
                    check_montains = driver.find_element(
                        By.XPATH,
                        '/html/body/div[8]/main/section/section/div[5]'
                        '/div/div[3]/div[1]/div/div/div/div/div/div[1]/div/div/div[3]/a'
                    )
                    print(f'№{step} Молодая лошадь: {name}, гуляем в горах.', *age)
                    blup_montains(driver, hour=11)

                    for i in range(3):
                        get_doping(driver)[i].click()
                        time.sleep(1)
                    get_doping(driver)[4].click()
                    time.sleep(1)
                    blup_diet(driver)
                    time.sleep(1)
                    blup_montains(driver, hour=3)
                    time.sleep(2)

                except:
                    fourrage_horse(driver, age, name, step)
                    time.sleep(1)
                    print('Еще не дорос до прогулок')

                time.sleep(1)
                grow_up(driver)

            elif training:
                try:
                    if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                        print('Ваша кобыла скоро родит!')
                        call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                        time.sleep(1)
                        childbirth(driver, current_url, race)
                except:
                    pass

                if child is True:
                    try:
                        for i in range(2):
                            female_reproduction(driver, f'{race}_blup', male_url=male_mating)
                            time.sleep(1)
                    except:
                        pass

                print(f'№{step} Взрослая лошадь: {name}, проводим тренировки.', *age)

                moral = get_moral(driver)

                if 100 > moral >= 94:
                    get_doping(driver)[4].click()
                    time.sleep(2)
                elif 100 > moral >= 84:
                    get_doping(driver)[4].click()
                    time.sleep(2)
                    get_doping(driver)[3].click()
                    time.sleep(2)
                elif 100 > moral >= 80:
                    get_doping(driver)[4].click()
                    time.sleep(2)
                    get_doping(driver)[3].click()
                    time.sleep(2)
                    get_doping(driver)[1].click()
                    time.sleep(2)

                energy = get_energy(driver)
                try:
                    message = blup_training(driver, energy, race)

                    if message == 'dressage':
                        for i in range(3):
                            get_doping(driver)[i].click()
                            time.sleep(2)
                        get_doping(driver)[4].click()
                        time.sleep(2)

                        blup_diet(driver)
                        get_sleep(driver)
                        try:
                            message = blup_dressage(driver, 4)
                        except:
                            energy = get_energy(driver)
                            message = blup_training(driver, energy - 20, race)

                    else:
                        for i in range(5):
                            get_doping(driver)[i].click()
                            time.sleep(2)

                        blup_diet(driver)
                        get_sleep(driver)
                        energy = get_energy(driver)
                        message = blup_training(driver, energy - 20, race)

                    if message in ['speed', 'dressage', 'galop', 'trot', 'jump']:
                        grow_up(driver)
                        training = True
                    elif 'Проведена тренировка' in message or 'Тренировали' in message:
                        grow_up(driver)
                        training = True
                    else:
                        training = False
                except:
                    print('Тренировка не случилась')
                    if driver.find_element(
                            By.XPATH,
                            '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
                    ).text == 'Эхография':
                        print('Слишком жеребая кобылка, урок, кушать и спать.')
                        get_lesson(driver)
                        time.sleep(1)
                        get_food(driver)
                        time.sleep(1)
                        get_doping(driver)[-1].click()
                        time.sleep(1)
                        get_sleep(driver)
                        time.sleep(1)
                        grow_up(driver)

            elif not training:
                if not equip:
                    answer = input('Нужно снаряжение')
                    equip = True

                print(f'№{step} Взрослая лошадь: {name}, идем на соревнования.', *age)

                energy = get_energy(driver)

                count = int(energy // 13.5)

                for _ in range(count):
                    choice_competition(driver, race)
                    competitions -= 1
                for i in range(2):
                    get_doping(driver)[i].click()
                    time.sleep(2)

                get_doping(driver)[-1].click()
                time.sleep(2)

                blup_diet(driver)
                time.sleep(2)

                grow_up(driver)

            skills = flag_complete_skill(driver, race)
            if 'complete' in skills[0] and 'complete' in skills[1] and 'complete' in skills[2]:
                complete = True

        except Exception as e:

            print('Некакая error при уходе за лошадью:', e, current_url)
            help = input('Нужна помощь Демиурга')

        step += 1

    now = datetime.now().strftime('%d.%m %H:%M')
    print(f'{now} кач окончен')
