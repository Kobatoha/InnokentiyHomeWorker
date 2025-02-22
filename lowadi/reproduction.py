import time
import os
import pretty_errors
from selenium.webdriver.common.by import By
from lowadi.other import check_ufo
from lowadi.care import get_name_horse, get_energy, push_mating_for_name, get_color, andalusian_male_color_mating


def ready_matt(driver):
    try:
        not_ready = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-body-content"]/div[1]/table/tbody/tr[1]/td'
        ).text
        print(not_ready)
        time.sleep(1)

        return False

    except:

        if driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Случить кобылу':
            print('Подходящий возраст, нужна случка!')
            return [True, 0]

        elif driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Открытые случки':

            print('Кобыле продложена случка')

            return [True, 1]

        elif driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Эхография':

            print('Кобыла уже жеребая')
            time.sleep(1)

            return False


def female_reproduction(driver, race='andalusian', sex='basic', male_url=None):
    matting = ready_matt(driver)

    cap_text = f'[{race.capitalize()} {sex.capitalize()}]'

    if matting and matting[1] == 1:

        if race == 'andalusian':
            if sex == 'elite':
                male_name = driver.find_element(
                    By.XPATH,
                    '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
                ).text
                print(f'[Andalusian Elite] Принимаем случку от {male_name}')
                try:
                    ok = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
                    ).click()
                except:
                    ok = driver.find_element(
                        By.XPATH,
                        '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
                    ).click()

                check_ufo(driver)

                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)

                print('[Andalusian Elite] Кобыла успешно приняла предложенную случку')
                time.sleep(1)

                return 1

            elif sex == 'creme':
                male_name = driver.find_element(
                    By.XPATH,
                    '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
                ).text
                print(f'[Andalusian Creme] Принимаем случку от {male_name}')

                ok = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
                ).click()

                check_ufo(driver)

                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)

                print('[Andalusian Creme] Кобыла успешно приняла предложенную случку')
                time.sleep(1)

                return 1

            elif sex == 'lava':
                male_name = driver.find_element(
                    By.XPATH,
                    '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
                ).text
                print(f'[Andalusian Lava] Принимаем случку от {male_name}')

                ok = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
                ).click()

                check_ufo(driver)

                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)

                print('[Andalusian Lava] Кобыла успешно приняла предложенную случку')
                time.sleep(1)

                return 1

            elif sex == 'blup':
                male_name = driver.find_element(
                    By.XPATH,
                    '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
                ).text
                print(f'[Andalusian Blup] Принимаем случку от {male_name}')

                ok = driver.find_element(
                    By.XPATH,
                    '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
                ).click()

                check_ufo(driver)

                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)

                print('[Andalusian Blup] Кобыла успешно приняла предложенную случку')
                time.sleep(1)

                return 1

            elif sex == 'unicorn':
                pass

        elif race == 'marshadore':
            if sex == 'female':
                male_name = driver.find_element(
                    By.XPATH,
                    '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
                ).text
                print(f'[Marshadore] Принимаем случку от {male_name}')

                ok = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
                ).click()

                check_ufo(driver)

                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)

                print('[Marshadore] Кобыла успешно приняла предложенную случку')
                time.sleep(1)

                return 1

        elif race == 'francais':
            if sex == 'garden':
                male_name = driver.find_element(
                    By.XPATH,
                    '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
                ).text
                print(f'{cap_text} Принимаем случку от {male_name}')

                ok = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
                ).click()

                check_ufo(driver)

                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)

                print(f'{cap_text} Кобыла успешно приняла предложенную случку')
                time.sleep(1)

                return 1

        elif race == 'goland':
            if sex == 'garden':
                male_name = driver.find_element(
                    By.XPATH,
                    '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
                ).text
                print(f'{cap_text} Принимаем случку от {male_name}')

                ok = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
                ).click()

                check_ufo(driver)

                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)

                print(f'{cap_text} Кобыла успешно приняла предложенную случку')
                time.sleep(1)

                return 1

    elif matting and matting[1] == 0:

        if race == 'andalusian':
            if sex == 'basic':
                print('В эфире обычная андалузка, идем на брачный рынок..')
                check_ufo(driver)
                driver.find_element(By.XPATH, '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]/a').click()
                time.sleep(1)
                master = driver.find_element(By.XPATH, '//*[@id="breeder"]').send_keys('Kolgotki')
                time.sleep(1)
                get_offers = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/form/button[1]/span/span'
                ).click()
                time.sleep(1)
                gp_sort = driver.find_element(By.XPATH, '//*[@id="table-0"]/thead/tr/td[4]/div/a').click()
                time.sleep(1)
                get_mating = driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[8]/a').click()
                time.sleep(1)

                if 'Kolgotki' in driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[2]').text:
                    mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                    time.sleep(1)

                print(f'{cap_text} Кобыла успешно провела случку')
                time.sleep(1)

                return 1

            elif sex == 'black':
                print('В эфире черная андалузка, идем на брачный рынок..')
                check_ufo(driver)
                driver.find_element(By.XPATH, '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]/a').click()
                time.sleep(1)
                master = driver.find_element(By.XPATH, '//*[@id="breeder"]').send_keys('Kolgotki')
                time.sleep(1)
                get_offers = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/form/button[1]/span/span'
                ).click()
                time.sleep(1)
                gp_sort = driver.find_element(By.XPATH, '//*[@id="table-0"]/thead/tr/td[4]/div/a').click()
                time.sleep(1)
                get_mating = driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[8]/a').click()
                time.sleep(1)

                if 'Kolgotki' in driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[2]').text:
                    mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                    time.sleep(1)

                print(f'{cap_text} Кобыла успешно провела случку')
                time.sleep(1)

                return 1

            elif sex == 'mouse':
                print('В эфире мышиная андалузка, идем на брачный рынок..')
                check_ufo(driver)
                driver.find_element(By.XPATH, '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]/a').click()
                time.sleep(1)
                master = driver.find_element(By.XPATH, '//*[@id="breeder"]').send_keys('Kolgotki')
                time.sleep(1)
                get_offers = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/form/button[1]/span/span'
                ).click()
                time.sleep(1)
                gp_sort = driver.find_element(By.XPATH, '//*[@id="table-0"]/thead/tr/td[4]/div/a').click()
                time.sleep(1)
                get_mating = driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[8]/a').click()
                time.sleep(1)

                if 'Kolgotki' in driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[2]').text:
                    mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                    time.sleep(1)

                print(f'{cap_text} Кобыла успешно провела случку')
                time.sleep(1)

                return 1

            elif sex == 'creme':
                name = get_name_horse(driver)
                color = get_color(driver)
                creme = ''

                if color == 'Соловая (Паломино)':
                    creme = 'palomino'
                elif color == 'Кремелло':
                    creme = 'cremello'

                try:
                    with open(f'lowadi/Lists of horses/andalusian_{creme}.txt', 'r') as file:
                        names = file.readlines()
                except FileNotFoundError:
                    with open(f'lowadi/Lists of horses/andalusian_{creme}.txt', 'w') as file:
                        pass
                    with open(f'lowadi/Lists of horses/andalusian_{creme}.txt', 'r') as file:
                        names = file.readlines()

                if name + '\n' not in names:
                    with open(f'lowadi/Lists of horses/andalusian_{creme}.txt', 'a') as file:
                        file.write(name + '\n')

                    print(f'{cap_text} Добавлена в очередь на ожидание случки')
                else:
                    print(f'{cap_text} Уже в очереди на ожидание случки')

                return 0

            elif sex == 'lava':
                name = get_name_horse(driver)
                color = get_color(driver)
                lava = ''

                if color == 'Огненно-рыжая с лавовой гривой':
                    lava = 'fire-red'
                elif color == 'Рыжая с лавовой гривой':
                    lava = 'red'

                try:
                    with open(f'lowadi/Lists of horses/andalusian_{lava}.txt', 'r') as file:
                        names = file.readlines()
                except FileNotFoundError:
                    with open(f'lowadi/Lists of horses/andalusian_{lava}.txt', 'w') as file:
                        pass
                    with open(f'lowadi/Lists of horses/andalusian_{lava}.txt', 'r') as file:
                        names = file.readlines()

                if name + '\n' not in names:
                    with open(f'lowadi/Lists of horses/andalusian_{lava}.txt', 'a') as file:
                        file.write(name + '\n')

                    print(f'{cap_text} Добавлена в очередь на ожидание случки')
                else:
                    print(f'{cap_text} Уже в очереди на ожидание случки')

                return 0

            elif sex == 'elite':
                name = get_name_horse(driver)

                try:
                    with open('lowadi/Lists of horses/andalusian.txt', 'r') as file:
                        names = file.readlines()
                except FileNotFoundError:
                    with open(f'lowadi/Lists of horses/andalusian.txt', 'w') as file:
                        pass
                    with open(f'lowadi/Lists of horses/andalusian.txt.txt', 'r') as file:
                        names = file.readlines()

                if name + '\n' not in names:
                    with open('lowadi/Lists of horses/andalusian.txt', 'a') as file:
                        file.write(name + '\n')

                    print(f'{cap_text} Добавлена в очередь на ожидание случки')
                else:
                    print(f'{cap_text} Уже в очереди на ожидание случки')

                return 0

            elif sex == 'blup':
                name = get_name_horse(driver)

                if male_url:
                    driver.get(male_url)
                    push_mating_for_name(driver, name)
                    driver.back()

                    print(f'[{race.capitalize()} {sex.capitalize()}] Случка прокинута на кобылу')
                else:
                    print(f'[{race.capitalize()} {sex.capitalize()}] Нет ссылки на коня')
                    try:
                        with open(f'lowadi/Lists of horses/andalusian_{sex}.txt', 'r') as file:
                            names = file.readlines()
                    except FileNotFoundError:
                        with open(f'lowadi/Lists of horses/andalusian_{sex}.txt', 'w') as file:
                            pass
                        with open(f'lowadi/Lists of horses/andalusian_{sex}.txt', 'r') as file:
                            names = file.readlines()

                    if name + '\n' not in names:
                        with open(f'lowadi/Lists of horses/andalusian_{sex}.txt', 'a') as file:
                            file.write(name + '\n')

                        print(f'{cap_text} Добавлена в очередь на ожидание случки')
                    else:
                        print(f'{cap_text} Уже в очереди на ожидание случки')

                return 0

            elif sex == 'unicorn':
                name = get_name_horse(driver)

                try:
                    with open('lowadi/Lists of horses/andalusian_unicorn.txt', 'r') as file:
                        names = file.readlines()
                except FileNotFoundError:
                    with open(f'lowadi/Lists of horses/andalusian_unicorn.txt', 'w') as file:
                        pass
                    with open(f'lowadi/Lists of horses/andalusian_unicorn.txt', 'r') as file:
                        names = file.readlines()

                if name + '\n' not in names:
                    with open('lowadi/Lists of horses/andalusian_unicorn.txt', 'a') as file:
                        file.write(name + '\n')

                    print(f'{cap_text} Добавлена в очередь на ожидание случки')
                else:
                    print(f'{cap_text} Уже в очереди на ожидание случки')

                return 0

        elif race == 'francais':
            if sex == 'blup':

                if male_url:
                    name = get_name_horse(driver)
                    driver.get(male_url)
                    push_mating_for_name(driver, name)
                    driver.back()

                    print(f'{cap_text} Случка прокинута на кобылу')
                else:
                    print(f'{cap_text} Нет ссылки на коня, давайте сами')
                    time.sleep(60 * 5)

            elif sex == 'garden':
                name = get_name_horse(driver)

                try:
                    with open('lowadi/Lists of horses/francais_garden.txt', 'r') as file:
                        names = file.readlines()
                except FileNotFoundError:
                    with open(f'lowadi/Lists of horses/francais_garden.txt', 'w') as file:
                        pass
                    with open(f'lowadi/Lists of horses/francais_garden.txt', 'r') as file:
                        names = file.readlines()

                if name + '\n' not in names:
                    with open('lowadi/Lists of horses/francais_garden.txt', 'a') as file:
                        file.write(name + '\n')

                    print(f'{cap_text} Добавлена в очередь на ожидание случки')
                else:
                    print(f'{cap_text} Уже в очереди на ожидание случки')

                return 0

        elif race == 'goland':
            if sex == 'blup':
                if male_url:
                    name = get_name_horse(driver)
                    driver.get(male_url)
                    push_mating_for_name(driver, name)
                    driver.back()

                    print(f'{cap_text} Случка прокинута на кобылу')
                else:
                    print(f'{cap_text} Нет ссылки на коня, давайте сами')
                    time.sleep(60 * 5)

            elif sex == 'garden':
                name = get_name_horse(driver)

                try:
                    with open('lowadi/Lists of horses/goland_garden.txt', 'r') as file:
                        names = file.readlines()
                except FileNotFoundError:
                    with open(f'lowadi/Lists of horses/goland_garden.txt', 'w') as file:
                        pass
                    with open(f'lowadi/Lists of horses/goland_garden.txt', 'r') as file:
                        names = file.readlines()

                if name + '\n' not in names:
                    with open('lowadi/Lists of horses/goland_garden.txt', 'a') as file:
                        file.write(name + '\n')

                    print(f'{cap_text} Добавлена в очередь на ожидание случки')
                else:
                    print(f'{cap_text} Уже в очереди на ожидание случки')

                return 0

        elif race == 'marshadore':
            if sex == 'female':
                name = get_name_horse(driver)

                try:
                    with open(f'lowadi/Lists of horses/marshadore.txt', 'r') as file:
                        names = file.readlines()
                except FileNotFoundError:
                    with open(f'lowadi/Lists of horses/marshadore.txt', 'w') as file:
                        pass
                    with open(f'lowadi/Lists of horses/marshadore.txt', 'r') as file:
                        names = file.readlines()

                if name + '\n' not in names:
                    with open('lowadi/Lists of horses/marshadore.txt', 'a') as file:
                        file.write(name + '\n')

                    print(f'{cap_text} Добавлена в очередь на ожидание случки')
                else:
                    print(f'{cap_text} Уже в очереди на ожидание случки')

                return 0

    else:
        return 0


