import time
import os
import pretty_errors
from selenium.webdriver.common.by import By
from lowadi.other import check_ufo, check_equus


class HorseCare:
    def __init__(self, driver):
        self.driver = driver


def get_farm(race: str, sex: str):

    farms = {
        'francais': {
            'blup': 'https://www.lowadi.com/elevage/chevaux/?elevage=1594529',
            'garden': 'https://www.lowadi.com/elevage/chevaux/?elevage=1599622',
            'north': 'https://www.lowadi.com/elevage/chevaux/?elevage=1596381',
        },
        'andalusian': {
            'basic': 'https://www.lowadi.com/elevage/chevaux/?elevage=1593197',
            'black': 'https://www.lowadi.com/elevage/chevaux/?elevage=1600331',
            'lava': 'https://www.lowadi.com/elevage/chevaux/?elevage=1600332',
            'creme': 'https://www.lowadi.com/elevage/chevaux/?elevage=1600333',
            'mouse': 'https://www.lowadi.com/elevage/chevaux/?elevage=1600375',
            'elite': 'https://www.lowadi.com/elevage/chevaux/?elevage=1586236',
            'blup': 'https://www.lowadi.com/elevage/chevaux/?elevage=1593203',
            'male': 'https://www.lowadi.com/elevage/chevaux/?elevage=1593198',
            'reserve': 'https://www.lowadi.com/elevage/chevaux/?elevage=1593208',
            'north': 'https://www.lowadi.com/elevage/chevaux/?elevage=1596383',
            'color': 'https://www.lowadi.com/elevage/chevaux/?elevage=1601761',
            'unicorn': 'https://www.lowadi.com/elevage/chevaux/?elevage=1593199'
        },
        'goland': {
            'blup': 'https://www.lowadi.com/elevage/chevaux/?elevage=1595755',
            'garden': 'https://www.lowadi.com/elevage/chevaux/?elevage=1599627',
            'north': 'https://www.lowadi.com/elevage/chevaux/?elevage=1596382',
        },
        'lusitanien': {
            'blup': 'https://www.lowadi.com/elevage/chevaux/?elevage=1599295'
        },
        'marshadore': {
            'female': 'https://www.lowadi.com/elevage/chevaux/?elevage=1590179',
            'male': 'https://www.lowadi.com/elevage/chevaux/?elevage=1594304'
        },
        'heavyhorse': {
            'all': 'https://www.lowadi.com/elevage/chevaux/?elevage=1593200'
        }
    }

    return farms[race][sex]


def find_unworking_horse(driver, race='andalusian', sex='basic'):

    farm = get_farm(race, sex)

    driver.get(farm)
    time.sleep(3)

    pages = len(driver.find_elements(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li'
    )[1:])
    if pages == 0:
        pages += 1
    url = ''
    print(f'Страниц во вкладке: {pages}')

    all_horses = pages * 200
    sleep_horses = 0

    if pages == 1:
        horses = driver.find_elements(By.XPATH, '//*[@class="damier-cell grid-cell width-25"]')
        all_horses = len(horses)
        for j in range(len(horses)):
            try:
                name = horses[j].find_element(By.CLASS_NAME, 'horsename').text
                status = horses[j].find_elements(By.XPATH, '//*[@class="cheval-status spacer-small-left"]/span[1]')[
                    j].get_attribute('data-tooltip')

                if status != 'Спит':
                    print('Найдена необработанная лошадь')
                    url = horses[j].find_element(By.CLASS_NAME, 'horsename').get_attribute('href')

                    return url, all_horses - sleep_horses
                sleep_horses += 1

            except:
                pass

    else:
        for i in range(2, pages + 2):

            page = driver.find_element(
                By.XPATH,
                f'/html/body/div[7]/main/section/section/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[{i}]/a'
            ).click()
            print(f'Page: {i - 1}')
            time.sleep(2)

            horses = driver.find_elements(By.XPATH, '//*[@class="damier-cell grid-cell width-25"]')

            for j in range(len(horses)):
                sleep_horses += 1
                try:
                    name = horses[j].find_element(By.CLASS_NAME, 'horsename').text
                    status = horses[j].find_elements(By.XPATH, '//*[@class="cheval-status spacer-small-left"]/span[1]')[
                        j].get_attribute('data-tooltip')

                    if status != 'Спит':
                        print('Найдена необработанная лошадь')
                        url = horses[j].find_element(By.CLASS_NAME, 'horsename').get_attribute('href')
                        return url, all_horses - sleep_horses

                except:
                    pass

    return url, all_horses - sleep_horses


