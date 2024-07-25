import time
import pretty_errors
from datetime import datetime
from selenium.webdriver.common.by import By


def check_ufo(driver):

    good_ufo = {'vieillissement': 'очки роста'}
    bad_ufo = {'pomme': 'яблоко', 'carotte': 'морковь', 'classique': 'седло', 'mash': 'комбикорм',
               'equus': 'экю'}
    try:

        if driver.find_element(By.XPATH, '//*[@id="Ufo_0"]'):
            icon = driver.find_element(By.XPATH, '/html/body/div[1]/img').get_attribute('src')

            for bad_key in bad_ufo:
                if bad_key in icon:
                    print(f"НЛО: {bad_ufo[bad_key]}, надо скипнуть")
                    driver.refresh()

            for good_key in good_ufo:
                if good_key in icon:
                    print(f"НЛО: {good_ufo[good_key]}, надо брать")
                    driver.find_element(By.XPATH, '//*[@id="Ufo_0"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="agi-10972849001709751854"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '/html/body/div[12]/aside/div[2]/button/span/span').click()
                    driver.refresh()
                    time.sleep(1)

            driver.get(driver.current_url)
            time.sleep(2)

    except:

        return


def check_equus(driver):
    try:
        equus = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/header/nav[1]/ul/li[8]/a/span/span[2]/strong'
        ).text.replace(' ', ''))

        if equus >= 10000:
            return 'Good'
        else:
            return 'Bad'
    except:
        driver.refresh()
        time.sleep(2)
        check_equus(driver)


def get_resurses(driver, name):
    resurses = {
        'wood': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[2]/td[5]/button/span/span/span/img'
        ),
        'iron': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[3]/td[5]/button/span/span/span/img'
        ),
        'sand': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[4]/td[5]/button/span/span/span/img'
        ),
        'skin': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[5]/td[5]/button/span/span/span/img'
        ),
        'straw': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[7]/td[5]/button/span/span/span/img'
        ),
        'flax': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[8]/td[5]/button/span/span/span/img'
        ),
        'wheat': driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/div/table/tbody/tr[10]/td[5]/button/span/span/span/img'
        ),
    }
    return resurses[name]


def spend_equus(driver, res='skin'):
    try:
        equus = int(driver.find_element(
            By.XPATH,
            '/html/body/div[7]/header/nav[1]/ul/li[8]/a/span/span[2]/strong'
        ).text.replace(' ', ''))
        driver.get('https://www.lowadi.com/marche/boutique')
        time.sleep(1)
        resurses = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[1]/ul/li[3]/div/a/img'
        ).click()
        time.sleep(3)
        iron = 10
        while equus > 10000:
            get_resurses(driver, res).click()
            time.sleep(1)
            quality = driver.find_element(
                By.XPATH,
                '/html/body/div[11]/div/div/table/tbody/tr[1]/td[1]/select/option[21]'
            ).click()
            time.sleep(1)
            confirm = driver.find_element(
                By.XPATH,
                '/html/body/div[11]/div/div/table/tbody/tr[1]/td[1]/button/span[2]'
            ).click()
            time.sleep(1)
            equus = int(driver.find_element(
                By.XPATH,
                '/html/body/div[7]/header/nav[1]/ul/li[8]/a/span/span[2]/strong'
            ).text.replace(' ', ''))
            time.sleep(1)

        driver.back()
    except:
        time.sleep(3)
        spend_equus(driver)


def login_lowadi(driver):
    now = datetime.now().strftime('%H:%M:%S')
    print(f'{now}: Логинимся на lowadi.com')
    url = 'https://www.lowadi.com'

    driver.get(url)

    try:
        print('Принимаем cookie')
        driver.find_element(By.XPATH, '/html/body/aside/div/article/div/div[2]/div/div/div[3]/form/button').click()

    except:
        print('Принять cookie не просили')

    try:

        print(f'Начинаем!')
        driver.find_element(By.XPATH, '/html/body/div[7]/header/nav/div/strong').click()
        time.sleep(2)
        if driver.find_element(By.XPATH, '//*[@id="login"]').text == '':
            print(f'Вводим логин..')
            login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
            time.sleep(1)
            print(f'Вводим пароль..')
            password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
            time.sleep(1)
        print(f'Входим')
        connect = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/header/nav/div/div/form/button/span/span/span'
        ).click()
        time.sleep(2)

    except:

        url = 'https://www.lowadi.com/elevage/chevaux/cheval?id=20378769'
        driver.get(url)

        print(f'Пробуем зайти заново')
        time.sleep(10)
        if driver.find_element(By.XPATH, '//*[@id="login"]').text == '':
            print(f'Вводим логин..')
            login = driver.find_element(By.XPATH, '//*[@id="login"]').send_keys('Kolgotki')
            time.sleep(1)
            print(f'Вводим пароль..')
            password = driver.find_element(By.XPATH, '//*[@id="password"]').send_keys('Sirok123')
            time.sleep(1)
            print(f'Входим')
        connect = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/aside/form/button'
        ).click()
        time.sleep(10)


