import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pretty_errors
import os
import requests
import re
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

extension = 'omghfjlpggmjjaagoclmmobgdodcjboh'


def new_drb():
    chrome_options = uc.ChromeOptions()

    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "normal"

    chrome_options.headless = False
    driver = uc.Chrome(options=chrome_options, desired_capabilities=caps)

    return driver


def new_brave_dr():
    brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
    chromedriver_path = r"C:\Users\user\PycharmProjects\InnokentiyHomeWorker\chromedriver.exe"

    chrome_options = uc.ChromeOptions()
    chrome_options.binary_location = brave_path
    chrome_options.add_argument("--single-process")
    chrome_options.headless = False

    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"

    service = Service(chromedriver_path)
    driver = uc.Chrome(service=service, options=chrome_options, desired_capabilities=caps)

    return driver


def check_for_chrome_update():
    driver = new_drb()
    driver.get("chrome://version/")

    status_element = driver.find_element(
        By.XPATH,
        '/html/body/div[1]/table/tbody/tr[1]/td[2]/span'
    )

    # Проверяем статус обновления
    update_text = status_element.text
    print(f"Статус обновления: {update_text}")

    if "Доступно обновление" in update_text:
        print("Обновление доступно. Запуск загрузки...")
        # Нажимаем кнопку обновления
        update_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Перезагрузить')]")
        update_button.click()
        print("Обновление установлено. Требуется перезагрузка браузера.")
    else:
        print("Установлена последняя версия Chrome.")