def check_horse_complete(driver):
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
        print('error in check_horse_complete:', error)


def check_young_horse_complete(driver):
    try:
        history = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[1]/div[5]/div/div/div/div[1]/div/div/div/ul'
        ).text.split('\n')
        count = 0
        for i in history:
            if 'Полный уход' in i:
                count += 1
            elif 'съел(а)' in i or 'молоко матери' in i:
                count += 1
            elif 'уложен(а) спать' in i:
                count += 1
        if count == 3:
            return True
        return False
    except Exception as error:
        print('error in check_young_horse_complete:', error)


def get_current_url(driver):
    current_url = driver.find_element(
                By.XPATH,
                '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
            ).get_attribute('href')
    return current_url


def get_location_complex(driver):
    try:
        location = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[1]/div[3]'
            '/div/div/div/div/div/div[1]/div[1]/table/tbody/tr[1]/td/div[2]/div/div[2]/a'
        ).get_attribute('class')
    except:
        location = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[1]/div[3]'
            '/div/div/div/div/div/div[1]/div[1]/table/tbody/tr[1]/td/div[2]/div/div[2]/a'
        ).get_attribute('class')
    return location


def get_age_horse(driver):
    age = driver.find_element(
        By.XPATH,
        '//*[@id="characteristics-body-content"]/table/tbody/tr[1]/td[2]'
    ).text.split()
    return age


def get_color(driver):
    color = driver.find_element(
        By.XPATH,
        '//*[@id="characteristics-body-content"]/table/tbody/tr[4]/td[1]'
    ).text.split(':')[-1].lstrip()

    return color


def get_name_horse(driver):
    name = driver.find_element(
        By.XPATH,
        '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
    ).text
    return name


def get_energy(driver):
    try:
        try:
            energie = int(driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]'
                '/div[2]/div/div/div/div[2]/div/div[1]/div[3]/strong/span'
            ).text)
        except:
            energie = int(driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/div[5]/div/div[2]/div[2]'
                '/div[2]/div/div/div/div[2]/div/div[1]/div[3]/strong/span'
            ).text)
    except:
        energie = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]'
            '/div[2]/div/div/div/div[2]/div/div[1]/div[3]/strong/span'
        ).text)
    return energie


def get_moral(driver):
    try:
        try:
            moral = int(driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[4]/div/div[2]/div[2]'
                '/div[2]/div/div/div/div[2]/div/div[3]/div[3]/strong/span'
            ).text)
        except:
            moral = int(driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/div[5]/div/div[2]/div[2]'
                '/div[2]/div/div/div/div[2]/div/div[3]/div[3]/strong/span'
            ).text)
    except:
        moral = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]'
            '/div[2]/div/div/div/div[2]/div/div[3]/div[3]/strong/span'
        ).text)
    return moral


def get_sex(driver):
    sex = driver.find_element(
        By.XPATH,
        '//*[@id="characteristics-body-content"]/table/tbody/tr[3]/td[1]').text
    return sex


