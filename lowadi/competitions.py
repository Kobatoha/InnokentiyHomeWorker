import time
import pretty_errors
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import re
from lowadi.care import get_current_url
from lowadi.other import check_ufo


def check_equip(driver):
    equip = False
    try:
        equipement = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[4]/div/div/div/div/table[1]'
            '/tbody[2]/tr/td/div/div/table/tbody/tr/td[1]/div/div'
        ).text
        if 'пока нельзя надеть снаряжение' in equipement:
            equip = False

        equipement = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[2]/div[4]/div/div/div/div/table[1]'
                '/tbody[2]/tr/td/div/div/table/tbody/tr/td[1]/div/div[2]/div[2]/ul/li[1]/a'
            ).get_attribute('data-tooltip')
        if 'Нет вальтрапа' in equipement:
            equip = False
        else:
            equip = True

    except:
        return equip

    return equip


def equiped_horse(driver, _type='public'):

    try:
        try:
            driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[4]/div/div/div/div/div/a/span[1]'
            ).click()
            time.sleep(2)

            equip = {
                'tapis': ['/html/body/div[11]/span/div/div[1]/div[2]/div[2]',
                          '/html/body/div[11]/span/div/div[1]/form/div[1]/div'],
                'selle': ['/html/body/div[11]/span/div/div[1]/div[2]/div[3]',
                          '/html/body/div[11]/span/div/div[1]/form/div[2]/div'],
                'bride': ['/html/body/div[11]/span/div/div[1]/div[2]/div[4]',
                          '/html/body/div[11]/span/div/div[1]/form/div[3]/div']
            }
        except:
            driver.find_element(
                By.XPATH,
                '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[4]/div/div/div/div/div/a/span[1]'
            ).click()
            time.sleep(2)

            equip = {
                'tapis': ['/html/body/div[12]/span/div/div[1]/div[2]/div[2]',
                          '/html/body/div[12]/span/div/div[1]/form/div[1]/div'],
                'selle': ['/html/body/div[12]/span/div/div[1]/div[2]/div[3]',
                          '/html/body/div[12]/span/div/div[1]/form/div[2]/div'],
                'bride': ['/html/body/div[12]/span/div/div[1]/div[2]/div[4]',
                          '/html/body/div[12]/span/div/div[1]/form/div[3]/div']
            }

        for i in equip:
            item = driver.find_element(
                By.XPATH,
                equip[i][0]
            )

            item.click()
            offers = driver.find_elements(
                By.XPATH,
                equip[i][1]
            )
            for offer in offers:
                if 'Предлагается конноспортивным комплексом!' in offer.text:
                    print(item.text, ':', offer.text)
                    offer.click()

            time.sleep(1)

        try:
            agree = driver.find_element(
                By.XPATH,
                '/html/body/div[11]/span/div/button/span/span/span'
            ).click()
            time.sleep(1)
        except:
            agree = driver.find_element(
                By.XPATH,
                '/html/body/div[12]/span/div/button/span/span/span'
            ).click()
            time.sleep(1)

    except:
        pass


def choice_specialisation(driver, _type='classique'):
    try:
        if _type == 'classique':
            try:
                driver.find_element(
                    By.XPATH,
                    '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[4]'
                    '/div/div/div/div/div/div/div/ul/li[1]/span[3]/form/button/span/span'
                ).click()
            except:
                driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[4]'
                    '/div/div/div/div/div/div/div/ul/li[1]/span[3]/form/button/span/span'
                ).click()
            time.sleep(1)
            print(f'Выбрали специализацию {_type}')

        elif _type == 'western':
            try:
                driver.find_element(
                    By.XPATH,
                    '/html/body/div[8]/main/section/section/div[5]/div/div[3]/div[4]'
                    '/div/div/div/div/div/div/div/ul/li[2]/span[3]/form/button/span/span'
                ).click()
            except:
                driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div[5]/div/div[3]/div[4]'
                    '/div/div/div/div/div/div/div/ul/li[2]/span[3]/form/button/span/span'
                ).click()
            time.sleep(1)
            print(f'Выбрали специализацию {_type}')

        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(1)

    except:
        pass


