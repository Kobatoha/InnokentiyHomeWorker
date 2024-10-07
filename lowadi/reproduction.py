import time
import os
import pretty_errors
from selenium.webdriver.common.by import By
from lowadi.other import check_ufo
from lowadi.care import get_name_horse, get_energy, push_mating_for_name, stable_options


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


def female_reproduction(driver, race='andalusian', male_url=None):
    matting = ready_matt(driver)

    if matting and matting[1] == 1:

        if race == 'andalusian_elite':
            male_name = driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
            ).text
            print(f'[Andalusian Elite] Принимаем случку от {male_name}')

            ok = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
            ).click()

            check_ufo(driver)

            mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
            time.sleep(1)

            print('[Andalusian Elite] Кобыла успешно приняла предложенную случку')
            time.sleep(1)

            return 1

        elif race == 'andalusian_blup':
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

        elif race == 'marshadore':
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

        elif race == 'andalusian_unicorn':
            male_name = driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
            ).text
            print(f'[Andalusian Unicorn] Принимаем случку от {male_name}')

            ok = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
            ).click()

            check_ufo(driver)

            mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
            time.sleep(1)

            print('[Andalusian Unicorn] Кобыла успешно приняла предложенную случку')
            time.sleep(1)

            return 1

    elif matting and matting[1] == 0:

        if race == 'andalusian':
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

            print('[Andalusian] Кобыла успешно провела случку')
            time.sleep(1)

            return 1

        elif race == 'andalusian_elite':
            name = get_name_horse(driver)

            with open('lowadi/Lists of horses/andalusian.txt', 'r') as file:
                names = file.readlines()

            if name + '\n' not in names:
                with open('lowadi/Lists of horses/andalusian.txt', 'a') as file:
                    file.write(name + '\n')

                print('[Andalusian Elite] Добавлена в очередь на ожидание случки')
            else:
                print('[Andalusian Elite] Уже в очереди на ожидание случки')

            return 0

        elif race == 'andalusian_blup':
            if male_url:
                name = get_name_horse(driver)
                driver.get(male_url)
                push_mating_for_name(driver, name)
                driver.back()

                print('[Andalusian Blup] Случка прокинута на кобылу')
            else:
                print('[Andalusian Blup] Нет ссылки на коня')

            return 0

        elif race == 'francais_blup':
            if male_url:
                name = get_name_horse(driver)
                driver.get(male_url)
                push_mating_for_name(driver, name)
                driver.back()

                print('[Andalusian Blup] Случка прокинута на кобылу')
            else:
                input('[Andalusian Blup] Нет ссылки на коня, давайте сами')

        elif race == 'marshadore':
            name = get_name_horse(driver)

            with open('lowadi/Lists of horses/marshadore.txt', 'r') as file:
                names = file.readlines()

            if name + '\n' not in names:
                with open('lowadi/Lists of horses/marshadore.txt', 'a') as file:
                    file.write(name + '\n')

                print('[Marshadore] Добавлена в очередь на ожидание случки')
            else:
                print('[Marshadore] Уже в очереди на ожидание случки')

            return 0

        elif race == 'andalusian_unicorn':
            name = get_name_horse(driver)

            with open('lowadi/Lists of horses/andalusian_unicorn.txt', 'r') as file:
                names = file.readlines()

            if name + '\n' not in names:
                with open('lowadi/Lists of horses/andalusian_unicorn.txt', 'a') as file:
                    file.write(name + '\n')

                print('[Andalusian Unicorn] Добавлена в очередь на ожидание случки')
            else:
                print('[Andalusian Unicorn] Уже в очереди на ожидание случки')

            return 0
    else:
        return 0


def male_reproduction(driver, race='andalusian'):
    lists_reproductions = {
        'andalusian_elite': 'lowadi/Lists of horses/andalusian.txt',
        'marshadore': 'lowadi/Lists of horses/marshadore.txt',
        'andalusian_unicorn': 'lowadi/Lists of horses/andalusian_unicorn.txt'
    }
    time.sleep(1)
    mating = 25
    num = 0
    name = get_name_horse(driver)
    gp = int(name.split()[1][:-3])
    energy = get_energy(driver)
    count = energy // mating
    if race == 'andalusian':
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

                if gp >= 17000:
                    price = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[11]'
                    ).click()
                    time.sleep(1)

                else:
                    price = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[5]'
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
                with open(lists_reproductions[race], 'r') as file:
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

                with open(lists_reproductions[race], 'w') as file:
                    for female in females[1:]:
                        file.write(female)

                num += 1
                count -= 1

            print(f'[{race}] {name} предложил случек: {num}')

            return num

        except:

            print('error male_reproduction')

            return num