def get_food(driver):
    try:
        food = driver.find_element(By.XPATH, '//*[@id="boutonAllaiter"]').click()
        time.sleep(2)
    except:
        food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
        time.sleep(2)
        recommend = int(driver.find_element(
            By.XPATH,
            '//*[@id="feeding"]/table[1]/tbody/tr[2]/td[1]/span[2]/strong'
        ).text)

        try:

            if 'недостаточный вес' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
                choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[21]').click()
                time.sleep(1)
            elif 'слишком толстая' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
                choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[2]').click()
                time.sleep(1)
            elif 'слишком толстый' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
                choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[2]').click()
                time.sleep(1)
            else:
                choice_food = driver.find_element(By.XPATH, f'//*[@id="haySlider"]/ol/li[{recommend + 1}]').click()
                time.sleep(1)

        except:

            choice_food = driver.find_element(By.XPATH, f'//*[@id="haySlider"]/ol/li[{recommend + 1}]').click()
            time.sleep(1)
        feed = driver.find_element(
            By.XPATH,
            '//*[@id="feed-button"]/span/span/span'
            ).click()

    time.sleep(1)


def grow_up(driver):
    grow_up = driver.find_element(
        By.XPATH,
        '//*[@id="boutonVieillir"]'
    ).click()
    time.sleep(1)
    try:
        try:
            agree = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[1]/div[2]/div/div/div[2]'
                '/div/div/div[2]/table/tbody/tr[2]/td/form/div/button/span/span/span'
            ).click()
        except:
            agree = driver.find_element(
                By.XPATH,
                '/html/body/div[9]/main/section/section/div[5]/div/div[1]/div[2]/div/div/div[2]'
                '/div/div[1]/div[2]/table/tbody/tr[2]/td/form/div/button/span/span/span'
            ).click()
    except:
        agree = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[1]/div[2]/div/div/div[2]'
            '/div/div/div[2]/table/tbody/tr[2]/td/form/div/button/span/span/span'
        ).click()

    time.sleep(2)


def next_horse(driver):
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


def milk_horse(driver, age, name, n):
    try:
        print(f'№{n} Молочный жеребенок: {name}, начинаем уход.', *age)
        clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
        time.sleep(1)
        food = driver.find_element(By.XPATH, '//*[@id="boutonAllaiter"]').click()
        time.sleep(1)
        sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
        time.sleep(2)
    except:
        pass


def fourrage_horse(driver, age, name, n):
    print(f'№{n} Жеребенок на фураже: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(2)
    get_food(driver)
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(2)


def young_horse(driver, age, name, n):
    print(f'№{n} Молодая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    get_food(driver)
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
    time.sleep(2)


def get_stable(driver):
    try:
        if 'Зарегистрируйте свою лошадь' in driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[1]'
                '/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
        ).text:

            print('Лошадь нуждается в стойле..')

            current_url = get_current_url(driver)

            time.sleep(2)
            find_stable = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[1]'
                '/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
            ).click()
            time.sleep(3)

            check_ufo(driver)

            reserv = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/ul/li[2]/div/a'
            ).click()
            time.sleep(2)

            one_month = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[2]/table/tbody/tr[1]/td[9]/button/span/span/span'
            ).click()
            time.sleep(3)

            return 1

    except:

        return 0


def about_stable(driver):
    try:
        name_stable = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[1]/div[3]'
            '/div/div/div/div/div/div[1]/div[1]/table/tbody/tr[1]/td/div[2]/div/div[2]'
        ).text
    except:
        name_stable = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[1]/div[3]'
            '/div/div/div/div/div/div[1]/div[1]/table/tbody/tr[1]/td/div[2]/div/div[2]'
        ).text
    return name_stable


def death_horse(driver):
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


def blup_diet(driver):
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(2)
    choice_hay = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[15]').click()
    time.sleep(1)
    choice_oats = driver.find_element(By.XPATH, '//*[@id="oatsSlider"]/ol/li[13]').click()
    time.sleep(1)
    click_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(2)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(2)


def get_doping(driver):
    '''
    :return: pat, water, carrot, mash, clean
    '''
    pat = driver.find_element(By.XPATH, '//*[@id="boutonCaresser"]')
    water = driver.find_element(By.XPATH, '//*[@id="boutonBoire"]')
    carrot = driver.find_element(By.XPATH, '//*[@id="boutonCarotte"]')
    try:
        mash = driver.find_element(By.XPATH, '//*[@id="boutonMash"]')
    except:
        mash = None
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]')

    return [pat, water, carrot, mash, clean]