def xanthos(driver):
    """
    Ежедневная глажка 5 Ксанфов.
    Есть вероятность получить рог изобилия.
    :return:
    """
    urls = [
        'https://www.lowadi.com/elevage/fiche/?id=1045736',
        'https://www.lowadi.com/elevage/fiche/?id=1047131',
        'https://www.lowadi.com/elevage/fiche/?id=1044747',
        'https://www.lowadi.com/elevage/fiche/?id=1044960',
        'https://www.lowadi.com/elevage/fiche/?id=1046269'
    ]
    print('Гладим Ксанфов')
    for url in urls:
        driver.get(url)
        time.sleep(2)
        pat_xanthos = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/div[2]'
            '/div/div/div/div/div/div[1]/table/tbody/tr/td[3]/form/a'
        ).click()
        time.sleep(2)


def topaz(driver):
    """
    Ежедневная глажка 5 Топазов.
    Есть вероятность получить 10 пропусков.
    :return:
    """
    urls = [
        'https://www.lowadi.com/elevage/fiche/?id=4763736',
        'https://www.lowadi.com/elevage/fiche/?id=4775333',
        'https://www.lowadi.com/elevage/fiche/?id=4771120',
        'https://www.lowadi.com/elevage/fiche/?id=4792032',
        'https://www.lowadi.com/elevage/fiche/?id=4789329'
    ]
    print('Гладим Топазов')
    for url in urls:
        driver.get(url)
        time.sleep(2)
        pat_topaz = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/div[2]'
            '/div/div/div/div/div/div[1]/table/tbody/tr/td[3]/form/a'
        ).click()
        time.sleep(2)


def givre(driver):
    """
    Ежедневная разморозка Морозницы.
    Есть вероятность получить Одеяло Гипноса.
    :return:
    """
    urls = [
        'https://www.lowadi.com/elevage/fiche/?id=12086505'
    ]
    print('Размораживаем Морозницу')
    for url in urls:
        driver.get(url)
        time.sleep(2)
        pat_givre = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/div[2]/'
            'div/div/div/div/div/div[1]/table/tbody/tr/td[3]/a'
        ).click()
        time.sleep(2)


def atelier(driver, workshop=3):
    print(datetime.now().strftime('%H:%M:%S'), 'Проверяем мастерские..')
    url = 'https://www.lowadi.com/centre/atelier/'
    driver.get(url)
    try:
        for _ in range(workshop):
            try:
                get_stable_1 = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/form/table/tbody/tr[6]/td[6]/a/span'
                )
            except:
                get_stable_1 = driver.find_element(
                    By.XPATH,
                    '/html/body/div[8]/main/section/section/form/table/tbody/tr[6]/td[6]/a/span'
                )

            match get_stable_1.text:
                case 'Получить':
                    print('Стойла готовы, собираем')
                    get_stable_1.click()
                    time.sleep(2)
                    try:
                        driver.find_element(
                            By.XPATH,
                            '/html/body/div[11]/div/div/form/button/span/span/span'
                        ).click()
                    except:
                        driver.find_element(
                            By.XPATH,
                            '/html/body/div[12]/div/div/form/button/span/span/span'
                        ).click()
                    time.sleep(2)
                case 'Стоп':
                    print('Стойла не готовы, сваливаем')
                    return 0

        for _ in range(workshop):
            begin_stable = driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/form/table/tbody/tr[1]/td[6]/button/span/span/span'
            )
            match begin_stable.text:
                case 'Производство':
                    print('Мастерская свободна, пора запускать постройку стойла')
                    begin_stable.click()
                    time.sleep(2)
                    driver.find_element(
                        By.XPATH,
                        '/html/body/div[12]/div/div/div/div/div/div/div[1]/div/div[3]/div[1]/div/span'
                    ).click()
                    time.sleep(2)
                    driver.find_element(
                        By.XPATH,
                        '/html/body/div[12]/div/div/div/div/div/div/div[2]/form[8]/div[2]/button/span/span/span'
                    ).click()
                    time.sleep(2)

    except:
        print('Проверка мастерской провалилась')


def refresh(driver):
    driver.refresh()
    time.sleep(2)


def quit_lowadi(driver):
    print(f'{datetime.now().strftime("%H:%M:%S")}: закрываем chrome')
    driver.quit()
