from datetime import datetime
import time
from get_driver import new_drb, new_brave_dr
import pretty_errors
from lowadi.other import *
from lowadi.care import *
from lowadi.training import *
from lowadi.reproduction import *
from lowadi.competitions import *
from lowadi.divine import *


def begin(driver):
    xanthos(driver)
    time.sleep(5)
    topaz(driver)
    time.sleep(5)
    givre(driver)
    time.sleep(5)
    tianma(driver)


def create_driver_chrome():
    '''
    main comp + chrome
    '''
    print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
    driver = new_drb()
    driver.set_window_size(1400, 1300)
    login_lowadi(driver)

    return driver


def create_driver_brave():
    '''
    notebook + brave
    '''
    driver = new_brave_dr()
    driver.set_window_size(1400, 1360)
    login_lowadi(driver)

    return driver


def run_horses(driver, race='andalusian', sex='basic', horses=200) -> None:
    '''
    :param driver:
    :param race: andalusian, marshadore, francais, goland, lusitanien, heavyhorse
    :param sex:
    :param horses:
    :return:
    '''

    current_url, horses = find_unworking_horse(driver, race, sex)
    not_training = ['unicorn', 'all']
    not_lesson = ['elite']

    if not current_url:
        print('Все спят, гонять нечего <3')
        return

    driver.get(current_url)

    children = 0
    get_mating = 0
    stable = 0
    lesson = True
    n = 1
    time.sleep(2)
    print(f'Начинаем гонять: {race} {sex} - {horses} коняк')

    while horses != 0:
        check_ufo(driver)
        time.sleep(1)

        if check_equus(driver) == 'Good':
            spend_equus(driver, 'sand')

        if check_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Лошадь: {name}, уже получила уход.', *age)
            n += 1
            print('-' * 70)
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

                sex_horse = get_sex(driver)

                print(f'№{n} Лошадь: {name}, начинаем уход.', *age)

                childbirth_without_stable(driver)

                equip = check_equip(driver)

                try:
                    if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                        print('Ваша кобыла скоро родит!')
                        call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                        time.sleep(1)
                        children += childbirth(driver, current_url, race)
                except:
                    pass

                if not equip and not child_age(age):
                    stable += get_stable_with_equip(driver)
                else:
                    stable += get_stable(driver)

                clean = get_doping(driver)[-1].click()
                time.sleep(1)

                get_food(driver)

                get_sleep(driver)

                if race == 'andalusian' and sex not in not_lesson and lesson:
                    get_lesson(driver)

                    if 'заработок: 0' in get_history(driver, 'lesson') and lesson:
                        lesson = False
                        print('УРОЧНЫЙ ПРОГОН ОКОНЧЕН, можно врубать остальные заводы скакать')

                try:
                    if 'кобыла' in sex_horse:
                        get_mating += female_reproduction(driver, race, sex)
                    elif 'конь' in sex_horse:
                        get_mating += male_reproduction(driver, race, sex)
                except:
                    pass

                energy = get_energy(driver)
                try:
                    if sex not in not_training:
                        general_training(driver, energy, race)

                        if about_stable(driver) != 'Велосипед на рельсах':
                            choice_specialisation(driver)
                            equiped_horse(driver, 'public')

                        energy = get_energy(driver)

                        try:
                            if lesson:

                                while energy >= 35:
                                    cost = choice_competition(driver, race)
                                    energy -= cost
                                    time.sleep(1)

                                if get_energy(driver) < 20:
                                    get_doping(driver)[0].click()
                                    time.sleep(1)
                                    get_doping(driver)[1].click()
                                    time.sleep(1)

                        except:
                            pass
                except:
                    pass

                if energy >= 60:
                    get_lesson(driver)
                next_horse(driver)

            except Exception as e:

                print('Некакая error при уходе за лошадью:', e, current_url)
                try:
                    next_horse(driver)
                except:
                    try:
                        driver.get(current_url)
                    except:
                        driver.back()

            n += 1
            print('-' * 50)
            horses -= 1

    now = datetime.now().strftime('%d.%m %H:%M')
    print(f'\n{now} прогон окончен\n-- Родилось жеребят: {children}\n-- Принято случек: {get_mating}'
          f'\n-- Куплено стойл: {stable}')