def get_sleep(driver):
    driver.find_element(
        By.XPATH,
        '//*[@id="boutonCoucher"]'
    ).click()
    time.sleep(2)


def old_horse(driver, age=None, name='horse', n=1):
    if age is None:
        age = ['Возраст:', '2', 'года']
    print(f'№{n} Взрослая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    get_food(driver)
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)


def get_lesson(driver):
    try:
        lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
        time.sleep(1)
    except:
        pass


def get_history(driver, event='lesson'):
    events = {
        'lesson': 'урок верховой езды',
        'mission': 'выполнила миссию',
        'clean': 'Полный уход',
        'food': 'съел(а)',
        'sleep': 'уложен(а) спать',
        'OR': 'нашли 1 очко роста'
    }
    history = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[5]/div/div[1]/div[5]/div/div/div/div[1]/div/div/div/ul'
    ).text.split('\n')
    for message in history:
        if events[event] in message:
            return message
        else:
            return ''


def get_servant_farm(driver):
    driver.get('https://www.lowadi.com/elevage/chevaux/?elevage=1582713')
    time.sleep(1)
    driver.find_element(
        By.XPATH,
        '//*[@id="linkBlocRecherche"]'
    ).click()
    time.sleep(1)
    clear_age = driver.find_element(
        By.XPATH,
        '//*[@id="horseSearchAge"]'
    ).clear()
    time.sleep(1)
    send_age = driver.find_element(
        By.XPATH,
        '//*[@id="horseSearchAge"]'
    ).send_keys('28')
    time.sleep(1)
    choice_month = driver.find_element(
        By.XPATH,
        '//*[@id="horseSearchUniteAge"]'
    ).click()
    time.sleep(0.5)
    send_month = driver.find_element(
        By.XPATH,
        '//*[@id="horseSearchUniteAge"]/option[2]'
    ).click()
    time.sleep(1)
    more_options = driver.find_element(
        By.XPATH,
        '//*[@id="horseSearchLink-criteres"]'
    ).click()
    time.sleep(1)
    send_sex = driver.find_element(
        By.XPATH,
        '//*[@id="horseSearchSexe"]'
    ).click()
    time.sleep(0.5)
    choice_sex = driver.find_element(
        By.XPATH,
        '//*[@id="horseSearchSexe"]/option[2]'
    ).click()
    time.sleep(1)
    for _ in range(2):
        not_in_sale = driver.find_element(
            By.XPATH,
            '//*[@id="horseSearchVenteCheckbox"]'
        ).click()
        time.sleep(0.2)
    submit = driver.find_element(
        By.XPATH,
        '//*[@id="horseSearchSubmit"]/span/span'
    ).click()
    time.sleep(1)
    more_options = driver.find_element(
        By.XPATH,
        '//*[@id="horseSearchLink-criteres"]'
    ).click()
    time.sleep(1)
    horses = driver.find_elements(By.XPATH, '//*[@class="damier-cell grid-cell width-25"]')

    print(f'Найдено {len(horses)} половозрелых мужчин')
    urls = []
    for j in range(len(horses)):
        try:
            name = horses[j].find_element(By.CLASS_NAME, 'horsename').text
            status = horses[j].find_elements(By.XPATH, '//*[@class="cheval-status spacer-small-left"]/span[1]')[
                j].get_attribute('data-tooltip')

            url = horses[j].find_element(By.CLASS_NAME, 'horsename').get_attribute('href')
            urls.append(url)
        except:
            pass

    return urls


