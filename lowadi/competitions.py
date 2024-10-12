import time
import pretty_errors
from selenium.webdriver.common.by import By
import re


def get_competition_galop(driver):
    click_competition = driver.find_element(
        By.XPATH,
        '//*[@id="competition-body-content"]/table/tbody/tr[1]/td[2]/a'
    ).click()
    time.sleep(5)
    try:
        run = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]'
            '/td/div/table/tbody/tr[1]/td[8]/button/span/span/span'
        ).click()
    except:
        run = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[8]/button/span/span/span'
        ).click()

    time.sleep(3)


def get_competition_trot(driver):
    click_competition = driver.find_element(
        By.XPATH,
        '//*[@id="competition-body-content"]/table/tbody/tr[1]/td[1]/a'
    ).click()
    time.sleep(5)
    try:
        run = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]'
            '/td/div/table/tbody/tr[1]/td[8]/button/span/span/span'
        ).click()
    except:
        run = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[8]/button/span/span/span'
        ).click()

    time.sleep(3)


def get_competition_jump(driver):
    click_competition = driver.find_element(
        By.XPATH,
        '//*[@id="competition-body-content"]/table/tbody/tr[2]/td[3]/a'
    ).click()
    time.sleep(5)
    try:
        run = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]'
            '/td/div/table/tbody/tr[1]/td[8]/button/span/span/span'
        ).click()
    except:
        run = driver.find_element(
            By.XPATH,
            '/html/body/div[7]/main/section/section/div/div/div[1]/table/tbody/tr[1]/td[8]/button/span/span/span'
        ).click()

    time.sleep(3)


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

        if eclair and last_place:
            return td_elements[7]




