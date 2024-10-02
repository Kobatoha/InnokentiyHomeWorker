import time

import pretty_errors
from lowadi.other import *
from lowadi.care import *
from lowadi.trade import *
from lowadi.training import *
from lowadi.reproduction import *


def train_blup(driver, race='francy', child=False):
    name = get_name_horse(driver)
    age = get_age_horse(driver)

    print(f'{datetime.now().strftime("%H:%M")} Начинаем качать [{name}] до 100 блюпа')

    if child is True:
        get_male_url = input('Дайте ссылку на коня для случек, если нет своего коня - нажмите Enter')
        if not get_male_url:
            get_male_url = False

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
                print(f'№{step} Молодая лошадь: {name}, гуляем в горах.', *age)

                try:
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
                        childbirth(driver, current_url, race='andalusian_blup')
                except:
                    pass

                if child is True:
                    try:
                        for i in range(2):
                            female_reproduction(driver, race='francais_blup', male_url=get_male_url)
                            time.sleep(1)
                    except:
                        print('Еще не время для любви')

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

                    if 'speed' in message or 'dressage' in message or 'galop' in message:
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
                competition_trot = 13.5

                count = int(energy // 13.5)

                for _ in range(count):
                    get_competition_trot(driver)
                    competitions -= 1
                for i in range(2):
                    get_doping(driver)[i].click()
                    time.sleep(2)

                get_doping(driver)[-1].click()
                time.sleep(2)

                blup_diet(driver)
                time.sleep(2)

                grow_up(driver)

            skills = flag_complete_skill(driver, 'andalusian')
            if 'complete' in skills[0] and 'complete' in skills[1] and 'complete' in skills[2]:
                complete = True

        except Exception as e:

            print('Некакая error при уходе за лошадью:', e, current_url)
            help = input('Нужна помощь Демиурга')

        step += 1

    now = datetime.now().strftime('%d.%m %H:%M')
    print(f'{now} кач окончен')
