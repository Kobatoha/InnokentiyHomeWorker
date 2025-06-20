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
from lowadi.states import *


class HorsesHandler:

    def __init__(self):
        self.driver = new_drb()
        self.driver.set_window_size(1400, 1300)

    @staticmethod
    def get_horses_list() -> list[list[str, str]]:
        return [
            ['heavyhorse', 'all'],
            # ['andalusian', 'unicorn'],

            ['francais', 'blup'],
            ['goland', 'blup'],
            ['andalusian', 'blup'],

            ['andalusian', 'basic'],
            ['andalusian', 'black'],
            ['andalusian', 'mouse'],
            ['andalusian', 'lava'],
            ['andalusian', 'creme'],
            ['andalusian', 'elite'],

            ['andalusian', 'north'],
            ['andalusian', 'male'],
            ['andalusian', 'reserve'],
            ['andalusian', 'color'],

            ['marshadore', 'female'],
            ['marshadore', 'male'],

            ['francais', 'garden'],
            ['francais', 'north'],

            ['goland', 'garden'],
            ['goland', 'north'],
        ]


def begin(driver):
    xanthos(driver)
    time.sleep(5)
    topaz(driver)
    time.sleep(5)
    givre(driver)


def create_driver_chrome():
    '''
    main comp + chrome
    '''
    print(f'{datetime.now().strftime("%H:%M:%S")}: запускаем chrome')
    driver = new_drb()
    driver.set_window_size(1400, 1300)

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

    print(f'Завод: {race.capitalize()} {sex.capitalize()}')

    current_url, horses = find_unworking_horse(driver, race, sex)
    not_training = ['unicorn', 'all']
    not_lesson = ['elite', 'garden', 'north']
    not_equip = []

    if not current_url:
        print('Все спят, гонять нечего <3')
        print('-' * 70)
        return

    driver.get(current_url)

    children = 0
    get_mating = 0
    stable = 0
    lesson = True
    competitions = 0
    n = 1
    time.sleep(2)
    print(f'Начинаем гонять: {race.capitalize()} {sex.capitalize()} - {horses} конях')

    while horses != 0:
        check_ufo(driver)
        time.sleep(1)

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

                name_race = get_name_race(driver)

                print(f'№{n} - [{name_race}]: {name}, начинаем уход.', *age)

                childbirth_without_stable(driver)

                equip = check_equip(driver)

                try:
                    if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                        print('Ваша кобыла скоро родит!')
                        call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                        time.sleep(1)
                        children += childbirth(driver, current_url, race, sex)
                except:
                    pass

                if not equip and not child_age(age) and sex not in not_training:
                    stable += get_stable_with_equip(driver, race)
                    driver.get(current_url)
                else:
                    stable += get_stable(driver)
                    time.sleep(2)
                    if 'centreOk' in driver.current_url:
                        driver.get(current_url)

                check_ufo(driver)

                clean = get_doping(driver)[-1].click()
                time.sleep(1)

                get_food(driver)

                get_sleep(driver)

                if sex not in not_lesson and lesson:
                    get_lesson(driver)

                    if 'заработок: 0' in get_history(driver, 'lesson') and lesson:
                        lesson = False
                        print('УРОЧНЫЙ ПРОГОН ОКОНЧЕН, можно врубать остальные заводы скакать')

                try:
                    if 'кобыла' in sex_horse:
                        if check_equus(driver) == 'Good':
                            spend_equus(driver, 'wood')
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
                            if race != 'marshadore':
                                choice_specialisation(driver)
                            else:
                                choice_specialisation(driver, 'western')
                            equiped_horse(driver, 'public')

                        energy = get_energy(driver)

                        try:
                            if lesson:

                                while energy >= 35:
                                    cost = choice_competition(driver, race)
                                    energy -= cost
                                    competitions += 1
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
                        next_horse(driver)
                    except:
                        driver.back()

            n += 1
            print('-' * 50)
            horses -= 1

    now = datetime.now().strftime('%d.%m %H:%M')
    print(f'\n{now} {race.capitalize()} {sex.capitalize()} прогон окончен\n-- Родилось жеребят: {children}\n-- Устроено случек: {get_mating}'
          f'\n-- Куплено стойл: {stable}\n-- Соревнований проведено: {competitions}\n')
    print('-' * 70)


def train_blup(driver, race='andalusian', sex='blup', child=False):
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

                blup_montains(driver, hour=11)
                for i in range(3):
                    get_doping(driver)[i].click()
                    time.sleep(1)
                get_doping(driver)[4].click()
                time.sleep(1)
                try:
                    blup_diet(driver)
                except:
                    get_food(driver)
                time.sleep(1)
                blup_montains(driver, hour=3)
                time.sleep(1)
                get_sleep(driver)
                time.sleep(1)
                grow_up(driver)

            elif training:
                try:
                    if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                        print('Ваша кобыла скоро родит!')
                        call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                        time.sleep(1)
                        childbirth(driver, current_url, race=race, sex=sex)
                except:
                    pass

                if child is True:
                    try:
                        for i in range(2):
                            female_reproduction(driver, race='andalusian', sex='blup', male_url=get_male_url)
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

                # competition_trot = 13.5

                count = int(energy // 13.5)

                for _ in range(count):
                    choice_competition(driver, race=race)
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


if __name__ == '__main__':
    try:
        driver = create_driver_chrome()
    except:
        pass

    login_lowadi(driver)
    tianma(driver)
    time.sleep(5)

    to_go_list = [
        ['heavyhorse', 'all'],
        # ['andalusian', 'unicorn'],

        ['francais', 'blup'],
        ['goland', 'blup'],
        ['andalusian', 'blup'],

        ['andalusian', 'basic'],
        ['andalusian', 'black'],
        ['andalusian', 'mouse'],
        ['andalusian', 'lava'],
        ['andalusian', 'creme'],
        ['andalusian', 'elite'],

        ['andalusian', 'north'],
        ['andalusian', 'male'],
        ['andalusian', 'reserve'],
        ['andalusian', 'color'],

        ['marshadore', 'female'],
        ['marshadore', 'male'],

        ['francais', 'garden'],
        ['francais', 'north'],

        ['goland', 'garden'],
        ['goland', 'north'],

    ]

    for to_go in to_go_list:
        run_horses(driver, to_go[0], to_go[1])

    try:
        begin(driver)
    except:
        print('Произошла ошибка где-то на уровно божков')