def stable_options(driver):
    options = {'water': False, 'wash': False, 'carrot': False, 'mash': False}
    for i in range(1, 5):
        try:
            option = driver.find_element(
                By.XPATH,
                f'//*[@id="center-tab-main"]/div[1]/table/tbody/tr[3]/td/div/div/div[2]/span[{i}]'
            ).get_attribute('data-tooltip')
            if option == 'Автопоилка доступна':
                options['water'] = True
            elif option == 'Наличие душевых':
                options['wash'] = True
        except:
            pass
    for i in range(1, 5):
        try:
            profit = driver.find_element(
                By.XPATH,
                f'//*[@id="center-tab-main"]/div[1]/table/tbody/tr[4]/td/div/div/div[2]/span[{i}]'
            ).get_attribute('data-tooltip')
            if 'морковь' in profit:
                options['carrot'] = True
            elif 'комбикорма' in profit:
                options['mash'] = True
        except:
            pass
    return options


def get_name_race(driver):
    try:
        name_race = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[4]/div/div/div/div/table[1]'
            '/tbody[1]/tr/td/div/table/tbody/tr[1]/td[1]/span/a'
        ).text
    except:
        name_race = driver.find_element(
            By.XPATH,
            '/html/body/div[8]/main/section/section/div[5]/div/div[2]/div[4]/div/div/div/div/table[1]'
            '/tbody[1]/tr/td/div/table/tbody/tr[1]/td[1]/span/a'
        ).text
    return name_race


def childbirth_without_stable(driver):
    try:
        button = driver.find_element(
            By.XPATH,
            '/html/body/div[11]/div/div/table/tbody/tr/td[2]/button/span/span/span'
        )
        if 'Зарегистрировать мою кобылу в КСК' == button.text:
            button.click()
            time.sleep(2)

            check_ufo(driver)

            reserv = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/ul/li[2]/div/a'
            ).click()
            time.sleep(2)

            one_month = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[2]/table/tbody/tr[1]/td[9]/button/span/span/span'
            ).click()
            time.sleep(3)

    except:
        pass


def childbirth_farms(driver, place=''):
    all_farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]'
        f'/div[2]/table/tbody/tr[2]/td[2]/select'
    )
    farms = all_farm.find_elements(By.TAG_NAME, 'option')
    for farm in farms:
        if place in farm.text:
            return farm


def childbirth(driver, current_url, race='andalusian', sex='basic'):
    age = ['Возраст:', 'несколько', 'часов']
    check_ufo(driver)

    races = {
        'andalusian': {
            'basic': ['Подземелье', 'Ежевика', 'Лимон'],
            'unicorn': ['9-й этаж [ᴜɴɪᴄᴏʀɴ]', 'Морожка', 'Ворожка'],
            'without_corn': ['Безрожье', 'Безрожка', 'Безрожик'],
            'black': ['Подземелье', 'Смородина', 'Розмарин'],
            'lava': ['Подземелье', 'Шоколадка', 'Кофе'],
            'creme': ['Подземелье', 'Пломбир', 'Крем'],
            'mouse': ['Подземелье', 'Мауси', 'Мышъ'],
            'elite': ['Подземелье', 'Чили', 'Шафран'],
            'blup': ['⧉ ᴛʀᴀɪɴɪɴɢ', 'жгг', 'мгг'],
        },
        'heavyhorse': {
            'all': ['Серп и Молот', 'Пончик', 'Эклер']
        },
        'marshadore': {
            'female': ['Катакомбы', 'Марша', 'Маршель']
        },
        'francais': {
            'blup': ['ᴅɪᴏɴ ᴠɪʟʟᴀɢᴇ ɢᴀʀᴅᴇɴ', 'Франочка', 'Франчик'],
            'garden': ['ᴅɪᴏɴ ᴠɪʟʟᴀɢᴇ ɢᴀʀᴅᴇɴ', 'Франочка', 'Франчик'],
        },
        'goland': {
            'blup': ['ɢɪʀᴀɴ ᴠɪʟʟᴀɢᴇ ɢᴀʀᴅᴇɴ', 'Голдишка', 'Голдунец'],
            'garden': ['ɢɪʀᴀɴ ᴠɪʟʟᴀɢᴇ ɢᴀʀᴅᴇɴ', 'Голдишка', 'Голдунец'],
        },
        'lusitanien': {
            'blup': ['ᴀᴅᴇɴ ᴠɪʟʟᴀɢᴇ', 'Лулзишка', 'Лулзинец'],
        }
    }

    if sex == 'unicorn':
        style = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/figure'
        ).get_attribute('style')
        if 'horn' not in style:
            sex = 'without_corn'

    sex_newhorse = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/img'
    ).get_attribute('alt')

    gen_potential = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[2]/tbody/tr[1]/td[2]/span').text
    print(f'Родился жеребенок! Пол: {sex_newhorse}, ГП: {gen_potential}')

    new_name = ''

    if sex_newhorse == 'male':

        new_name = f'{races[race][sex][2]} {gen_potential}'

        get_name = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/input'
        ).send_keys(new_name)

    elif sex_newhorse == 'femelle':

        new_name = f'{races[race][sex][1]} {gen_potential}'

        get_name = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/input'
        ).send_keys(new_name)
    time.sleep(2)

    profile = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[1]/a'
    ).click()
    time.sleep(1)

    choice_farm = childbirth_farms(driver, races[race][sex][0])
    choice_farm.click()
    time.sleep(1)

    complete = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/button'
    ).click()
    time.sleep(1)

    milk_horse(driver, age, new_name, 0)
    time.sleep(1)

    return_to_mother = driver.get(current_url)
    time.sleep(2)

    return 1


