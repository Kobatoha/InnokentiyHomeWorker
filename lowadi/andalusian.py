import pretty_errors
from lowadi.other import *
from lowadi.care import *
from lowadi.trade import *
from lowadi.training import *
from lowadi.reproduction import *


def andalusian_female(driver, horses=2000):
    print('Начинаем гонять лошадулек')
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=19637945'

    current_url, horses = find_unworking_horse(driver, 'andalusian', 'female')

    if not current_url:
        print('Все спят, гонять нечего <3')
        return

    driver.get(current_url)

    children = 0
    get_mating = 0
    stable = 0
    lesson = True
    n = 1
    time.sleep(5)

    while horses != 0:
        check_ufo(driver)
        time.sleep(2)
        if check_equus(driver) == 'Good':
            spend_equus(driver)
        if check_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Лошадь: {name}, уже получила уход.', *age)
            n += 1
            print('-' * 50)
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

                sex = get_sex(driver)

                childbirth_without_stable(driver)

                try:
                    stable += get_stable(driver)
                except:
                    pass

                if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                    milk_horse(driver, age, name, n)

                elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        fourrage_horse(driver, age, name, n)
                    try:
                        blup_montains(driver, hour=8)
                    except:
                        print('Еще не дорос до прогулок')
                    time.sleep(1)

                elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '4', 'мес.']:
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        young_horse(driver, age, name, n)
                    blup_montains(driver, hour=6)
                    get_doping(driver)[0].click()

                elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                    try:

                        if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                            print('Ваша кобыла скоро родит!')
                            call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                            time.sleep(1)
                            children += childbirth(driver, current_url, 'andalusian')

                    except:
                        pass

                    old_horse(driver, age, name, n)
                    if lesson:
                        get_lesson(driver)

                    if 'заработок: 0' in get_history(driver, 'lesson') and lesson:
                        lesson = False
                        print('УРОЧНЫЙ ПРОГОН ОКОНЧЕН, можно врубать остальные заводы скакать')

                    if 'кобыла' in sex:
                        get_mating += female_reproduction(driver)

                    time.sleep(1)
                    energy = get_energy(driver)
                    general_training(driver, energy)
                    if get_energy(driver) < 20:
                        get_doping(driver)[0].click()
                        time.sleep(1)
                        get_doping(driver)[1].click()
                        time.sleep(1)

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


def andalusian_male(driver, horses=300):
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=90938560'

    current_url = find_unworking_horse(driver, 'andalusian', 'male')

    if not current_url:
        print('Все спят, гонять нечего <3')
        return

    driver.get(current_url[0])

    post_mating = 0
    stable = 0
    n = 1
    time.sleep(5)

    while horses != 0:
        check_ufo(driver)
        time.sleep(2)
        if check_young_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Конь: {name}, уже получил уход.', *age)
            n += 1
            print('-' * 50)
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

                sex = get_sex(driver)

                try:
                    stable += get_stable(driver)
                except:
                    pass

                if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                    milk_horse(driver, age, name, n)

                elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        fourrage_horse(driver, age, name, n)

                        try:
                            blup_montains(driver, hour=8)
                        except:
                            print('Еще не дорос до прогулок')
                        time.sleep(1)

                elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '4', 'мес.']:
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        young_horse(driver, age, name, n)
                    blup_montains(driver, hour=6)
                    get_doping(driver)[0].click()

                elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                    get_doping(driver)[1].click()
                    time.sleep(1)

                    if 'конь' in sex:
                        post_mating += male_reproduction(driver)

                    get_food(driver)
                    time.sleep(1)
                    get_doping(driver)[4].click()
                    time.sleep(1)
                    get_sleep(driver)
                    time.sleep(1)

                    energy = get_energy(driver)
                    general_training(driver, energy)
                    if get_energy(driver) < 20:
                        get_doping(driver)[0].click()
                        time.sleep(1)
                        get_doping(driver)[1].click()
                        time.sleep(1)

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
    print(f'\n{now} прогон мужиков окончен\n-- Предложено случек: {post_mating}')


def andalusian_unicorn(driver, horses=50):
    print('Начинаем гонять лошадулек')
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=19637945'

    current_url = find_unworking_horse(driver, 'andalusian', 'unicorn')

    if not current_url:
        print('Все спят, гонять нечего <3')
        return

    driver.get(current_url)

    children = 0
    get_mating = 0
    post_mating = 0
    stable = 0

    n = 1
    time.sleep(5)

    while horses != 0:
        check_ufo(driver)
        time.sleep(2)

        if check_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Лошадь-единорог: {name}, уже получила уход.', *age)
            n += 1
            print('-' * 50)
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

                sex = get_sex(driver)

                childbirth_without_stable(driver)

                try:
                    stable += get_stable(driver)
                except:
                    pass

                if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                    milk_horse(driver, age, name, n)

                elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        fourrage_horse(driver, age, name, n)

                elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '4', 'мес.']:
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        young_horse(driver, age, name, n)

                elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                    try:

                        if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                            print('Ваша кобыла скоро родит!')
                            call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                            time.sleep(1)
                            children += childbirth(driver, current_url, 'unicorn')

                    except:
                        pass

                    old_horse(driver, age, name, n)
                    time.sleep(1)
                    get_lesson(driver)
                    time.sleep(1)

                    if 'кобыла' in sex:
                        get_mating += female_reproduction(driver, 'andalusian_unicorn')

                    elif 'конь' in sex:
                        post_mating += male_reproduction(driver, 'andalusian_unicorn')

                    time.sleep(1)

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
    print(f'\n{now} прогон единорожек окончен\n-- Родилось жеребят: {children}\n')


