import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.chrome.service import Service
import pretty_errors

extension = 'omghfjlpggmjjaagoclmmobgdodcjboh'


def new_drb():
    chromeOptions = uc.ChromeOptions()
    caps = DesiredCapabilities().CHROME
    caps["pageLoadStrategy"] = "eager"
    chromeOptions.headless = False
    driver = uc.Chrome(options=chromeOptions, desired_capabilities=caps)

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