def male_reproduction(driver, race='andalusian', sex='male'):
    if race == 'andalusian' and sex != 'unicorn' and sex != 'north' and sex != 'reserve':
        sex = andalusian_male_color_mating(driver)

    lists_reproductions = {
        'andalusian': {
            'reserve': 'lowadi/Lists of horses/andalusian.txt',
            'unicorn': 'lowadi/Lists of horses/andalusian_unicorn.txt',
            'palomino': 'lowadi/Lists of horses/andalusian_palomino.txt',
            'cremello': 'lowadi/Lists of horses/andalusian_cremello.txt',
            'red': 'lowadi/Lists of horses/andalusian_red.txt',
            'fire_red': 'lowadi/Lists of horses/andalusian_fire-red.txt',
            'north': 'lowadi/Lists of horses/andalusian_blup.txt'
        },
        'marshadore': {
            'male': 'lowadi/Lists of horses/marshadore.txt'
        },
        'francais': {
            'north': 'lowadi/Lists of horses/francais_garden.txt'
        },
        'goland': {
            'north': 'lowadi/Lists of horses/goland_garden.txt'
        }
    }

    second_lists_reproductions = {
        'andalusian': {
            'north': 'lowadi/Lists of horses/andalusian.txt',
        },
        'francais': {
            'north': 'lowadi/Lists of horses/francais_blup.txt'
        },
        'goland': {
            'north': 'lowadi/Lists of horses/goland_blup.txt'
        }
    }

    time.sleep(1)
    mating = 25
    num = 0
    name = get_name_horse(driver)
    gp = int(name.split()[1][:-3])
    energy = get_energy(driver)
    count = energy // mating
    if race == 'andalusian' and sex == 'male':
        try:
            while count != 0:
                create_mating = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[3]/a'
                ).click()
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

                if gp >= 21000:
                    male_reproduction(driver, 'andalusian', 'reserve')

                elif gp >= 20000:
                    price = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[8]'
                    ).click()
                    time.sleep(1)

                elif gp >= 19000:
                    price = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[5]'
                    ).click()
                    time.sleep(1)

                else:
                    price = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[2]'
                    ).click()
                    time.sleep(1)

                complete = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[3]/button/span'
                ).click()
                time.sleep(5)

                num += 1
                count -= 1

            print(f'[Andalusian] {name} предложил случек: {num}')

            return num

        except:

            print('error male_reproduction (andalusian)')

            return num
    else:
        try:
            while count != 0:
                with open(lists_reproductions[race][sex], 'r') as file:
                    females = file.readlines()

                if not females:
                    with open(second_lists_reproductions[race][sex], 'r') as file:
                        females = file.readlines()

                    if not females:
                        return num

                use_mating = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[3]/a'
                ).click()
                time.sleep(2)

                choice_reservation = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/ul/li[3]/input'
                ).click()
                time.sleep(2)

                send_name = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[2]/div[2]/input'
                ).send_keys(f'{females[0][:-1]}')
                time.sleep(1)

                watch = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[2]/div[2]/button/span/span/span'
                ).click()
                time.sleep(1)

                complete = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[3]/button/span/span/span'
                ).click()
                time.sleep(3)

                with open(lists_reproductions[race][sex], 'w') as file:
                    for female in females[1:]:
                        file.write(female)

                with open(second_lists_reproductions[race][sex], 'w') as file:
                    for female in females[1:]:
                        file.write(female)

                num += 1
                count -= 1

            print(f'[{race}] {name} предложил случек: {num}')

            return num

        except:
            return num
