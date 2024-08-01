import time
import os
import pretty_errors
from selenium.webdriver.common.by import By
from lowadi.other import check_ufo, check_equus


def get_farm(race: str, sex: str):
    farm = ''
    if race == 'andalusian':
        if sex == 'female':
            farm = 'https://www.lowadi.com/elevage/chevaux/?elevage=1593197'
        elif sex == 'male':
            farm = 'https://www.lowadi.com/elevage/chevaux/?elevage=1593198'
        elif sex == 'unicorn':
            farm = 'https://www.lowadi.com/elevage/chevaux/?elevage=1593199'

    if race == 'andalusian_elite':
        if sex == 'female':
            farm = 'https://www.lowadi.com/elevage/chevaux/?elevage=1586236'
        elif sex == 'male':
            farm = 'https://www.lowadi.com/elevage/chevaux/?elevage=1593208'

    elif race == 'heavy_horse':
        farm = 'https://www.lowadi.com/elevage/chevaux/?elevage=1593200'

    elif race == 'marshadore':
        if sex == 'female':
            farm = 'https://www.lowadi.com/elevage/chevaux/?elevage=1590179'
        if sex == 'male':
            farm = 'https://www.lowadi.com/elevage/chevaux/?elevage=1594304'

    return farm


def find_unworking_horse(driver, race='andalusian', sex='female'):

    farm = get_farm(race, sex)

    driver.get(farm)
    time.sleep(5)

    pages = len(driver.find_elements(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li'
    )[1:])
    url = ''
    print(f'Страниц во вкладке: {pages}')

    if pages == 0:
        horses = driver.find_elements(By.XPATH, '//*[@class="damier-cell grid-cell width-25"]')

        for j in range(len(horses)):
            try:
                name = horses[j].find_element(By.CLASS_NAME, 'horsename').text
                status = horses[j].find_elements(By.XPATH, '//*[@class="cheval-status spacer-small-left"]/span[1]')[
                    j].get_attribute('data-tooltip')

                if status != 'Спит':
                    print('Найдена необработанная лошадь')
                    url = horses[j].find_element(By.CLASS_NAME, 'horsename').get_attribute('href')
                    return url
            except:
                pass

    for i in range(2, pages + 2):

        page = driver.find_element(
            By.XPATH,
            f'/html/body/div[7]/main/section/section/div[2]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[{i}]/a'
        ).click()
        print(f'Page: {i - 1}')
        time.sleep(2)

        horses = driver.find_elements(By.XPATH, '//*[@class="damier-cell grid-cell width-25"]')

        for j in range(len(horses)):
            try:
                name = horses[j].find_element(By.CLASS_NAME, 'horsename').text
                status = horses[j].find_elements(By.XPATH, '//*[@class="cheval-status spacer-small-left"]/span[1]')[
                    j].get_attribute('data-tooltip')

                if status != 'Спит':
                    print('Найдена необработанная лошадь')
                    url = horses[j].find_element(By.CLASS_NAME, 'horsename').get_attribute('href')
                    return url
            except:
                pass


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
    time.sleep(2)


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
    mash = driver.find_element(By.XPATH, '//*[@id="boutonMash"]')
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]')

    return [pat, water, carrot, mash, clean]


def get_sleep(driver):
    driver.find_element(
        By.XPATH,
        '//*[@id="boutonCoucher"]'
    ).click()
    time.sleep(2)


def old_horse(driver, age=['Возраст:', '2', 'года'], name='horse', n=1):
    print(f'№{n} Взрослая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(2)
    get_food(driver)
    time.sleep(2)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
    time.sleep(2)


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


def female_andalusian(driver, current_url):

    matting = ready_matt(driver)

    if matting and matting[1] == 0:

        print('Нужна случка, идем на брачный рынок..')
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

        print('Кобыла успешно провела случку')
        time.sleep(1)

        return 1

    else:

        return 0


def male_andalusian(driver):
    time.sleep(1)
    mating = 25
    num = 0
    name = get_name_horse(driver)
    gp = int(name.split()[1][:-3])

    try:

        for i in range(5):
            energie = int(driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[2]/div[2]'
                '/div/div/div/div[2]/div/div[1]/div[3]/strong/span'
            ).text)
            if energie - mating >= 20:
                create_mating = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                    '/div/div/div/div/div[1]/div[1]/table/tbody/tr/td[3]/a'
                )
                try:
                    create_mating.click()
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
                    if gp >= 11555:
                        lower_price = driver.find_element(
                            By.XPATH,
                            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                            '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[13]'
                        ).click()
                        time.sleep(1)
                    else:
                        lower_price = driver.find_element(
                            By.XPATH,
                            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                            '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[9]'
                        ).click()
                        time.sleep(1)
                    complete = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[3]/button/span'
                    ).click()
                    time.sleep(5)

                    num += 1

                except:
                    return num

        print(f'{name} предложил случек: {num}')

        return num

    except:

        print('error male_horse')

        return 0


def female_andalusian_elite_mating(driver, current_url):
    matting = ready_matt(driver)

    if matting and matting[1] == 1:

        male_name = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
        ).text
        print(f'Принимаем случку от {male_name}')

        ok = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
            '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
        ).click()

        check_ufo(driver)

        mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
        time.sleep(1)

        print('Кобыла успешно провела случку')
        time.sleep(1)

        return 1

    elif matting and matting[1] == 0:

        name = get_name_horse(driver)

        with open('lowadi/andalusian.txt', 'r') as file:
            names = file.readlines()

        if name + '\n' not in names:
            with open('lowadi/andalusian.txt', 'a') as file:
                file.write(name + '\n')

            print('Добавлена в очередь на ожидание случки')
        else:
            print('Уже в очереди на ожидание случки')

        return 0

    else:

        return 0