def andalusian_elite_female(driver, horses=100):
    print('Начинаем гонять элитных андалузочек')
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=90314563'

    current_url = find_unworking_horse(driver, 'andalusian_elite', 'female')

    if not current_url:
        print('Все спят, гонять нечего <3')
        return

    driver.get(current_url[0])

    children = 0
    get_mating = 0
    stable = 0

    n = 1
    time.sleep(5)

    while horses != 0:
        check_ufo(driver)
        time.sleep(2)
        if check_equus(driver) == 'Good':
            spend_equus(driver)
        if check_young_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Лошадь-элитный андалуз: {name}, уже получила уход.', *age)
            n += 1
            print('-' * 50)
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

                sex = get_sex(driver)

                childbirth_without_stable(driver)

                if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                    milk_horse(driver, age, name, n)

                elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                    fourrage_horse(driver, age, name, n)

                    try:
                        blup_montains(driver, hour=8)
                    except:
                        print('Еще не дорос до прогулок')
                    time.sleep(1)

                elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '4', 'мес.']:

                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        young_horse(driver, age, name, n)

                    blup_montains(driver, hour=6)
                    get_doping(driver)[0].click()

                elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                    try:

                        if driver.find_element(By.XPATH, '//*[@id="alerteVeterinaireContent"]/table/tbody/tr/td[2]'):
                            print('Ваша кобыла скоро родит!')
                            call_doctor = driver.find_element(By.XPATH, '//*[@id="boutonVeterinaire"]').click()
                            time.sleep(1)
                            children += childbirth(driver, current_url, 'andalusian_elite')

                    except:
                        pass

                    get_mating += female_reproduction(driver, 'andalusian')

                    get_doping(driver)[-1].click()
                    time.sleep(2)
                    get_food(driver)
                    get_sleep(driver)

                    energy = get_energy(driver)
                    general_training(driver, energy)
                    if get_energy(driver) < 20:
                        get_doping(driver)[0].click()
                        time.sleep(1)
                        get_doping(driver)[1].click()
                        time.sleep(1)

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
    print(f'\n{now} прогон элитных андалузок окончен\n-- Родилось жеребят: {children}\n-- Принято случек: {get_mating}'
          f'\n-- Куплено стойл: {stable}')


def andalusian_male_reserve(driver, horses=20):
    url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=92509117'

    current_url = find_unworking_horse(driver, 'andalusian_reserve', 'male')

    if not current_url:
        print('Все спят, гонять нечего <3')
        return

    driver.get(current_url[0])

    post_mating = 0
    stable = 0

    n = 1
    time.sleep(5)

    while horses != 0:
        check_ufo(driver)
        time.sleep(2)
        if check_young_horse_complete(driver):

            age = get_age_horse(driver)

            name = get_name_horse(driver)

            next_horse(driver)

            print(f'№{n} Конь-маршадор: {name}, уже получил уход.', *age)
            n += 1
            print('-' * 50)
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

                sex = get_sex(driver)

                try:
                    stable += get_stable(driver)
                except:
                    pass

                if 'несколько' in age or age == ['Возраст:', '2', 'мес.'] or age == ['Возраст:', '4', 'мес.']:
                    milk_horse(driver, age, name, n)

                elif (int(age[1]) < 2 and 'год' in age[2]) or (int(age[1]) >= 6 and age[2] == 'мес.'):
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        fourrage_horse(driver, age, name, n)

                        try:
                            blup_montains(driver, hour=8)
                        except:
                            print('Еще не дорос до прогулок')
                        time.sleep(1)

                elif age == ['Возраст:', '2', 'года'] or age == ['Возраст:', '2', 'года', '2', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '4', 'мес.']:
                    if check_young_horse_complete(driver):
                        next_horse(driver)
                    else:
                        young_horse(driver, age, name, n)
                    blup_montains(driver, hour=6)
                    get_doping(driver)[0].click()

                elif (int(age[1]) > 2 and age[2] != 'мес.') or age == ['Возраст:', '2', 'года', '6', 'мес.'] or age == \
                        ['Возраст:', '2', 'года', '8', 'мес.'] or age == ['Возраст:', '2', 'года', '10', 'мес.']:

                    get_doping(driver)[1].click()
                    time.sleep(1)

                    if 'конь' in sex:
                        post_mating += male_reproduction(driver)

                    get_doping(driver)[4].click()
                    time.sleep(1)
                    get_food(driver)
                    time.sleep(1)
                    get_sleep(driver)
                    time.sleep(1)

                    energy = get_energy(driver)
                    general_training(driver, energy)
                    if get_energy(driver) < 20:
                        get_doping(driver)[0].click()
                        time.sleep(1)
                        get_doping(driver)[1].click()
                        time.sleep(1)

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
    print(f'\n{now} прогон мужиков окончен\n-- Предложено случек: {post_mating}')


def train_blup(driver):
    name = get_name_horse(driver)
    age = get_age_horse(driver)
    race = 'andalusian'

    print(f'{datetime.now().strftime("%H:%M")} Начинаем качать [{name}] до 100 блюпа')

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

            elif not training:
                if not equip:
                    answer = input('Нужно снаряжение')
                    equip = True

                print(f'№{step} Взрослая лошадь: {name}, идем на соревнования.', *age)

                energy = get_energy(driver)
                competition_galop = 13.5

                count = int(energy // 13.5)

                for _ in range(count):
                    get_competition_galop(driver)
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
