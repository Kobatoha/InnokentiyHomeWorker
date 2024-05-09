from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys, ActionChains
import os
import random
from datetime import datetime
import time
from chrome_driver import newDRB


def find_unworking_horse():

    pages = len(driver.find_elements(
        By.XPATH,
        '/html/body/div[7]/main/section/section/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li'
    )[1:])

    print(f'Страниц во вкладке: {pages}')
    for i in range(2, pages + 2):
        page = driver.find_element(
            By.XPATH,
            f'/html/body/div[7]/main/section/section/div[1]/div[2]/div[2]/div/div[1]/div[2]/div/ul/li[{i}]/a'
        ).click()
        print(f'Page: {i - 1}')
        time.sleep(2)
        url = ''
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


def check_horse_complete():
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
        print('error in check_horse_complete')


def get_age_horse():
    age = driver.find_element(
        By.XPATH,
        '//*[@id="characteristics-body-content"]/table/tbody/tr[1]/td[2]'
    ).text.split()
    return age


def get_name_horse():
    name = driver.find_element(
        By.XPATH,
        '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
    ).text
    return name


def get_food():
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(2)
    recommend = int(driver.find_element(
        By.XPATH,
        '//*[@id="feeding"]/table[1]/tbody/tr[2]/td[1]/span[2]/strong'
    ).text)

    try:

        if 'недостаточный вес' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[21]').click()
            time.sleep()
        elif 'слишком толстая' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[2]').click()
            time.sleep(1)
        else:
            choice_food = driver.find_element(By.XPATH, f'//*[@id="haySlider"]/ol/li[{recommend + 1}]').click()
            time.sleep(1)

    except:

        choice_food = driver.find_element(By.XPATH, f'//*[@id="haySlider"]/ol/li[{recommend + 1}]').click()
        time.sleep(1)


def grow_up():
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


def next_horse():
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


def milk_horse(age, name, n):
    print(f'№{n} Молочный жеребенок: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonAllaiter"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(2)


def fourrage_horse(age, name, n):
    print(f'№{n} Жеребенок на фураже: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(2)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(2)
    choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[12]').click()
    time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(2)


def young_horse(age, name, n):
    print(f'№{n} Молодая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(1)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(2)
    choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[12]').click()
    time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
    time.sleep(1)

    try:
        training()
    except:
        pass


def get_stable():
    try:
        print('Лошадь нуждается в стойле, ищем подходящий КСК..')
        current_url = driver.find_element(
            By.XPATH,
            '//*[@id="module-2"]/div[1]/div/div[2]/h1/a'
        ).get_attribute('href')

        find_stable = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[1]'
            '/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
        ).click()
        time.sleep(1)

        check_ufo()

        two_mouth = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/table/thead/tr/td[6]/span[2]/span/span[9]/a'
        ).click()
        time.sleep(1)
        low_price_stable = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/table/tbody/tr[1]/td[10]/button/span/span/span/span'
        )
        if len(low_price_stable.text) == 1200:
            low_price_stable.click()
            alert = driver.switch_to.alert
            alert.accept()
            print(f'Стойло найдено за {low_price_stable.text}, продолжаем')
            time.sleep(2)

            return 1
        else:
            print(f'Стойло слишком дорогое, аж {low_price_stable.text}')

            return 0

    except:

        return 0


def death_horse():
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


def blup_diet():
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(2)
    choice_hay = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[15]').click()
    time.sleep(1)
    choice_oats = driver.find_element(By.XPATH, '//*[@id="oatsSlider"]/ol/li[13]').click()
    time.sleep(1)
    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(1)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(2)


def get_doping():
    '''

    :return: pat, water, carrot, mash, clean
    '''
    pat = driver.find_element(By.XPATH, '//*[@id="boutonCaresser"]')
    water = driver.find_element(By.XPATH, '//*[@id="boutonBoire"]')
    carrot = driver.find_element(By.XPATH, '//*[@id="boutonCarotte"]')
    mash = driver.find_element(By.XPATH, '//*[@id="boutonMash"]')
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]')

    return [pat, water, carrot, mash, clean]