def male_andalusian_elite_mating(driver):

    mating = 25
    num = 0
    name = get_name_horse(driver)
    energy = get_energy(driver)

    count = energy // mating

    try:
        while count != 0:
            with open('lowadi/andalusian.txt', 'r') as file:
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

            with open('lowadi/andalusian.txt', 'w') as file:
                for female in females[1:]:
                    file.write(female)

            num += 1
            count -= 1

        print(f'{name} предложил случек: {num}')

        return num

    except:

        print('error male_andalusian_elite_mating')

        return num


def female_marshadore(driver, current_url):
    matting = ready_matt(driver)

    if matting and matting[1] == 1:

        male_name = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
        ).text
        print(f'Принимаем случку от {male_name}')

        ok = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
            '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
        ).click()

        check_ufo(driver)

        mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
        time.sleep(1)

        print('Кобыла успешно провела случку')
        time.sleep(1)

        return 1

    elif matting and matting[1] == 0:

        name = get_name_horse(driver)

        with open('lowadi/marshadore.txt', 'r') as file:
            names = file.readlines()

        if name + '\n' not in names:
            with open('lowadi/marshadore.txt', 'a') as file:
                file.write(name + '\n')

            print('Добавлена в очередь на ожидание случки')
        else:
            print('Уже в очереди на ожидание случки')

        return 0

    else:

        return 0


def male_marshadore(driver):

    mating = 25
    num = 0
    name = get_name_horse(driver)
    energy = get_energy(driver)

    count = energy // mating

    try:
        while count != 0:
            with open('lowadi/marshadore.txt', 'r') as file:
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

            with open('lowadi/marshadore.txt', 'w') as file:
                for female in females[1:]:
                    file.write(female)

            num += 1
            count -= 1

        print(f'{name} предложил случек: {num}')

        return num

    except:

        print('error male_marshadore')

        return num


def female_andalusian_unicorn_mating(driver, current_url):
    matting = ready_matt(driver)

    if matting and matting[1] == 1:

        male_name = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-bottom"]/table/tbody/tr/td[2]/a'
        ).text
        print(f'Принимаем случку от {male_name}')

        ok = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
            '/div/div/div/div/div[2]/table/tbody/tr/td[4]/div/div/a/span/span/span'
        ).click()

        check_ufo(driver)

        mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
        time.sleep(1)

        print('Кобыла успешно провела случку')
        time.sleep(1)

        return 1

    elif matting and matting[1] == 0:

        name = get_name_horse(driver)

        with open('lowadi/andalusian_unicorn.txt', 'r') as file:
            names = file.readlines()

        if name + '\n' not in names:
            with open('lowadi/andalusian_unicorn.txt', 'a') as file:
                file.write(name + '\n')

            print('Добавлена в очередь на ожидание случки')
        else:
            print('Уже в очереди на ожидание случки')

        return 0

    else:

        return 0


def male_andalusian_unicorn_mating(driver):

    mating = 25
    num = 0
    name = get_name_horse(driver)
    energy = get_energy(driver)

    count = energy // mating

    try:
        while count != 0:
            with open('lowadi/andalusian_unicorn.txt', 'r') as file:
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

            with open('lowadi/andalusian_unicorn.txt', 'w') as file:
                for female in females[1:]:
                    file.write(female)

            num += 1
            count -= 1

        print(f'{name} предложил случек: {num}')

        return num

    except:

        print('error male_andalusian_unicorn_mating')

        return num


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


def check_open_mating(driver):
    checked = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/ul/li[1]/label'
    ).get_attribute('data-tooltip')
    return checked


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


def childbirth(driver, current_url, race):
    '''
    0 == ...
    1 == Цитадель
    :param driver:
    :param current_url:
    :param race:
    :return:
    '''
    age = ['Возраст:', 'несколько', 'часов']
    check_ufo(driver)

    races = {
        'andalusian': [20, 'Гранат', 'Лайм'],
        'andalusian_elite': [12, 'Явь', 'Морок'],
        'unicorn': [18, 'Морожка', 'Ворожка'],
        'heavy_horse': [8, 'Пончик', 'Эклер'],
        'marshadore': [3, 'Марша', 'Маршель']
    }

    if race == 'unicorn':
        style = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/figure'
        ).get_attribute('style')
        if 'horn' not in style:
            race = 'andalusian'

    sex = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/img'
    ).get_attribute('alt')

    gen_potential = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[2]/tbody/tr[1]/td[2]/span').text
    print(f'Родился жеребенок! Пол: {sex}, ГП: {gen_potential}')

    new_name = ''

    if sex == 'male':

        new_name = f'{races[race][2]} {gen_potential}'

        get_name = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/input'
        ).send_keys(new_name)

        if race == 'marshadore':
            races[race][0] = 4
        elif race == 'andalusian_elite':
            races[race][0] = 13

    elif sex == 'femelle':

        new_name = f'{races[race][1]} {gen_potential}'

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

    choice_farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]'
        f'/div[2]/table/tbody/tr[2]/td[2]/select/option[{races[race][0]}]'
    ).click()
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