def energy_of_items(driver):
    options = stable_options(driver)
    water, carrot, mash = 2, 0, 0
    matting = 25
    if options['water']:
        water = 8
    if options['carrot']:
        carrot = 8
    if options['mash']:
        mash = 10
    if options['wash']:
        matting = 22.5

    return water, carrot, mash, matting


def sell_horse(driver):
    options = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/div/div[1]/button/span'
    ).click()
    time.sleep(1)
    option_sale = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[1]/div/div[3]/div/div[2]/ul/li[2]/a'
    ).click()
    time.sleep(1)
    direct_sale = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div/div/form/div[1]/div/div/div/div/div/p[3]/label/input'
    ).click()
    time.sleep(1)
    equus_sale = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div/div/form/div[4]/div[2]/div/div/div/div/div/p[1]/label/input'
    ).click()
    amount = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div/div/form/div[4]/div[4]/div/div/div/div/div/div/p[1]/input'
    )
    time.sleep(1)
    amount.clear()
    time.sleep(1)
    amount.send_keys('1999')
    time.sleep(1)
    agree_sale = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div/div/form/div[4]/button/span/span/span'
    ).click()
    time.sleep(2)


def push_mating_for_name(driver, female_name=''):
    if female_name:
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
        ).send_keys(f'{female_name}')
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
    else:
        print('No name horse')


def andalusian_male_color_mating(driver):
    color = get_color(driver)
    sex = 'male'
    if color == 'Рыжая с лавовой гривой':
        sex = 'red'
    elif color == 'Огненно-рыжая с лавовой гривой':
        sex = 'fire_red'
    elif color == 'Кремелло':
        sex = 'cremello'
    elif color == 'Соловая (Паломино)':
        sex = 'palomino'
    return sex


def child_age(age=''):
    ages = [
        ['Возраст:', '6', 'мес.'],
        ['Возраст:', '8', 'мес.'],
        ['Возраст:', '10', 'мес.'],
        ['Возраст:', '1', 'год'],
        ['Возраст:', '1', 'год', '2', 'мес.'],
        ['Возраст:', '1', 'год', '4', 'мес.'],
        ['Возраст:', '1', 'год', '6', 'мес.'],
        ['Возраст:', '1', 'год', '8', 'мес.'],
        ['Возраст:', '1', 'год', '10', 'мес.'],
        ['Возраст:', '2', 'года'],
        ['Возраст:', '2', 'года', '2', 'мес.'],
        ['Возраст:', '2', 'года', '4', 'мес.'],
        ['Возраст:', '2', 'года', '6', 'мес.'],
        ['Возраст:', '2', 'года', '8', 'мес.'],
        ['Возраст:', '2', 'года', '10', 'мес.'],
    ]
    return age in ages