def old_horse(age=['Возраст:', '2', 'года'], name='horse', n=1):
    print(f'№{n} Взрослая лошадь: {name}, начинаем уход.', *age)
    clean = driver.find_element(By.XPATH, '//*[@id="boutonPanser"]').click()
    time.sleep(2)
    food = driver.find_element(By.XPATH, '//*[@id="boutonNourrir"]').click()
    time.sleep(2)

    try:

        if 'недостаточный вес' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[21]').click()
            time.sleep(1)
        elif 'слишком толстая' in driver.find_element(By.XPATH, '//*[@id="messageBoxInline"]').text:
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[2]').click()
            time.sleep(1)
        else:
            choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[13]').click()
            time.sleep(1)

    except:

        choice_food = driver.find_element(By.XPATH, '//*[@id="haySlider"]/ol/li[13]').click()
        time.sleep(1)

    get_food = driver.find_element(By.XPATH, '//*[@id="feed-button"]').click()
    time.sleep(2)
    sleep = driver.find_element(By.XPATH, '//*[@id="boutonCoucher"]').click()
    time.sleep(1)
    lesson = driver.find_element(By.XPATH, '//*[@id="mission-tab-0"]/div/div/div[2]').click()
    time.sleep(1)


def female_horse(current_url):
    try:

        not_ready = driver.find_element(
            By.XPATH,
            '//*[@id="reproduction-body-content"]/div[1]/table/tbody/tr[1]/td'
        ).text
        print(not_ready)
        time.sleep(1)
        training()

        next_horse()

        return 0

    except:

        if driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Случить кобылу':

            print('Нужна случка, идем на брачный рынок..')
            check_ufo()
            driver.find_element(By.XPATH, '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]/a').click()
            time.sleep(1)
            master = driver.find_element(By.XPATH, '//*[@id="breeder"]').send_keys('Kolgotki')
            time.sleep(1)
            get_offers = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/form/button[1]/span/span'
            ).click()
            time.sleep(1)
            price_sort = driver.find_element(By.XPATH, '//*[@id="table-0"]/thead/tr/td[6]/a').click()
            time.sleep(1)
            get_mating = driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[8]/a').click()
            time.sleep(1)

            if 'Kolgotki' in driver.find_element(By.XPATH, '//*[@id="table-0"]/tbody/tr[1]/td[2]').text:
                mating = driver.find_element(By.XPATH, '//*[@id="boutonDoReproduction"]').click()
                time.sleep(1)

            print('Кобыла успешно провела случку')
            time.sleep(1)

            training()

            next_horse()

            return 1

        elif driver.find_element(
                By.XPATH,
                '//*[@id="reproduction-tab-0"]/table/tbody/tr/td[3]'
        ).text == 'Эхография':

            print('Кобыла уже жеребая')
            time.sleep(1)

            training()

            next_horse()

            return 0


def male_horse():
    mating = 25
    num = 0

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
                    lower_price = driver.find_element(
                        By.XPATH,
                        '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[5]'
                        '/div/div/div/div/div[1]/div[3]/table/tbody/tr[2]/td/form/div[1]/select/option[3]'
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

        print(f'Конь предложил случек: {num}')

        training()

        next_horse()

        return num

    except:

        print('error male_horse')

        return 0


def childbirth(current_url):
    age = 'Несколько часов'
    check_ufo()
    sex = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/img'
    ).get_attribute('alt')
    gen_potential = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[2]/tbody/tr[1]/td[2]/span').text
    print(f'Родился жеребенок! Пол: {sex}, ГП: {gen_potential}')

    if sex == 'male':

        get_name = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/input'
        ).send_keys(f'Пуля {gen_potential}')

    elif sex == 'femelle':
        get_name = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[2]/input'
        ).send_keys(f'Вишня {gen_potential}')

    profile = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody/tr/td[3]/div[1]'
    ).click()
    time.sleep(1)
    farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody'
        '/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]').click()
    time.sleep(2)
    get_farm = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/table[3]/tbody'
        '/tr/td[3]/div[2]/table/tbody/tr[2]/td[2]/select/option[2]'
    ).click()
    time.sleep(1)
    complete = driver.find_element(
        By.XPATH,
        '/html/body/div[7]/main/section/section/form/button'
    ).click()
    time.sleep(1)

    milk_horse(age, 'дитё', 0)
    time.sleep(1)

    return_to_mother = driver.get(current_url)

    return 1