def get_stable_with_equip(driver, race='andalusian'):
    specialisation = {
        'classique': ['andalusian', 'francais', 'goland', 'lusitanien'],
        'western': ['marshadore']
    }
    options = {
        'days': '/html/body/div[7]/main/section/section/div[1]/table/thead/tr/td[6]/span[2]/span/span[3]/a',
        'selle': '//*[@id="search-line"]/table/tbody/tr[2]/td[1]/span[5]',
        'bride': '//*[@id="search-line"]/table/tbody/tr[2]/td[1]/span[6]',
        'tapis': '//*[@id="search-line"]/table/tbody/tr[2]/td[1]/span[7]',
        'classic': '//*[@id="classiqueLabel"]'
    }

    if race in specialisation['classique']:
        options['classic'] = '//*[@id="classiqueLabel"]'
    else:
        options['classic'] = '//*[@id="westernLabel"]'

    try:
        if 'Зарегистрируйте свою лошадь' in driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[1]'
                '/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
        ).text:

            print('Лошадь нуждается в стойле со снаряжением..')

            current_url = get_current_url(driver)

            find_stable = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[5]/div/div[1]'
                '/div[2]/div/div/div[2]/div/div[2]/div/div/span/span[2]/a'
            ).click()
            time.sleep(3)

            check_ufo(driver)

            for i in options:
                driver.find_element(By.XPATH, options[i]).click()
                time.sleep(2)

            find = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[1]/form/button[1]/span/span/span'
            ).click()
            time.sleep(2)

            first_offer = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div[1]/table/tbody'
                '/tr[1]/td[7]/button/span/span/span/span/strong'
            )
            print(f'Стоимость стойла с амунницией за 3 дня составляет: {first_offer.text} экю')

            first_offer.click()

            time.sleep(1)
            return 1

    except:

        return 0


def choice_competition(driver, race='andalusian'):
    if race == 'andalusian':
       cost = get_competition_galop(driver)
    elif race == 'francais':
       cost = get_competition_trot(driver)
    elif race == 'goland':
       cost = get_competition_jump(driver)

    return cost


def get_cost_and_run_competition(driver):
    try:
        try:
            cost = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[7]'
            ).text.split(' ')[0]
            run = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]'
                '/td/div/table/tbody/tr[1]/td[8]/button/span/span/span'
            ).click()

        except:
            cost = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody'
                '/tr[1]/td/div/table/tbody/tr[1]/td[7]'
            ).text.split(' ')[0]
            run = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody'
                '/tr[1]/td/div/table/tbody/tr[1]/td[8]/button/span/span/span'
            ).click()

    except:
        cost = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[2]/td[7]'
        ).text.split(' ')[0]
        run = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[8]/button/span/span/span'
        ).click()

    return cost


def get_competition_galop(driver):
    click_competition = driver.find_element(
        By.XPATH,
        '//*[@id="competition-body-content"]/table/tbody/tr[1]/td[2]/a'
    ).click()
    time.sleep(2)
    try:
        try:
            try:
                cost = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]'
                    '/td/div/table/tbody/tr[1]/td[7]'
                ).text.split(' ')[0]
                run = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]'
                    '/td/div/table/tbody/tr[1]/td[8]'
                ).click()
            except:
                cost = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div/div[2]/div/div[1]/table/tbody/tr[1]/td[7]'
                ).text.split(' ')[0]
                run = driver.find_element(
                    By.XPATH,
                    '/html/body/div[7]/main/section/section/div/div[2]/div/div[1]/table/tbody/tr[1]/td[8]'
                ).click()
        except:
            cost = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[7]'
            ).text.split(' ')[0]
            run = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[8]'
            ).click()
    except:
        try:
            cost = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div[2]/div/div[1]/table/tbody'
                '/tr[1]/td/div/table/tbody/tr[1]/td[7]'
            ).text.split(' ')[0]
            run = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div[2]/div/div[1]/table/tbody'
                '/tr[1]/td/div/table/tbody/tr[1]/td[8]'
            ).click()
        except:
            cost = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div/div[2]/table/tbody/tr[1]/td[7]'
            ).text.split(' ')[0]
            run = driver.find_element(
                By.XPATH,
                '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[8]/button/span/span/span'
            ).click()

    return float(cost)


def get_competition_trot(driver):
    click_competition = driver.find_element(
        By.XPATH,
        '//*[@id="competition-body-content"]/table/tbody/tr[1]/td[1]/a'
    ).click()
    time.sleep(3)

    cost = get_cost_and_run_competition(driver)

    return float(cost)


def get_competition_jump(driver):
    click_competition = driver.find_element(
        By.XPATH,
        '//*[@id="competition-body-content"]/table/tbody/tr[2]/td[3]/a'
    ).click()
    time.sleep(3)

    cost = get_cost_and_run_competition(driver)
    return float(cost)


def find_fast_competition(driver, _type='public', _eclair=False):
    competitions = driver.find_elements(By.XPATH, '//*[@id="public"]/tbody/tr')

    eclair = False
    last_place = False

    if _type == 'divine':
        competitions = driver.find_elements(By.XPATH, '//*[@id="slide-divin"]/div/table/tbody/tr')
    elif _type == 'race':
        competitions = driver.find_elements(By.XPATH, '//*[@id="slide-race"]/div/table/tbody/tr')

    for competition in competitions:
        td_elements = competition.find_elements(By.XPATH, './td')

        if td_elements[5].text == '1':
            last_place = True

        if _eclair:
            try:
                find_eclair = td_elements[1].find_element(By.XPATH, './div/div').get_attribute('data-tooltip')
                if 'эту розетку' in find_eclair:
                    eclair = True
                return td_elements[7]
            except:
                pass

        else:
            eclair = False

        return td_elements[7]




